import os

import py.test

from element_gen import TwitterElement

def test_twitter_element():
    test = TwitterElement('dontusethiscode')
    test.create_slideshow()
    assert test.slideshow_filename in os.listdir('.')
    for slide in test.tempfiles:
        assert os.path.exists(slide)
    test.clean_up()
    for slide in test.tempfiles:
        assert os.path.exists(slide) == False

def test_exception():
    with py.test.raises(ValueError):
        test = TwitterElement()

