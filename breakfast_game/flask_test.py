from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def main():
    print('Hello Dom')
    return render_template('test.html')

@app.route('/', methods=['POST'])
def read_input():
    # read the posted values from the UI
    input = request.form['userinput']
    print(input)
    return render_template('test.html')

if __name__ == "__main__":
    print('Hello Again')
    app.run()