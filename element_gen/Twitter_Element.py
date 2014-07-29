import uuid
import math
import os
import re

from PIL import Image

import moviepy.editor

from .Element import Element

from urllib import urlopen, urlretrieve, urlcleanup

from bs4 import BeautifulSoup

class Twitter_Element(Element):

    def __init__(self, username):
        self.username = username
        self.get_tweets(self.username)
        self.tile_photo()
        super(Twitter_Element, self).__init__(filename=self.tile_filename)


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
        self.tweets = tweets

    def tile_photo(self):
        i_file = Image.open(self.profile_photo)
        canvas_size = (1280,720)
        canvas = Image.new('RGB', canvas_size)
        start_width = 0
        start_height = 0
        while start_height<canvas_size[1]:
            while start_width<canvas.size[0]:
                canvas.paste(i_file, (start_width, start_height))
                start_width += i_file.size[0]
            start_width = 0
            start_height += i_file.size[1]
        self.tile_filename = str(uuid.uuid4())+'.jpg'
        canvas.save(self.tile_filename)

