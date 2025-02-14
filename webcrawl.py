from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run without opening a window (optional)
driver = webdriver.Chrome(options=options)

# Open LinkedIn login page
driver.get("https://www.linkedin.com/login")

# Enter username and password
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("")
password.send_keys("")

# Click the login button
password.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(5)

# Now go to job listings page
driver.get("https://www.linkedin.com/jobs/collections/recommended/")
print(driver.page_source)  
time.sleep(5)

# Extract jobs
#LinkedIn dynamically changes class names, CSS_SELECTOR is not always reliable.
jobs = driver.find_elements(By.CSS_SELECTOR, "div.job-card-container")

# Debugging: Print how many jobs were found
print(f"Found {len(jobs)} job listings.")

# Extract Job Titles and Links
for job in jobs[:5]:  
    try:
        title = job.find_element(By.CSS_SELECTOR, "a.job-card-container__link").text
        link = job.find_element(By.CSS_SELECTOR, "a.job-card-container__link").get_attribute("href")

        print(f"Job Title: {title}")
        print(f"Apply Here: {link}\n")
    except Exception as e:
        print(f"⚠ Error extracting job details: {e}")

# Close the browser
driver.quit()