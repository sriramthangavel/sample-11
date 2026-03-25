import time

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_Login():

    driver = webdriver.Chrome()
    driver.get("https://www.guvi.in/")
    driver.maximize_window()
    driver.find_element(By.XPATH,"//button[text()='Login'][1]").click()
    login_page_url = driver.current_url()
    assert login_page_url == "https://www.guvi.in/sign-in/?sourceUri=http%3A%2F%2Fwww.guvi.in%2F"

    username = driver.find_element(By.XPATH, "//input[@id ='email']")
    username.send_keys("sriramsmrg@gmail.com")
    password = driver.find_element(By.XPATH, "//input[@id = 'password']")
    password.send_keys("Studio@23")
    login_button = driver.find_element(By.XPATH, "//a[@id = 'login-btn']").click()
    time.sleep(5)
    driver.quit()
