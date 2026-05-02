import logging
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.positive
def test_valid_Login():
    driver = webdriver.Chrome()                                     # Initillizing the browser
    driver.get("https://www.guvi.in/")                              # feed the URL and direct to this web site
    driver.maximize_window()                                        # Maximize the window to full screen
    driver.find_element(By.XPATH,"//button[@id='login-btn'][1]").click()            #find this element and click
    username = driver.find_element(By.XPATH, "//input[@id ='email']")               # initillizing the Username field to a variable
    username.send_keys("sriramsmrg@gmail.com")                                      # enter this value in the user name field
    password = driver.find_element(By.XPATH, "//input[@id = 'password']")           # initillizing the password field to a variable
    password.send_keys("Studio@23")                                                 # enter this password in the password field
    driver.find_element(By.XPATH, "//input[@ id = 'logged-in']").click()            # emabling the keep me logged in checkbox
    login_button = (driver.find_element(By.XPATH, "//a[@id = 'login-btn']"))        # click on the login button
    login_button.click()
    time.sleep(10)                                                                  # wait for 10 sec so that the user will be re-direct to the home page as a loggedin user
    driver.quit()

@pytest.mark.negative
def test_invalid_Login():
    driver = webdriver.Chrome()                                     # Initillizing the browser
    driver.get("https://www.guvi.in/")                              # feed the URL and direct to this web site
    driver.maximize_window()                                        # Maximize the window to full screen
    driver.find_element(By.XPATH,"//button[@id='login-btn'][1]").click()            #find this element and click
    username = driver.find_element(By.XPATH, "//input[@id ='email']")               # initillizing the Username field to a variable
    username.send_keys("QA@gmail.com")                                              # enter this value in the user name field
    password = driver.find_element(By.XPATH, "//input[@id = 'password']")           # initillizing the password field to a variable
    password.send_keys("Studio@23")                                                 # enter this password in the password field
    login_button = (driver.find_element(By.XPATH, "//a[@id = 'login-btn']"))        # click on the login button
    login_button.click()
    assert driver.find_element(By.XPATH, "//div[@id = 'emailgroup']//div").is_displayed()          # Validating whether the error message is displaying
    logging.info("In Valid login is performed")
    driver.quit()


@pytest.mark.negative
def test_empty_field_Login():
    driver = webdriver.Chrome()                         # Initillizing the browser
    driver.get("https://www.guvi.in/")                  # feed the URL and direct to this web site
    driver.maximize_window()                            # Maximize the window to full screen
    driver.find_element(By.XPATH, "//button[@id='login-btn'][1]").click()               # find this element and click
    time.sleep(3)
    login_button = (driver.find_element(By.XPATH, "//a[@id = 'login-btn']"))  # click on the login button
    login_button.click()
    assert driver.find_element(By.XPATH,"//div[@id= 'passwordGroup']//div").is_displayed()  # Validating whether the error message is displaying for empty field
    logging.info("In Empty field login is performed")
    driver.quit()

@pytest.mark.positive
def test_URL_validation():
    driver = webdriver.Chrome()                         # Initillizing the browser
    driver.get("https://www.guvi.in/")                  # feed the URL and direct to this web site
    driver.maximize_window()                            # Maximize the window to full screen
    driver.find_element(By.XPATH, "//button[@id='login-btn'][1]").click()          # find this element and click
    time.sleep(5)
    login_page_URL = driver.current_url                                            # Storing the login page url in a variable
    assert login_page_URL == "https://www.guvi.in/sign-in/?sourceUri=http%3A%2F%2Fwww.guvi.in%2F"           #Camparing the url with the variable
    driver.quit()

@pytest.mark.validated
def test_input_fields_validation():
    driver = webdriver.Chrome()                         # Initillizing the browser
    driver.get("https://www.guvi.in/")                  # feed the URL and direct to this web site
    driver.maximize_window()                            # Maximize the window to full screen
    driver.find_element(By.XPATH, "//button[@id='login-btn'][1]").click()          # find this element and click
    time.sleep(5)
    email_address = driver.find_element(By.XPATH, "//input[@id='email']")    #setting a variable for email field
    password = driver.find_element(By.XPATH, "//input[@id='password']")      #setting a variable for password field
    email_address.is_displayed() and email_address.is_enabled()              #Validating the email field
    password.is_displayed() and password.is_enabled()                        #Validating the password field
    logging.info("THE input fields are Visibled and emabled")                # printing the message in the report
    driver.quit()

@pytest.mark.validated
def test_submit_button_validation():
    driver = webdriver.Chrome()                         # Initillizing the browser
    driver.get("https://www.guvi.in/")                  # feed the URL and direct to this web site
    driver.maximize_window()                            # Maximize the window to full screen
    driver.find_element(By.XPATH, "//button[@id='login-btn'][1]").click()          # find this element and click
    time.sleep(5)
    login_button = (driver.find_element(By.XPATH, "//a[@id = 'login-btn']"))       # Setting a variable for log in button
    login_button.is_displayed()                                                    # validating the button
    login_button.is_enabled()                                                      # Validating the button
    logging.info("THE input fields are Visibled and emabled")                      # printing the  message in the report
    driver.quit()

@pytest.mark.positive
def test_Signup_validation():
    driver = webdriver.Chrome()                          # Initillizing the browser
    driver.get("https://www.guvi.in/")                   # feed the URL and direct to this web site
    driver.maximize_window()                             # Maximize the window to full screen
    driver.find_element(By.XPATH, "//button[@id='login-btn'][1]").click()    # find this element and click
    time.sleep(5)
    sign_in_button = (driver.find_element(By.XPATH, "//*[contains(text(),'Signup')]"))      # setting a variable for sign button
    sign_in_button.click()
    sign_in_page_URL = driver.current_url  # Storing the login page url in a variable       # validating the url
    assert sign_in_page_URL == "https://www.guvi.in/register/?sourceUri=http%3A%2F%2Fwww.guvi.in%2F"  # Camparing the url with the variable
    driver.quit()


// this is a sample line
