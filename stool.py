#!/bin/env python2.7

import json, requests
pages='1'
feed='http://union.barstoolsports.com/v1/stories?page='+pages
session=requests.session()
r=session.get(feed, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'})
'''
for featStory in r.json()['featured']['stories']:
    print featStory['author']['name'] + ' :: '+ featStory['title'] + '\n' + featStory['url']
    print
'''
counter=0
numOfStories=len(r.json()['stories'])
for story in r.json()['stories']:
    print str(counter+1)+') '+story['author']['name'] + ' :: '+ story['title'] + '\n' + story['url']
    counter+=1
    print
