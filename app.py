from flask import Flask, render_template, request, session, redirect, url_for
from multiprocessing import Process, Queue
import breakfast_game.breakfast_game as bg
import os

i = Queue()
o = Queue()
w = Queue()
s = True

game_process = Process(target=bg.main, args=(i, o, w,))


class MyMiddleware(object):

    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app
        self.on = False

    def __call__(self, *args, **kwargs):
        print('Executing MyMiddleware call')
        if not self.on:
            game_process.start()
            self.on = True
        return self.wsgi_app(*args, **kwargs)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Your Secret Key'
app.template_folder = 'breakfast_game/templates'
app.wsgi_app = MyMiddleware(app.wsgi_app)


def refresh():
    if w.empty() is False and o.empty() is True:
        return False
    else:
        return True


@app.route('/', methods=['GET', 'POST'])
def read_input():
    print('executing read_input')

    if session.get('output') is None:
        session['output'] = []

    if o.empty() is False:
        output = o.get()
        session['output'].append(output)
        session['output'] = session['output'][-15:]
        html_output = '<p' + '</p><p>'.join(session['output']) + '</p>'
        if refresh():
            session['refresh'] = '<meta http-equiv="refresh" content="1" >'
        else:
            session['refresh'] = ''
        return render_template('breakfast_game.html', output=html_output, refresh=session['refresh'])

    # read the posted values from the UI
    input = request.form['userinput']
    i.put(input)
    session['output'].append(input)
    session['output'] = session['output'][-15:]
    html_output = '<p' + '</p><p>'.join(session['output']) + '</p>'
    session['refresh'] = '<meta http-equiv="refresh" content="1" >'

    return render_template('breakfast_game.html', output=html_output, refresh=session['refresh'])


if __name__ == "__main__":
    app.run(debug=True)

    print('Will I ever be executed?')