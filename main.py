#-*- coding:utf-8 -*-
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from urllib import urlopen
from bs4 import BeautifulSoup
import tweepy
import os
import codecs
import json
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

@app.route('/twitter')
def twitter():
	return render_template('twitter.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
	if request.method == "POST":
		auth = tweepy.OAuthHandler('Ymy7VTAZSx4tuY0skkYHHBGKn', 'wQafteJSPwf1egyrN7KJgLxZubbKCvzKUPSa5p2XmuGMypcx0j')
		auth.set_access_token('186740931-1OAFTPIVjv9gRBv0pPBnoJ8ACPHKa6zvbIHWfsMT', 'Cw9PdgQJuTdAVAzbOINi8fQXcjOq68EVVL3Ak8OvN9oDF')
		api = tweepy.API(auth)
		response = []
		results = api.search(request.form['keyword'], show_user=True)
		for result in results:
			response.append({ 'id': result.user.screen_name, 'text': result.text})
		return json.dumps(response)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
