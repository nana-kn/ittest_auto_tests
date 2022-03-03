from selenium import webdriver
import time
import math 

link = "http://suninjuly.github.io/math.html"
 


 
try:
    
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    print(x_element.text)
    x = x_element.text
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
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()