element_gen
===========

Create video slideshows from your favorite twitter feed!

To install it, clone this repo then run ``pip install -r requirements.txt`` and ``pip install -e .``

You also must install the font:

``http://www.fontspace.com/gnu-freefont/freesans``

unfortunately this font is hardcoded to the filepath:

``/usr/share/fonts/truetype/freefont/FreeSans.ttf``

Looking for a workaround.

This build also requires ffmpeg & all of the moviepy requirements.

usage goes as follows,

```python
from element_gen import TwitterElement

djds23 = TwitterElement('djds23')
djds23.create_slideshow() #create the slideshow!
djds23.clean_up() #delete temporary files

