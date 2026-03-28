from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait

o = ChromeOptions()
o.add_experimental_option("detach", True)
o.add_argument("--disable-notifications")

driver = Chrome(options=o)

driver.implicitly_wait(20)

# Launched the browser and opened it successfully!
driver.get("https://www.myntra.com/")

actions = ActionChains(driver)
wait = WebDriverWait(driver, 30)

#MMaximize the window here
driver.maximize_window()
print("\n -> Maximized the Website \n")

# Locate the GENZ Menu
genz = driver.find_element(By.LINK_TEXT, "GENZ")
actions.pause(2).move_to_element(genz).perform()

# Clicked on the "Jackets Under ₹899"
driver.find_element(By.LINK_TEXT, "Jackets Under ₹899").click()
print(" -> Jackets Under ₹899 \n")


# Filtering the product Once
wait.until(visibility_of_element_located(( By.XPATH, "(//div[@class='common-checkboxIndicator'])[4]" ))).click()

sleep(3)
# Filtering the product Twice
actions.scroll_by_amount(0, 600).perform()
wait.until(visibility_of_element_located((By.XPATH, "(//div[@class='common-checkboxIndicator'])[20]"))).click()

print(" -> Filtering on the basis of Cloth and color \n")

sleep(3)
# Clicked on Sort By
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Sort by')]"))).click()

# Popularity Selected
wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Popularity')]"))).click()
print(" -> Sorted BY Popuplarity \n")


# Product Clicked using XPATH locator
wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='product-productMetaInfo'])[5]"))).click()
print(" -> Product picked \n")


# Switched the Driver to the new window
driver.switch_to.window(driver.window_handles[1])
print(" -> Driver Switched \n")



# Size selected using XPATH
wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class = 'size-buttons-tipAndBtnContainer'])[2]"))).click()
print(" -> Selected the Size of cloth \n")


# Product added on the cart by clicking on the "Add to Cart" button
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='ADD TO BAG']"))).click()
print(" -> Added to Cart \n")


sleep(7)
print("Website Closed!!!")
driver.close()
