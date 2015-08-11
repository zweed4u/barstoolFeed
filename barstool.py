import json, urllib
from BeautifulSoup import BeautifulStoneSoup
def HTMLEntitiesToUnicode(text):
    """Converts HTML entities to unicode.  For example '&amp;' becomes '&'."""
    text = unicode(BeautifulStoneSoup(text, convertEntities=BeautifulStoneSoup.ALL_ENTITIES))
    return text

#while 1 - check if first title matches, 
#if true, sleep for 5 else fetch 
#implement prompt for page numbers
jsonurl='http://api.barstoolsports.com/api/get_recent_posts/?page=1&count=35'
response = urllib.urlopen(jsonurl)
data = json.loads(response.read())
#How many posts (matches payload)- len(data[u'posts'])
i=0
while i < len(data[u'posts']):
	#parse string for '&#(.+?); and conver html entity to text
	#unescape needed?
	print '\n'+str(i+1)+'.) '+HTMLEntitiesToUnicode(str(data[u'posts'][i][u'title']))+'\n'+str(data[u'posts'][i][u'url'])
	i+=1


