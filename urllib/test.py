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

urllib.urlretrieve("http://static.naver.net/m/photopc/exphotoimg/img/logo_naver4.gif",
                   'test.gif')
