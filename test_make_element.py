from editor import make_element

def test_make_element():
    meg = make_element('this is a super long quote that I am going to say to dean for his project and he will just chill the funk out',
            'meg',
            (1280,720))
    meg.write_videofile('textoutput.mp4')
