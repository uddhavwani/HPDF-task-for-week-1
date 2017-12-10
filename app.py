from flask import Flask, render_template, make_response, request, jsonify, abort
import requests
import json

app = Flask(__name__) #object that is instance of the flask framework.

#Task_1
@app.route('/')
def index():
    return "<h1>Hello​ ​World​ ​-​ ​Uddhav</h1>"

#Task_2
@app.route('/authors')
def authors():
	data=[]
	authors=requests.get('https://jsonplaceholder.typicode.com/users')
	posts=requests.get('https://jsonplaceholder.typicode.com/posts')
	data_authors=json.loads(authors.text)
	data_posts=json.loads(posts.text)
	for i in data_authors:
		count=0
		for j in data_posts:
			if(j['userId']==i['id']):
				count=count+1
		data.append({"name":i['name'],"posts":count})
	return render_template("authors.html", data_authors=data)    #data send in html page 

#Task_3
@app.route('/setcookie')
def setcookie():
	if request.cookies.get('name') is None:
		resp = make_response('Cookie is set')
		resp.set_cookie('name','Uddhav')
		resp.set_cookie('age','21')
		return resp
	resp = make_response('Cookie is Already set')
	return resp

#Task_4
@app.route('/getcookies')
def getcookies():
	if request.cookies.get('name') is None:
		return 'cookies are not set'
	name = request.cookies.get('name')
	age = request.cookies.get('age')
	return 'name cookie value is '+name+' &age cookie value is '+age

#Task_5
@app.route('/robots.txt')
def deny_request():
	abort(403)				#if abort not execute, then another way to do this is return the error in html.
	return render_template('error.html')

#Task_6
@app.route('/html')
def render_htmlpage():
	return render_template('home.html')

#Task_7
@app.route('/input', methods=['GET','POST'])
def input():
	if request.method == 'POST':
		input=request.form['input']
		return render_template('input.html',input=input)
	return render_template('input.html')

if __name__ == "__main__":
    app.run(debug=True)
