from wand.image import Image
from wand.color import Color
from wand.drawing import Drawing

import uuid

import os 

class Element(object):

    def __init__(self, filename=None, quote=None, author=None):
        self.filename = filename
        self.quote = quote
        self.author = author
        if self.filename.endswith('.jpg' or '.png'):
            self.blurred = str(uuid.uuid4()) + '.png'
            self.rectangle = str(uuid.uuid4())+ '.png'
        else:
            raise NameError('File is not .jpg or .png!')
    
    def format_content(self):
        '''
        There should be logic to control the quote.
        Make sure quote is not too long, make sure the rectangle
        will fit the quote
        '''
        self.width=800
        self.height=400
        pass

    def create_rectangle(self):
        with Color('white') as color:
            with Image(width=self.width, height=self.height, background=color) as image:
                image.save(filename=self.rectangle)
                return self.rectangle


    def create_background(self):
        '''create image and return the name of the new file'''
        with Image(filename=self.filename) as img:
            with img.clone() as blurred:
                blurred.gaussian_blur(0,6)
                blurred.save(filename=self.blurred)
        return self.blurred
