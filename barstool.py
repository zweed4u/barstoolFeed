import json, urllib, datetime
from BeautifulSoup import BeautifulStoneSoup
def HTMLEntitiesToUnicode(text):
    """Converts HTML entities to unicode.  For example '&amp;' becomes '&'."""
    text = unicode(BeautifulStoneSoup(text, convertEntities=BeautifulStoneSoup.ALL_ENTITIES))
    return text

#while 1 - check if first title matches, 
#if true, sleep for 5 else fetch 
#try catch for valid inputs - default to 35
print 'Enter how many stories you want to fetch: '
numStories = raw_input('')

jsonurl='http://api.barstoolsports.com/api/get_recent_posts/?page=1&count='+str(numStories)
response = urllib.urlopen(jsonurl)
data = json.loads(response.read())
#How many posts (matches payload)- len(data[u'posts'])
i=0
while i < len(data[u'posts']):
	timeOfPost=datetime.datetime.strptime( str(data[u'posts'][i][u'date'])[:-6],"%Y-%m-%d %H:%M:%S" )
	print '\n'+str(i+1)+'.) '+HTMLEntitiesToUnicode(str(data[u'posts'][i][u'title']))+' - '+str(timeOfPost.month)+'/'+str(timeOfPost.day)+'/'+str(timeOfPost.year)+' :: ' + str(timeOfPost.hour)+':'+str(timeOfPost.minute)+'.'+str(timeOfPost.second)+'\n'+str(data[u'posts'][i][u'url'])
	i+=1

print '\n'
