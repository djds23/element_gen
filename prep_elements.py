from wand.image import Image
from wand.color import Color

import uuid

import os 

class Element(object):

    def __init__(self, filename=None, quote=None, author=None):
        self.filename = filename
        self.quote = quote
        self.author = author
        if self.filename.endswith('.jpg' or '.png'):
            self.blurred = str(uuid.uuid4()) + '.png'
        else:
            raise NameError('File is not .jpg or .png!')
 
    def 


    def create_background(self):
        with Image(filename=self.filename) as img:
            with img.clone() as blurred:
                blurred.gaussian_blur(0,6)
                blurred.save(filename=self.blurred)
        return self.blurred
