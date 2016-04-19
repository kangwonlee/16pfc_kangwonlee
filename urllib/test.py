import urllib
import bs4

url = "http://photo.naver.com/camera/"

website = urllib.urlopen(url)
text = website.read()
website.close()

print(text)
