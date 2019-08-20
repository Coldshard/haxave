"""
This module contains selectors for Selenium
"""
from selenium.webdriver.common.by import By

FLICK_PIC = (By.CSS_SELECTOR, ".view.photo-notes-scrappy-view")
FLICK_PIC_ZOOM = (By.CSS_SELECTOR, ".zoom-large")
FLICK_ALBUM_PIC_SELECT = (By.CSS_SELECTOR, ".overlay")
FLICK_ALBUM_PICS_COUNT = (By.CSS_SELECTOR, ".photo-counts")
