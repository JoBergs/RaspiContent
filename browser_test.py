from selenium import webdriver
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()

profile = webdriver.FirefoxProfile()
profile.native_events_enabled = False
driver = webdriver.Firefox(profile)

driver.get("http://www.duckduckgo.com")
print(driver.page_source.encode('utf-8'))
driver.quit()