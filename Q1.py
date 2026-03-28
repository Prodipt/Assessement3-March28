from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)

driver.implicitly_wait(30)

# Launched the browser and opened it successfully!
driver.get("https://www.shoppersstack.com/")

#MMaximize the window here
driver.maximize_window()
print(" -> Maximized the Website \n")

sleep(2)
actions = ActionChains(driver)
wait = WebDriverWait(driver, 20)

sleep(5)

# Located that Apple Product here inside ele1 variable
ele1 = driver.find_element(By.XPATH, "(//div[@class ='featuredProducts_cardContainer__r2Ou6'])//child::div")


# Scroll to ele1 element
actions.pause(2).scroll_to_element(ele1).perform()
print(" -> Scrolled to Apple Product \n")

ele1.click()

# Located pincode input area
pincode = driver.find_element(By.ID, "Check Delivery")
print(" -> Entered PinCode \n")

# Used send_keys to put the data
pincode.send_keys("826001")

# Wait to make sure the check button is clickable
checkBtn = wait.until(EC.element_to_be_clickable((By.ID, "Check")))

# Clicked on check button to check that pincode
checkBtn.click()
print(" -> Clicked on Check Button")

sleep(3)
print("Website Closed!!!")
driver.close()
