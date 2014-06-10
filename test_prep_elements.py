from prep_elements import Element

import os

def test_elements():
    test = Element(filename='test.jpg')
    before = os.listdir('.')
    test.create_background()
    assert before != os.listdir('.')
