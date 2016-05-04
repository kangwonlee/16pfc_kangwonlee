# -*-coding:utf8
import urllib
import bs4
import urlparse

url = "http://photo.naver.com/camera/"

# website 에서 정보를 가져 옴
website = urllib.urlopen(url)
text = website.read()
website.close()

# 가져 온 정보를 해석함
soup = bs4.BeautifulSoup(text, 'lxml')

# 해석한 정보에서 img 포함된 내용을 추출함
imgs = soup.find_all('img')

# 추출한 내용을 하나씩 살펴 봄
for image_info in imgs:
    image_url = image_info.get('src')
    print('image_url = %s' % image_url)
    url_parse_result = urlparse.urlparse(image_url)
    print('url_parse_result = ' + str(url_parse_result))
    parsed_path = url_parse_result.path
    print('parsed_path = ' + str(parsed_path))
    parsed_path_split = parsed_path.split('/')
    print('parsed_path_split = ' + str(parsed_path_split))
    filename = parsed_path_split[-1]
    urllib.urlretrieve(image_url, filename)
