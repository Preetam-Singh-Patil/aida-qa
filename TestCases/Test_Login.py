import time
from PageObject.LoginPage import LoginPage

class Test_Login():
    BaseURL = "https://app-staging.laer.ai/login"
    useremail = "aida@laerai.com"
    password = "aida456321@"

    def test_001_LoginHomepagetitle(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.BaseURL)
        time.sleep(3)
        actual_title = self.driver.title
        time.sleep(3)
        if(actual_title == "Aida"):
            assert True
            print("Testcase passed - AIDA Homepage title verified")
            self.driver.close()
        else:
            assert False
            print("Testcase failed")

    def test_002_AIDA_signin(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.BaseURL)
        time.sleep(3)
        self.lp = LoginPage(self.driver)
        self.lp.set_user_email(self.useremail)
        time.sleep(1)
        self.lp.set_user_password(self.password)
        time.sleep(1)
        self.lp.click_button_sing_in()
        time.sleep(2)
        current_URL = self.driver.current_url
        time.sleep(1)
        if(current_URL == "https://app-staging.laer.ai/"):
            assert True
            print("Testcase passed - AIDA Signin verified")
            self.driver.close()
        else:
            assert False
            print("Testcase failed")



