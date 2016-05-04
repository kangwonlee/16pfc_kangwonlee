import urllib
import bs4

url = "http://photo.naver.com/camera/"

website = urllib.urlopen(url)
text = website.read()
website.close()

soup = bs4.BeautifulSoup(text, 'lxml')
imgs = soup.find_all('img')

for image_info in imgs:
    print(image_info.get('src'))

# urllib.urlretrieve()
