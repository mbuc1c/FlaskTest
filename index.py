from flask import Flask, make_response, redirect, request, render_template, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from webbrowser import open_new_tab


app = Flask(__name__)
app.config['SECRET_KEY'] = '7a72eaa4821026fa49844c6cb02f30f104bb6c655bf9d1c1'

messages = [{'title': 'Message One', 'content': 'Message One Content'},
            {'title': 'Message Two', 'content': 'Message Two Content'}]

class LoginForm(FlaskForm):
    username = StringField('Username: ')
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return render_template('index.html', messages=messages)
    
@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))
    return render_template('create.html')


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