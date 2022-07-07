import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument("--headless")options=chrome_options

driver = webdriver.Chrome(executable_path="/home/tringapps/Downloads/chromedriver")

driver.maximize_window()

driver.implicitly_wait(5)
username = "sanjay09@tringapps.com"
password = "1234567890"
driver.get("https://d1hapd67qimv5t.cloudfront.net/")
driver.find_element(By.ID, "standard-helperText").send_keys(username)
driver.find_element(By.ID, "standard-adornment-password").send_keys(password)
driver.find_element(By.XPATH, "//button[contains(@class,'MuiButtonBase-root MuiIconButton-root')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[contains(@class,'MuiButtonBase-root MuiIconButton-root')]").click()

driver.find_element(By.XPATH, "//button[text()='Login']").click()

print(driver.current_url)

driver.current_url == "https://d1hapd67qimv5t.cloudfront.net/userform"

driver.find_element(By.XPATH, "//input[@placeholder='Enter your Name']").send_keys("abi")

wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.ID, ":r4:"))).send_keys("0-10")
wait.until(EC.presence_of_element_located((By.ID, ":r4:"))).send_keys(Keys.ARROW_DOWN)
wait.until(EC.presence_of_element_located((By.ID, ":r4:"))).send_keys(Keys.RETURN)

wait.until(EC.presence_of_element_located((By.ID, ":r6:"))).send_keys("0-10")
wait.until(EC.presence_of_element_located((By.ID, ":r6:"))).send_keys(Keys.ARROW_DOWN)
wait.until(EC.presence_of_element_located((By.ID, ":r6:"))).send_keys(Keys.RETURN)

wait.until(EC.presence_of_element_located((By.ID, ":r8:"))).send_keys("0-10")
wait.until(EC.presence_of_element_located((By.ID, ":r8:"))).send_keys(Keys.ARROW_DOWN)
wait.until(EC.presence_of_element_located((By.ID, ":r8:"))).send_keys(Keys.RETURN)

wait.until(EC.presence_of_element_located((By.ID, ":ra:"))).send_keys("0-10")
wait.until(EC.presence_of_element_located((By.ID, ":ra:"))).send_keys(Keys.ARROW_DOWN)
wait.until(EC.presence_of_element_located((By.ID, ":ra:"))).send_keys(Keys.RETURN)

wait.until(EC.presence_of_element_located((By.ID, ":rc:"))).send_keys("0-10")
wait.until(EC.presence_of_element_located((By.ID, ":rc:"))).send_keys(Keys.ARROW_DOWN)
wait.until(EC.presence_of_element_located((By.ID, ":rc:"))).send_keys(Keys.RETURN)

wait.until(EC.presence_of_element_located((By.ID, ":re:"))).send_keys("2017")
wait.until(EC.presence_of_element_located((By.ID, ":re:"))).send_keys(Keys.ARROW_DOWN)
wait.until(EC.presence_of_element_located((By.ID, ":re:"))).send_keys(Keys.RETURN)

wait.until(EC.presence_of_element_located((By.ID, ":rg:"))).send_keys("7.0-7.9")
wait.until(EC.presence_of_element_located((By.ID, ":rg:"))).send_keys(Keys.ARROW_DOWN)
wait.until(EC.presence_of_element_located((By.ID, ":rg:"))).send_keys(Keys.RETURN)

wait.until(EC.presence_of_element_located((By.ID, ":ri:"))).send_keys("Erode")
wait.until(EC.presence_of_element_located((By.ID, ":ri:"))).send_keys(Keys.ARROW_DOWN)
wait.until(EC.presence_of_element_located((By.ID, ":ri:"))).send_keys(Keys.RETURN)

wait.until(EC.presence_of_element_located((By.ID, ":rk:"))).send_keys("computer")
wait.until(EC.presence_of_element_located((By.ID, ":rk:"))).send_keys(Keys.ARROW_DOWN)
wait.until(EC.presence_of_element_located((By.ID, ":rk:"))).send_keys(Keys.RETURN)

wait.until(EC.presence_of_element_located((By.ID, ":rm:"))).send_keys("government")
wait.until(EC.presence_of_element_located((By.ID, ":rm:"))).send_keys(Keys.ARROW_DOWN)
wait.until(EC.presence_of_element_located((By.ID, ":rm:"))).send_keys(Keys.RETURN)

driver.find_element(By.XPATH, "//input[@placeholder='Enter your Alternative Email Id']").send_keys("ab12@gmail.com")

driver.find_element(By.XPATH, "//input[@placeholder='Enter your Contact number']").send_keys("9876543210")

wait.until(EC.presence_of_element_located((By.NAME, "Choose prefered language"))).send_keys("python")
wait.until(EC.presence_of_element_located((By.NAME, "Choose prefered language"))).send_keys(Keys.ARROW_DOWN)
wait.until(EC.presence_of_element_located((By.NAME, "Choose prefered language"))).send_keys(Keys.RETURN)

# driver.find_element(By.XPATH, "//button[text()='Submit']").click()

#
# btn = driver.find_element(By.XPATH, "//button[text()='Start the test']")
# # btn.click()
#
# a = ActionChains(driver)
#
# m = driver.find_element(By.XPATH, "(//div[@class='avataricon']//span)[3]")
#
# a.move_to_element(m).perform()
#
# n = driver.find_element(By.XPATH, "//span[text()='Logout']")
#
# a.move_to_element(n).click().perform()
#
# driver.get("https://d1hapd67qimv5t.cloudfront.net/start")
#
# print(driver.current_url)