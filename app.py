# import psycopg2
from flask import Flask

app = Flask(__name__)

# conn = psycopg2.connect("dbname=loon_db user=nickhernandez")
# cur = conn.cursor()
# cur.execute("SELECT * FROM loon_db")
# records = cur.fetchall()

@app.route('/')
def helloWorld():
    return"<h1>Hello, rams!</h1>"

@app.route('/aboutme')
def about_me():
    return"<h1>This is an anbout me page</h1>" 