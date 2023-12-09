from main import *


try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(by="id", value="input_value").get_attribute("textContent")

    y = calc(int(x_element))

    answer = browser.find_element(by="id", value="answer")
    answer.send_keys(y)

    browser.execute_script("window.scrollBy(0, 100);") # скрол страницы на 100 пикселей

    chekbox = browser.find_element(by="id", value="robotCheckbox")
    chekbox.click()

    radiob = browser.find_element(by="id", value="robotsRule")
    radiob.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(5)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()