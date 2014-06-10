from utils.Element import Element
from utils.CreateMedia import CreateMedia

import pytest

import os

def test_elements():
    test = Element(filename='test.jpg', text='Hello World')
    before = os.listdir('.')
    test.format_content()
    test.create_background()
    test.create_rectangle()
    test.merge()
    assert len(os.listdir('.'))-len(before)==3
    with pytest.raises(NameError) as execinfo:
        bad = Element(filename='bad_filename')

