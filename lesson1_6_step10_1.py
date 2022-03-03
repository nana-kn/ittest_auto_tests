from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.XPATH, '//*[text()="First name*"]/following-sibling::input')
    last_name = browser.find_element(By.XPATH, '//*[text()="Last '
                                               'name*"]/following-sibling::input')
    e_mail = browser.find_element(By.XPATH, '//*[text('
                                            ')="Email*"]/following-sibling::input')
    # phone = browser.find_element(By.XPATH, '[text('
    #                                    ')="Phone:"]/following-sibling::input')
    # address = browser.find_element(By.XPATH,
    #     '*[text()="Address:"]/following-sibling::input')
    fields = [first_name, last_name, e_mail]

    for field in fields:
        field.send_keys("...")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_elements(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()