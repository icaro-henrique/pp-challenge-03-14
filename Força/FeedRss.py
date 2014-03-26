import feedparser
 
rss_url = "http://www.giantbomb.com/feeds/new_releases/"
feed = feedparser.parse(rss_url)
print (feed["channel"]["title"])

for item in feed["items"]:
    print(item["title"])
    print(item["link"])
    print(item["summary"])
    print ("\n")
