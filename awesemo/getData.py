import win32clipboard
from selenium.webdriver.common.by import By
import pandas as pd
from scripts.main.getDriver import GetDriver

from scripts.main.waitForPage import waitForPage


def getData(driver:GetDriver):
    copyButton ="#tablist1-panel2 a.dt-button.buttons-copy.buttons-html5.DTTT_button.DTTT_button_copy"
    driver.waitForElement(copyButton)
    driver.selectOne(copyButton).click()
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    df = pd.DataFrame([row.split("\t") for row in data.split("\n")])
    df.columns = df.iloc[0]
    df = df[1:]

    return df
    