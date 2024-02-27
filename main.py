from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.get("https://www.google.com.br/?hl=pt-BR")