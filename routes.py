import os
import shutil
import uuid

from flask import Flask, render_template, request

from editor import make_element

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':

        try:
            del context
        except NameError:
            pass

        author = request.form['author']
        quote = request.form['quote']
        size = (int(request.form['width']),int(request.form['height']))
        element = make_element(quote, author, size)
        destination = 'static'
        vid_id = str(uuid.uuid4())[:4]
        supported_codecs = [('libx264', '.mp4'),
                            ('libvpx','.webm'),
                            ('libtheora','.ogv')]
        context = []
        for codec in supported_codecs:
            filename = author + vid_id + codec[1]
            element.write_videofile(filename, codec=codec[0])
            shutil.move(filename, destination)
            context.append({'filename' : filename,
                            'suffix': codec[1]})
        return render_template('video.html', videos=context)
    else:
        return render_template('index.html')

if __name__=='__main__':
    app.run(debug = True)
