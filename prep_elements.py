from wand.image import Image
from wand.color import Color

import uuid

import os 

class Elements(object):

    def __init__(filename=None, quote=None, author=None):
        self.filename = filename
        self.quote = quote
        self.author = author

    def create_background():
        if self.filename.endswith('.jpg' or '.png'):
            self.blurred = uuid.uuid4() + '.png'
            with Image(filename=self.filename) as img:
                with img.clone() as blurred:
                    blurred.gaussian_blur(0,6)
                    blurred.save(filename=self.blurred)
        else:
            raise NameError('File is not .jpg or .png!')
