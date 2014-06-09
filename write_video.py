from moviepy.editor import *

def merge(filename, text, duration):
    background = ImageClip(filename)
    text = TextClip(text, fontsize 70, color='black')
    video = CompositeVideoClip([
            background.set_duration(duration),
            text.set_pos('center').set_duration(duration)])
    video.to_videofile(filename+'.mp4',fps=60)
