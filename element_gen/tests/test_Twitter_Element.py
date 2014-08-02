from element_gen.TwitterElement import TwitterElement

def test_twitter_element():
    test = TwitterElement('RuthBourdain')
    test.merge_tweets()
    print test.filename
    assert 0
