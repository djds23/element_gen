import os

import py.test

from element_gen.TwitterElement import TwitterElement

def test_twitter_element():
    os.system('rm *png *mp4')
    test = TwitterElement('RuthBourdain')
    assert 'RuthBourdain.mp4' in os.listdir('.')

def test_exception():
    with py.test.raises(ValueError):
        test = TwitterElement()

