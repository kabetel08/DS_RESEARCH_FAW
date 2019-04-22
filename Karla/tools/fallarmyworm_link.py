from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def loadElement(driver, locator):
	return WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, locator)))


def fallArmyWormCsvLink():
	driver = webdriver.Chrome()
	driver.get('http://www.fao.org/fall-armyworm/en/')

	# wait for powerbi to load
	loadElement(driver, '//*[contains(@src, "app.powerbi.com")]').click

	# change focus to iframe
	driver.switch_to.frame(loadElement(driver,'//*[contains(@src, "app.powerbi.com")]'))

	# get a reference to link element
	csvLink = loadElement(driver,'//*[text()="Download Comma Delimited File"]')

	# get link from attribute
	link = csvLink.get_attribute("href")
	driver.quit()
	
	return link
