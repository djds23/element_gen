from utils.Element import Element

from loremipsum import get_paragraph

import pytest

import os

text = get_paragraph()

def test_elements():
    test = Element(filename='test.jpg', quote=text,
            author='Lorem Ipsum', duration=1)
    before = os.listdir('.')
    test.create_background()
    test.size_rectangle()
    test.create_rectangle()
    assert isinstance(test.clips, list)
    test.merge()
    assert len(os.listdir('.'))-len(before)==3
    with pytest.raises(NameError) as execinfo:
        bad = Element(filename='bad_filename')
    os.system('rm *png')
    os.system('ffplay *mp4')
