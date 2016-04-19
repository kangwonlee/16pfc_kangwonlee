import urllib
import bs4

url = "http://photo.naver.com/camera/"

website = urllib.urlopen(url)
text = website.read()
website.close()

# http://edoli.tistory.com/26
soup = bs4.BeautifulSoup(text, 'lxml')
imgs = soup.find_all('img')

print(imgs)
