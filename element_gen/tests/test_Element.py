import random
import os

import pytest
from loremipsum import get_paragraph, get_sentence

from element_gen.Element import Element

quote = get_paragraph()

name_pool = get_sentence()

name_pool = name_pool.split()

author = random.choice(name_pool) + ' ' + random.choice(name_pool)

def test_elements():
    try:
        os.system('rm *mp4')
        os.system('rm *png')
    except:
        pass
    test = Element(filename='test.jpg', quote=quote,
            author=author, duration=1)
    before = os.listdir('.')
    test.blur_background()
    test.size_rectangle()
    test.create_rectangle()
    assert isinstance(test.clips, list)
    test.merge()
    assert len(os.listdir('.'))-len(before)==3
    with pytest.raises(NameError) as execinfo:
        bad = Element(filename='bad_filename')
    os.system('ffplay *mp4')
