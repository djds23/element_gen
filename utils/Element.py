from wand.image import Image
from wand.color import Color
from wand.drawing import Drawing

import moviepy.editor

import uuid
import math
import os

class Element(object):
    '''Construct the video, all resolutions set to be 1280x720'''

    def __init__(self, filename=None, quote='',
            duration=10, author=''):
        self.filename = filename
        self.quote = quote
        self.author = author
        self.duration =duration
        if self.filename.endswith('.jpg' or '.png'):
            self.blurred = str(uuid.uuid4()) + '.png'
            self.rectangle = str(uuid.uuid4()) + '.png'
            self.video = str(uuid.uuid4()) + '.mp4'
            self.width = 1280
            self.height = 720
            self.inner_width=906
            self.inner_height=560
        else:
            raise NameError('File is not .jpg or .png!')

    def create_rectangle(self):
        with Color('white') as color:
            with Image(width=self.inner_width, height=self.inner_height,
                    background=color) as image:
                image.save(filename=self.rectangle)

    def create_background(self):
        '''create image and return the name of the new file'''
        with Image(filename=self.filename) as img:
            with img.clone() as blurred:
                blurred.gaussian_blur(0,6)
                blurred.save(filename=self.blurred)

    def size_rectangle(self):
        '''Determine the size of inner rectangle'''
        ratio = 1.61803398875
        quote = '\"' + self.quote + '\"'
        character_length=len(quote)
        area_per_char = character_length/ratio
        self.font_size = int(math.sqrt(area_per_char))
        self.start_width = (self.width-self.inner_width) + (self.font_size+1)
        self.start_height = (self.height-self.inner_height) + (self.font_size+1)

    def merge(self):
        background = moviepy.editor.ImageClip(self.blurred)
        rectangle = moviepy.editor.ImageClip(self.rectangle)
        quote = moviepy.editor.TextClip(self.quote,fontsize=self.font_size,
                font='Century-Schoolbook-L-Roman')
        author = moviepy.editor.TextClip(self.author, fontsize=self.font_size,
                font='Century-Schoolbook-L-Roman')
        video = moviepy.editor.CompositeVideoClip([
            background.set_duration(self.duration),
            rectangle.set_pos('center').set_duration(self.duration),
            quote.set_pos((self.start_width, self.start_height)).set_duration(self.duration),
            author.set_pos((720,500)).set_duration(self.duration)])
        video.to_videofile(self.video, fps=60)
