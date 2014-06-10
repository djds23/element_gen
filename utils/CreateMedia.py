import moviepy.editor

class CreateMedia(object):

    def __init__(self, filename, background, duration, text):
        self.text=text
        self.filename=filename
        self.duration=duration
        self.background=background

    def merge(self):
        background = moviepy.editor.ImageClip(self.filename)
        text = moviepy.editor.TextClip(self.text, fontsize=70, color='black')
        video = moviepy.editor.CompositeVideoClip([
                background.set_duration(self.duration),
                text.set_pos('center').set_duration(self.duration)])
        video.to_videofile(self.filename+'.mp4',fps=60)
