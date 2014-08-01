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

class Twitter_Element(object):

    def __init__(self, username):
        self.username = username
        self.get_tweets(self.username)
        self.tile_photo()
        self.tweet_canvas(self.tweets[0])
        self.filename = str(uuid.uuid4())+'.jpg'
        self.canvas.save(self.filename)

    def get_tweets(self, username):
        url = urlopen("https://twitter.com//" + self.username)
        page = BeautifulSoup(url)
        url.close()

        tweets = [p.text for p in page.findAll("p")
                if ("class" in p.attrs) and
                ("ProfileTweet-text" in p.attrs["class"])]

        prof_pic = [img.attrs["src"] for img in page.findAll("img")
                    if ("class" in img.attrs) and
                    ("ProfileAvatar-image" in img.attrs["class"])]
        self.profile_photo = str(uuid.uuid4())+'.jpg'
        urlretrieve(prof_pic[0], self.profile_photo)
        urlcleanup()
        self.i_file = Image.open(self.profile_photo)
        self.tweets = tweets

    def tile_photo(self):
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
        tweet_canvas_size = (3*self.i_file.size[0], self.i_file.size[1])
        tweet_canvas = Image.new('RGB', tweet_canvas_size, 'white')
        tweet_canvas.paste(self.i_file, (0,0))
        draw = ImageDraw.Draw(tweet_canvas)
        font = ImageFont.truetype(CONFIGURE['FONTPATH'], 16, 0)
        self.prep_tweet(tweet, draw, font)
        draw.text((1000, 340), '@' + self.username, (0,0,0), font)
        self.canvas.paste(tweet_canvas, (40,160))

    def prep_tweet(self, tweet, draw, font=None):
        tweet = tweet.encode('ascii', 'ignore')
        tweet = textwrap.wrap(tweet, 70)
        max_height = 80
        max_width = 1600
        color = (0,0,0)
        full_line = ''
        for line in tweet:
            width, height = draw.textsize(line, font)
            draw.text(((max_width-width)/2, max_height), line, color, font)
            max_height += 40
