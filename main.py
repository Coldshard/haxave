"""Main module to do all the stuff."""
from time import time
from urllib.request import urlopen, urlretrieve
from getpass import getuser
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import locators


BROWSER = webdriver.Chrome()
BROWSER.implicitly_wait(10)
ACTION = ActionChains(BROWSER)


def interface(url):
    """Get common url of pic and retrieve the original source image"""
    BROWSER.get(url)
    elem = BROWSER.find_element(*locators.FLICK_PIC)
    elem.click()
    ACTION.move_to_element(elem).perform()
    pic = BROWSER.find_element(*locators.FLICK_PIC_ZOOM).get_attribute('src')
    get_img(pic)
    BROWSER.close()


def get_img(url, loc='C:/Users/'+getuser()+'/Desktop/'):
    """Download the image to selected location"""
    response = urlopen(url)
    assert response.code == 200, "Can't open image. Maybe link is broken"
    urlretrieve(url, loc+str(int(time()))+'.png')


def main():
    """Main function gets user url and starts the program"""
    link = 'https://www.flickr.com/photos/kristianbell/48016130083/in/album-72157625507310459/'
    interface(link)


main()
