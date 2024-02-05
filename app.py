from flask import Flask

app = Flask(__name__)

print('hello world!! file running')

@app.route('/')
def helloWorld():
    return"<h1>Hello, rams!</h1>"

@app.route('/aboutme')
def about_me():
    return"<h1>This is an anbout me page</h1>" 