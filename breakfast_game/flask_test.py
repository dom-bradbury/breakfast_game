from flask import Flask, render_template, request, session, redirect, url_for
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Your Secret Key'


@app.route("/")
def main():
    print('executing main')
    session['output'] = ''
    return render_template('test.html')


@app.route('/', methods=['POST'])
def read_input():

    if

    print('executing read_input')
    # read the posted values from the UI
    input = request.form['userinput']
    output = '<p>' + input + '</p>' + session.get('output')
    session['output'] = output

    return redirect(url_for('foo'))


@app.route('/foo')
def foo():
    print('foor')
    _ = request.form['userinput']
    _ = '<p>' + '</p>' + session.get('output')
    return render_template('test.html')

if __name__ == "__main__":
    app.run(debug=True)