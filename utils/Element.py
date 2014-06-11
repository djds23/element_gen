from wand.image import Image
from wand.color import Color
from wand.drawing import Drawing

import moviepy.editor

import uuid

import os 

class Element(object):

    def __init__(self, filename=None, text='', 
            duration=10, author=''):
        self.filename = filename
        self.text = text
        self.author = author
        self.duration =duration
        if self.filename.endswith('.jpg' or '.png'):
            self.blurred = str(uuid.uuid4()) + '.png'
            self.rectangle = str(uuid.uuid4()) + '.png'
            self.video = str(uuid.uuid4()) + '.mp4'
            self.width=800
            self.height=400
        else:
            raise NameError('File is not .jpg or .png!')
    
    def create_rectangle(self):
        with Color('white') as color:
            with Image(width=self.width, height=self.height, background=color) as image:
                image.save(filename=self.rectangle)

    def create_background(self):
        '''create image and return the name of the new file'''
        with Image(filename=self.filename) as img:
            with img.clone() as blurred:
                blurred.gaussian_blur(0,6)
                blurred.save(filename=self.blurred)

    def merge(self):    
        background = moviepy.editor.ImageClip(self.blurred)
        rectangle = moviepy.editor.ImageClip(self.rectangle)
        text = moviepy.editor.TextClip(self.text,fontsize=70, font='Century-Schoolbook-L-Roman')
        author = moviepy.editor.TextClip(self.author, fontsize=18, font='Century-Schoolbook-L-Roman')
        video = moviepy.editor.CompositeVideoClip([
            background.set_duration(self.duration),
            rectangle.set_pos('center').set_duration(self.duration),
            text.set_pos('center').set_duration(self.duration),
            author.set_pos((720,500)).set_duration(self.duration)])
        video.to_videofile(self.video, fps=60)
