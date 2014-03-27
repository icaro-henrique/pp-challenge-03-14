import feedparser as fp
import sys
import codecs


if sys.stdout.encoding != 'UTF-8':
    sys.stdout = codecs.getwriter('cp850')(sys.stdout.buffer, 'strict')
if sys.stderr.encoding != 'UTF-8':
    sys.stderr = codecs.getwriter('cp850')(sys.stderr.buffer, 'strict')

d = fp.parse('http://feeds.reuters.com/reuters/sportsNews')
print("Feed 1")
print(d.entries[0].title_detail)
print(d.entries[0].summary_detail)
print("Feed 2")
print(d.entries[1].title_detail)
print(d.entries[1].summary_detail)
print("Feed 3")
print(d.entries[2].title_detail)
print(d.entries[2].summary_detail)
