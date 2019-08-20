"""Main module to do all the stuff."""
from time import time, sleep
import re
from urllib.request import urlopen, urlretrieve
from getpass import getuser
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import locators


BROWSER = webdriver.Chrome()
BROWSER.implicitly_wait(10)
ACTION = ActionChains(BROWSER)


def interface(url, url_type='pic'):
    """Starts execution"""
    BROWSER.get(url)
    pics = parse_album(url) if url_type == 'album' else url
    for img in pics:
        get_img(img)
    BROWSER.close()


def get_source(url):
    """Get common url of pic and retrieve the original source image"""
    BROWSER.get(url)
    elem = BROWSER.find_element(*locators.FLICK_PIC)
    elem.click()
    ACTION.move_to_element(elem).perform()
    pic = BROWSER.find_element(*locators.FLICK_PIC_ZOOM).get_attribute('src')
    return pic


def scroll_to_end():
    """Scrolls dynamic content to the end of page"""
    pause = 1
    last_height = BROWSER.execute_script("return document.body.scrollHeight")
    while True:
        BROWSER.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(pause)
        new_height = BROWSER.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def parse_album(album_url):
    """Find all images in album and return their urls"""
    BROWSER.get(album_url)
    scroll_to_end()
    lst = []
    pics = BROWSER.find_elements(*locators.FLICK_ALBUM_PIC_SELECT)
    for elem in pics:
        lst.append(elem.get_attribute('href'))
    cnt = BROWSER.find_element(*locators.FLICK_ALBUM_PICS_COUNT).text
    assert len(lst) == int(re.search(r'\d+', cnt).group())
    return lst


def get_img(url, loc='C:/Users/'+getuser()+'/Desktop/'):
    """Download the image to selected location"""
    img = get_source(url)
    response = urlopen(img)
    assert response.code == 200, "Can't open image. Maybe link is broken"
    pic_name = str(int(time()))+'.png'
    urlretrieve(img, loc+pic_name)
    print(f'Saved {img} to {loc} as {pic_name}')


def main():
    """Main function gets user url and starts the program"""
    link = 'https://www.flickr.com/photos/kristianbell/albums/72157625584774754'
    interface(link, 'album')


main()
