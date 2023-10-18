from selenium.webdriver.common.by import By

from scripts.main.getDriver import GetDriver
from .config import EMAIL, PASSWORD, MAINPAGE
from ..main.waitForPage import waitForPage


def login(driver: GetDriver):
    def gotoLoginPage():
        driver.get(MAINPAGE)
        waitForPage(driver, '//a[text()="Login/Register"]', By.XPATH)
        driver.find_element(By.XPATH, '//a[text()="Login/Register"]').click()
        waitForPage(driver, "input#user_login")

    gotoLoginPage()
    for i in range(2):
        try:

            driver.selectOne("input#user_login").send_keys(EMAIL)
            driver.selectOne("input#user_pass").send_keys(PASSWORD)
            driver.selectOne("input#user_pass").send_keys(driver.keys.ENTER)

            return True
        except:
            gotoLoginPage()

    return False
