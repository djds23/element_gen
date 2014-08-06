element_gen
===========

Create video slideshows from your favorite twitter feed!

To install it, clone this repo then run ``pip install -r requirements.txt`` and ``pip install -e .``

usage goes as follows,

```python
from element_gen import TwitterElement

djds23 = TwitterElement('djds23')
djds23.create_slideshow() #create the slideshow!
djds23.clean_up() #delete temporary files

