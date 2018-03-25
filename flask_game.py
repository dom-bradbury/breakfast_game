from flask import Flask, render_template, request, session, redirect, url_for
from multiprocessing import Process, Queue
from time import sleep
import breakfast_game.breakfast_game as bg

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Your Secret Key'
app.template_folder = 'breakfast_game/templates'

i = Queue()
o = Queue()
w = Queue()
s = True


@app.route("/")
def main():
    print('executing main')
    session['output'] = ''
    #session['refresh'] = '<meta http-equiv="refresh" content="1" >'
    print('Hullabalooza')
    return redirect((url_for('read_input')))


def refresh():
    if w.empty() is False and o.empty() is True:
        return False
    else:
        return True

@app.route('/game', methods=['GET', 'POST'])
def read_input():
    print('executing read_input')

    print(o.empty())
    print(w.empty())

    if o.empty() is False:
        html_output = '<p>' + o.get() + '</p>' + session['output']
        session['output'] = html_output
        if refresh():
            session['refresh'] = '<meta http-equiv="refresh" content="1" >'
        else:
            session['refresh'] = ''
        return render_template('breakfast_game.html', output=html_output, refresh=session['refresh'])
    #session['refresh'] = ''
    # read the posted values from the UI
    input = request.form['userinput']
    i.put(input)
    html_output = '<p>' + input + '</p>' + session['output']
    session['output'] = html_output

    if refresh():
        session['refresh'] = '<meta http-equiv="refresh" content="1" >'
    else:
        session['refresh'] = ''

    return render_template('breakfast_game.html', output=html_output, refresh=session['refresh'])

if __name__ == "__main__":

    game_process = Process(target=bg.main, args=(i, o, w,))

    game_process.start()

    app.run()

    print('Will I ever be executed?')