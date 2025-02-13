# LOCATORS
from selenium.webdriver.common.by import By


class LoginPage():
    field_user_email_name = "email"
    field_user_password_name = "password"
    button_signin_xpath = "//button[@type='submit']"

    def __init__(self,driver):
        self.driver = driver

    def set_user_email(self, email):
        self.driver.find_element(By.NAME, self.field_user_email_name).send_keys(email)

    def set_user_password(self, password):
        self.driver.find_element(By.NAME, self.field_user_password_name).send_keys(password)

    def click_button_sing_in(self):
        self.driver.find_element(By.XPATH, self.button_signin_xpath).click()


