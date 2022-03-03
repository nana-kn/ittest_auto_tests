from selenium import webdriver
import math
import time

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
        
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    checkbox1 = browser.find_element_by_id("robotCheckbox") 
    checkbox1.click()
    browser.execute_script("window.scrollBy(0, 100);")
    rbutton1 = browser.find_element_by_id('robotsRule')
    rbutton1.click()
    button = browser.find_element_by_tag_name("button")
    button.click()
    
finally:
    time.sleep(15)
    browser.quit()   
    