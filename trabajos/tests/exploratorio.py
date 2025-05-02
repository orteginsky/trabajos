from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from ..occ.exploratorio import exploratorio

driver = webdriver.Chrome()

exploratorio(driver)