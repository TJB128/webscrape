from scripts.main.getDriver import GetDriver
from .login import login
from .getData import getData
import time
from scripts.main.waitForPage import waitForPage
def awesemo(driver:GetDriver, saveData, sheetName):
    loggedIn = login(driver)
    waitForPage(driver,"#tablist1-tab2")
    if loggedIn:

        driver.selectOne("#tablist1-tab2").click()
        try:

            df = getData(driver)
        except:
            print("could not get data")
            df=None
        saveData(sheetName, df)
        print("Extracted",sheetName,"\n")
    else:
        df = None

    
