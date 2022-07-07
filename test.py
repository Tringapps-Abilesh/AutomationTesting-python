from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Headless
chrome_options = Options()
chrome_options.add_argument("--headless")

# path for chromeDriver
driver = webdriver.Chrome(executable_path="/home/tringapps/Downloads/chromedriver", options=chrome_options)

driver.maximize_window()

driver.implicitly_wait(5)
driver.get("https://letcode.in/alert")

driver.find_element(By.ID, "accept").click()

alert = WebDriverWait(driver, 5).until(EC.alert_is_present())

alert_text = alert.text
print(alert_text)

alert.accept()
driver.quit()
