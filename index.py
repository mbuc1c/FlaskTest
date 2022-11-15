from flask import Flask, make_response, redirect, request
from webbrowser import open_new_tab


app = Flask(__name__)

@app.route('/')
def index():
    ipAdresa = request.remote_addr
    return 'Unesi /user/svojeIme ;) ' + ipAdresa

@app.route('/user/<name>')
def helloUser(name):
    return f'<h1>Hello {name}!</h1>'

@app.route('/makeResponse')
def makeResponse():
    response = make_response('<h1>This document has a cookie</h1>')
    response.set_cookie('answer', '14')
    return response

@app.route('/redirect')
def redirectMe():
    return redirect('www.google.com')

@app.route('/bruh')
def bruh():
    return open_new_tab('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley')