from flask import Flask, render_template, request, session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Your Secret Key'


@app.route("/")
def main():
    print('executing main')
    session['output'] = ''
    return render_template('test.html')


@app.route('/', methods=['POST'])
def read_input():
    print('executing read_input')
    # read the posted values from the UI
    input = request.form['userinput']
    output = '<p>' + input + '</p>' + session.get('output')
    session['output'] = output

    with open('templates/test.html') as f:
        print(f.read().format(output))

    return render_template('test.html', output=output)

if __name__ == "__main__":
    app.run(debug=True)