import feedparser

python_wiki_rss_url = "http://www.giantbomb.com/feeds/new_releases/"
feed = feedparser.parse( python_wiki_rss_url )

print("\n" + feed[ "channel" ][ "title" ])
print("----------------------------------")

i = 0
for item in feed["items"]:
	print("\n" + item["title"])
	print("\n" + item["link"])
	print("\n" + item["summary"] + "\n" + "---------------------------------------------------------")
	i = i + 1
	if(i == 3):
		break