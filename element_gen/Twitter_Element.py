import uuid
import math
import os
import re

from PIL import Image, ImageFilter

import moviepy.editor

from .Element import Element

from urllib import urlopen, urlretrieve, urlcleanup

from bs4 import BeautifulSoup

class Twitter_Element(Element):

    def __init__(self, username):
        self.username = username
        self.get_tweets(self.username)
        self.tile_photo()
        self.tweet_canvas()
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

    def tweet_canvas(self):
        tweet_canvas_size = (3*self.i_file.size[0], self.i_file.size[1])
        tweet_canvas = Image.new('RGB', tweet_canvas_size, 'white')
        tweet_canvas.paste(self.i_file, (0,0))
        self.canvas.paste(tweet_canvas, (40,160))
