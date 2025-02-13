import time
from PageObject.LoginPage import LoginPage

class Test_Login():
    BaseURL = "https://app-staging.laer.ai/login"
    useremail = "aida@laerai.com"
    password = "aida456321@"

    def test_LoginHomepagetitle(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.BaseURL)
        time.sleep(3)
        actual_title = self.driver.title
        time.sleep(3)
        if(actual_title == "Aida"):
            assert True
            self.driver.close()
        else:
            assert False


