import feedparser


rss = "http://www.giantbomb.com/feeds/new_releases/"

feed = feedparser.parse(rss)

for x in range(1, len(feed["entries"])):
    pass
    print(feed.entries[x].title)
    print(feed.entries[x].link)
    print(feed.entries[x].description)
