#-*- coding:utf-8 -*-
from flask import Flask, render_template
from urllib import urlopen
from bs4 import BeautifulSoup
import os
import codecs
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('self.html')

@app.route('/idea')
def idea():
    """Return a friendly HTTP greeting."""
    return render_template('idea.html')

@app.route('/photography')
def photography():
    """Return a friendly HTTP greeting."""
    return render_template('photo.html')

@app.route('/webtoon')
def webtoon():
	data = urlopen('http://comics.nate.com/webtoon/detail.php?btno=64923')
	soup = BeautifulSoup(data)
	list = []
	find_div = soup.find('div', {"class" : "toonView"})
	for img in find_div.findAll('img'):
		list.append(img['src'])
	print list
	return render_template('webtoon.html', list=list)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
