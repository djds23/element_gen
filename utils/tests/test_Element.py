from utils.Element import Element

import pytest

import os

def test_elements():
    test = Element(filename='test.jpg', text='Hello World', author='Dean Rex', duration=1)
    before = os.listdir('.')
    test.create_background()
    test.create_rectangle()
    test.merge()
    assert len(os.listdir('.'))-len(before)==3
    with pytest.raises(NameError) as execinfo:
        bad = Element(filename='bad_filename')
    os.system('rm *png')
