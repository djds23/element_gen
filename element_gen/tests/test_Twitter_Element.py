from element_gen.Twitter_Element import Twitter_Element

def test_twitter_element():
    test = Twitter_Element('deanrex')
    test.merge_tweets()
    print test.filename
    assert 0
