from flask import Flask, render_template, request, session
from multiprocessing import Process, Queue
from time import sleep
import breakfast_game

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Your Secret Key'
app.template_folder = 'breakfast_game/templates'


@app.route("/")
def main():
    print('executing main')
    session['output'] = ''
    return render_template('breakfast_game.html')


@app.route('/', methods=['POST'])
def read_input():
    print('executing read_input')

    # read the posted values from the UI
    input = request.form['userinput']
    output = '<p>' + input + '</p>' + session.get('output')
    session['output'] = output

    return render_template('breakfast_game.html', output=output)

if __name__ == "__main__":
    app.run(debug=True)
    print('Will I ever be executed?')