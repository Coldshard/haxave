from time import time
from urllib.request import urlopen, urlretrieve
from getpass import getuser


def get_img(url, loc='C:/Users/'+getuser()+'/Desktop/'):
    response = urlopen(url)
    assert response.code == 200
    urlretrieve(url, loc+str(int(time()))+'.png')


link = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'
get_img(link)
