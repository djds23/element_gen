from element_gen.Twitter_Element import Twitter_Element

def test_twitter_element():
    test = Twitter_Element('dontusethiscode')
    test.blur_background()
    print test.blurred
    assert 0
