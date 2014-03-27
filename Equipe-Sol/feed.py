import feedparser

python_wiki_rss_url = "http://g1.globo.com/dynamo/rss2.xml"

feed = feedparser.parse( python_wiki_rss_url )
aux = 0
master = feed['channel']
print(master['title'])
print(master['link'])

for post in feed.entries:
	if(aux < 3):
		print("===========\nTitulo:",post.title+"\nLink:"+post.link+"\nDescrição:"+post.description)
	aux = aux +1
	
