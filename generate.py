import feedparser
from datetime import datetime
import xml.etree.ElementTree as ET

BLOG_FEED_URL = "https://guantaod.blogspot.com/feeds/posts/default?alt=rss"

feed = feedparser.parse(BLOG_FEED_URL)
urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

for entry in feed.entries:
    url = ET.SubElement(urlset, "url")
    loc = ET.SubElement(url, "loc")
    loc.text = entry.link
    lastmod = ET.SubElement(url, "lastmod")
    lastmod.text = datetime(*entry.updated_parsed[:6]).strftime("%Y-%m-%d")

tree = ET.ElementTree(urlset)
tree.write("sitemap.xml", encoding="utf-8", xml_declaration=True)
