#-*- coding:utf-8 -*-
from flask import Flask, render_template
from urllib import urlopen
from bs4 import BeautifulSoup
import tweepy
import os
import codecs

auth = tweepy.OAuthHandler('Ymy7VTAZSx4tuY0skkYHHBGKn', 'wQafteJSPwf1egyrN7KJgLxZubbKCvzKUPSa5p2XmuGMypcx0j')
auth.set_access_token('186740931-1OAFTPIVjv9gRBv0pPBnoJ8ACPHKa6zvbIHWfsMT', 'Cw9PdgQJuTdAVAzbOINi8fQXcjOq68EVVL3Ak8OvN9oDF')
api = tweepy.API(auth)

results = api.search('손흥민', show_user=True)
print results
list = {}
i = 0
for result in results:
	list[result.user.screen_name] = result.text
	i += 1
print list
# list = []
# for result in results:
# 	list.append(result.user.screen_name + ' : ' + result.text)
# print list