""" 
Iegūt ziņas, izmantojot RSS plūsmu no google.lv.

"""
import feedparser

# URL uz RSS plūsmu

rss_url="https://news.google.com/home?hl=en-LV&gl=LV&ceid=LV:en"

# iegūst Rss plūsmas datus
kkk=feedparser.parse(rss_url)

# parāda un noformē

for entry in kkk.entries:
    print("Virsraksts: ", entry.title)
    print("Saite: ", entry.link)
    print("\n")