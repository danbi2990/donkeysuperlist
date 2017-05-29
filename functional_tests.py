from selenium import webdriver
from autotest_lib.client.common_lib.cros import chromedriver

# browser = webdriver.Chrome()
# browser.get("http://localhost:8000")
with chromedriver.chromedriver() as chromedriver_instance:
    driver = chromedriver_instance.driver
    driver.get("http://localhost:8000")
    assert 'Django' in driver.title


