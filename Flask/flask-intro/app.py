# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps
import sqlite3

from pandas import Series, DataFrame
import pandas as pd

# create the application object
app = Flask(__name__) 

#config
app.secret_key = "random keygen"
app.database = "sample.db"

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('login'))

	return wrap

# use decorators to link(map) the function to a url
@app.route('/')
@login_required
def home():
	data = pd.read_csv("/Users/diongarman/Desktop/flask-intro/road_safety_data.csv")[:200]
	return render_template('index.html', data= data.to_html()) #render a template



@app.route('/welcome')
def welcome():
	return render_template("welcome.html") # render a template

@app.route('/secret')
@login_required
def secret():
	return render_template("breakfast_menu.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	error=None
	if request.method == 'POST':
		if request.form['username'] == 'admin' and request.form['password'] == 'admin':
			session['logged_in'] = True
			flash('You were just logged in')
			return redirect(url_for('home'))
		elif request.form['username'] == 'secret' and request.form['password'] == 'secret':
			session['logged_in'] = True
			flash('You were just logged in to a top secret page')
			return redirect(url_for('secret'))
			
		else:
			error = 'Invalid credentials bro!'
	return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None) #This pops the value out of the session abject and replace with 'None'.
	flash('You were just logged out')
	return redirect(url_for('welcome'))




# start the server with the 'run()' method
if __name__=="__main__":
	app.run(debug=True)