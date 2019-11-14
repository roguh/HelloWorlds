from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Use Firefox to go to the given website
driver = webdriver.Firefox()
driver.get("http://www.python.org")

# Make sure the page loaded correctly
assert "Python" in driver.title

# Process the page
elem = driver.find_element_by_name("q")
elem.clear()

# Send input to the browser
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

# Check the website from the browser's perspective
assert "No results found." not in driver.page_source
driver.close()

print("Automation completed")
