import importlib

from selenium import webdriver
from easy_selenium import EasySelenium

chrome_driver = webdriver.Chrome()
driver = chrome_driver
es = EasySelenium(driver)

# Loads the provider
module = importlib.import_module('providers.br.santa_catarina')
provider = module.Provider(es)


provider.login()
provider.request_registration('Florianópolis', 'Av. Me. Benvenuta, 1248 - Trindade, Florianópolis - SC, 88036-500')