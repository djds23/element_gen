import uuid
import math
import os
import re

import moviepy.editor

from wand.image import Image
from wand.color import Color
from wand.drawing import Drawing


class Element(object):
    '''Construct the video, all resolutions set to be 1280x720
       Filename in this context refers to the source file,
       remember this was originally developed to create title screens
    '''


    def __init__(self, filename=None, quote='', duration=10, author=''):
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
        else:
            raise NameError('File is not .jpg or .png!')


    def blur_background(self):
        '''create image and return the name of the new file'''
        with Image(filename=self.filename) as img:
            with img.clone() as blurred:
                blurred.gaussian_blur(0,6)
                blurred.save(filename=self.blurred)

    def size_rectangle(self):
        '''Determine the size of inner rectangle, bloated and
        poorly executed'''
        ratio = 1.61803398875
        self.inner_width = int(self.width/ratio)
        self.inner_height = int(self.height/ratio)
        self.quote = '\"' + self.quote + '\"'
        character_length = len(self.quote)
        not_area = (character_length * 2)/ratio
        self.font_size = int(math.sqrt(not_area))
        self.width_margin = (self.width-self.inner_width)/2
        self.height_margin = (self.height-self.inner_height)/2
        self.start_width = self.width_margin + self.font_size + 1
        self.start_height = self.height_margin + self.font_size + 1
        char_per_line = (self.inner_width/self.font_size) * 2
        num_of_lines = self.inner_height/self.font_size + 1
        self.clips = []
        original = self.quote
        start_height = self.start_height
        for line in range(num_of_lines):
            segment = moviepy.editor.TextClip(original[:char_per_line],
                                            fontsize=self.font_size,
                                            font='Century-Schoolbook-L-Roman')
            segment = segment.set_pos((
                            self.start_width,
                             start_height)).set_duration(self.duration)
            self.clips.append(segment)
            if len(original) >= char_per_line:
                original = original[char_per_line:]
                start_height += (self.font_size+1)
            else:
                break

    def create_rectangle(self):
        with Color('white') as color:
            with Image(width=self.inner_width, height=self.inner_height,
                    background=color) as image:
                image.save(filename=self.rectangle)

    def merge(self):
        '''take all parts and make a movie!'''
        background = moviepy.editor.ImageClip(self.blurred)
        background = background.set_duration(self.duration)
        rectangle = moviepy.editor.ImageClip(self.rectangle).set_pos('center')
        rectangle = rectangle.set_duration(self.duration)
        author = moviepy.editor.TextClip(self.author,
                                        fontsize=self.font_size,
                                        font='Century-Schoolbook-L-Roman')
        author = author.set_pos((840,520)).set_duration(self.duration)
        self.clips.insert(0, background)
        self.clips.insert(1, rectangle)
        self.clips.insert(2, author)
        video = moviepy.editor.CompositeVideoClip(self.clips)
        video.to_videofile(self.video, fps=24)
