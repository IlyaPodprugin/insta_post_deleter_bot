import time
import config

from seleniumwire import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def click(xpath):
    try:
        elem = driver.find_element(by=By.XPATH, value=xpath)
    except NoSuchElementException:
        return False
    ActionChains(driver).move_to_element(elem).click().perform()
    return True


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.instagram.com/")

config.nickname = input("Авторизуйтесь, затем введите ваш ник и нажмите enter: ")
config.posts = int(input("Сколько постов вы хотите удалить?: "))

driver.get(f"https://www.instagram.com/{config.nickname}/")
time.sleep(1.5)
for post in range(config.posts):
    start_time = time.time()
    if post == 21:
        driver.get(f"https://www.instagram.com/{config.nickname}/")
        time.sleep(1.5)
    click("/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]")
    time.sleep(config.sleep_time)
    click("/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[1]/div/div/button")
    time.sleep(config.sleep_time)
    click("/html/body/div[7]/div/div/div/div/button[1]")
    time.sleep(config.sleep_time)
    click("/html/body/div[7]/div/div/div/div[2]/button[1]")
    time.sleep(config.sleep_time)
    print(time.time() - start_time)
print("Посты успешно удалены")
time.sleep(999)
