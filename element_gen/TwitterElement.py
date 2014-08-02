import textwrap
import uuid
import os

from PIL import Image, ImageFilter, ImageDraw, ImageFont

import moviepy.editor

from urllib import urlopen, urlretrieve, urlcleanup

from bs4 import BeautifulSoup

CONFIGURE = {
        'FONTPATH': '/usr/share/fonts/truetype/freefont/FreeSans.ttf'
        }

class TwitterElement(object):
    '''Write a video from a user's tweets'''
    def __init__(self, username=None):
        if username:
            self.username = username
            self.get_tweets(self.username)
            self.tile_photo()
            self.files = []
            for tweet in self.tweets:
                self.tweet_canvas(tweet)
                self.filename = str(uuid.uuid4())+'.png'
                self.canvas.save(self.filename)
                self.files.append(self.filename)
            self.merge_tweets()
        else:
            raise ValueError('Please provide a username!')

    def get_tweets(self, username):
        '''Pull down the latest tweets from the provided username'''
        url = urlopen("https://twitter.com//" + self.username)
        page = BeautifulSoup(url)
        url.close()

        tweets = [p.text for p in page.findAll("p")
                if ("class" in p.attrs) and
                ("ProfileTweet-text" in p.attrs["class"])]

        prof_pic = [img.attrs["src"] for img in page.findAll("img")
                    if ("class" in img.attrs) and
                    ("ProfileAvatar-image" in img.attrs["class"])]
        self.profile_photo = str(uuid.uuid4())+'.png'
        urlretrieve(prof_pic[0], self.profile_photo)
        urlcleanup()
        self.i_file = Image.open(self.profile_photo)
        self.tweets = tweets

    def tile_photo(self):
        '''Creates a mosaic from the users profile picture'''
        canvas_size = (1280,720)
        canvas = Image.new('RGB', canvas_size)
        start_width = int(-self.i_file.size[0]/1.618)
        start_height = int(-self.i_file.size[1]/1.618)
        while start_height<canvas_size[1]:
            while start_width<canvas.size[0]:
                canvas.paste(self.i_file, (start_width, start_height))
                start_width += self.i_file.size[0]
            start_width = int(-self.i_file.size[0]/1.618)
            start_height += self.i_file.size[1]
        self.canvas = canvas.filter(ImageFilter.GaussianBlur(12))

    def tweet_canvas(self, tweet):
        '''Makes a canvas for the user's tweets'''
        tweet_canvas_size = (3*self.i_file.size[0], self.i_file.size[1])
        tweet_canvas = Image.new('RGB', tweet_canvas_size, 'white')
        tweet_canvas.paste(self.i_file, (0,0))
        draw = ImageDraw.Draw(tweet_canvas)
        font = ImageFont.truetype(CONFIGURE['FONTPATH'], 26, 0)
        self.prep_tweet(tweet, draw, font)
        draw.text((1000, 340), '@' + self.username, (0,0,0), font)
        self.canvas.paste(tweet_canvas, (40,160))

    def prep_tweet(self, tweet, draw, font=None):
        '''Encode the tweets as ascii, and wrap the text for the canvas'''
        tweet = tweet.encode('ascii', 'ignore')
        tweet = textwrap.wrap(tweet, 60)
        max_height = 80
        max_width = 1600
        color = (0,0,0)
        full_line = ''
        for line in tweet:
            width, height = draw.textsize(line, font)
            draw.text(((max_width-width)/2, max_height), line, color, font)
            max_height += 40

    def merge_tweets(self):
        '''Make the final slideshow'''
        self.image_clips = [moviepy.editor.ImageClip(img).set_duration(6)\
                            for img in self.files]
        clip = moviepy.editor.concatenate(self.image_clips)
        clip.to_videofile(self.username+'.mp4', fps=24)
