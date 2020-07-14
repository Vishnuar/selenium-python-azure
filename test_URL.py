import pytest
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

class TestMyURL():

	def test_url_load(self, driver, envurl):
		try:
			driver.get(reporturl)
			print(driver.current_url)
			assert 'testodev' in driver.current_url, "URL Loading failed"
		except:
			assert False, "Exception in URL loading"