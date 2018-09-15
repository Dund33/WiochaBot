import bs4
import requests


def getImg():

    data = requests.get('http://www.wiocha.pl/losuj').text
    soup = bs4.BeautifulSoup(data, 'html.parser')
    img_tag = soup.find('img', {'class': 'imageitself'})

    while img_tag is None:
        data = requests.get('http://www.wiocha.pl/losuj').text
        soup = bs4.BeautifulSoup(data,'html.parser')
        img_tag = soup.find('img',{'class':'imageitself'})

    url = img_tag['src']
    name = url[-36::]
    img = requests.get(url).content
    return img, name


for i in range(0,10):
    img, name = getImg()
    f = open(name, 'w')
    f.write(img)
    f.close()
