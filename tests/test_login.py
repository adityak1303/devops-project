import test_setup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = test_setup.driver


def find_element_by_xpath(xpath):
    return lambda d: driver.find_element(by=By.XPATH, value=xpath)


def test_login():
    driver.get(test_setup.LOGIN_PAGE)
    title = driver.title
    assert title != ""
    WebDriverWait(driver, timeout=10).until(find_element_by_xpath(xpath="/html/body/nav/ul/li[1]/a"))
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div[2]/div/div/form/input[1]").send_keys("abcdef@gmail.com")
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div[2]/div/div/form/input[2]").send_keys("kiran")
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div[2]/div/div/form/input[4]").click()
    WebDriverWait(driver, timeout=10).until(find_element_by_xpath(xpath="/html/body/nav/ul/li[1]/a"))
    login_string = driver.find_element(by=By.XPATH, value="/html/body/nav/ul/li[1]/a").text
    print(login_string)
    assert login_string.endswith("Kiran") == True

    # driver.quit()



def test_locate():
    driver.find_element(by=By.XPATH, value="/html/body/nav/ul/li[2]/a").click()
    WebDriverWait(driver, timeout=10).until(
        find_element_by_xpath(xpath="/html/body/div[2]/div[2]/div/div/form/input[1]"))
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div/form/input[1]").send_keys(
        "12.929614570407022")
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div/form/input[2]").send_keys(
        "77.60308772503659")
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div/form/div/button").click()

    WebDriverWait(driver, timeout=50).until(
        find_element_by_xpath(xpath="/html/body/div[2]/div/div/div/table/tbody/tr[1]/td"))
    latitude = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/table/tbody/tr[1]/td").text
    assert latitude != "" or latitude is not None

def test_logout():
    # driver.find_element(by=By.XPATH)
    driver.quit()