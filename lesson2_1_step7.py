from selenium import webdriver
import time
import math 

link = "http://suninjuly.github.io/get_attribute.html"
 


 
try:
    
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    element = browser.find_element_by_tag_name("img")
    x_element = element.get_attribute("valuex")
    x = x_element
    print(x)
    y = calc(x)
    
    input2 = browser.find_element_by_id("answer")
    input2.send_keys(y)
    input3 = browser.find_element_by_id("robotCheckbox")
    input3.click()
    input4 = browser.find_element_by_id("robotsRule")
    input4.click()
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    

    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()