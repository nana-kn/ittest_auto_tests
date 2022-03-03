from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input_name = browser.find_element_by_name("firstname")
    input_name.send_keys("Katerina")
    input_sername = browser.find_element_by_name("lastname")
    input_sername.send_keys("Sergeeva")
    input_email = browser.find_element_by_name("email")
    input_email.send_keys("K_Sergeeva@mail.ru")
    file = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    file.send_keys(file_path)
    button = browser.find_element_by_tag_name("button")
    button.click()
    
finally:
    time.sleep(15)
    browser.quit()
    