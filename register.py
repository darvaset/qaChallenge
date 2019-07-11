class RegisterPage():

    def __init__ (self, driver):
        self.driver = driver

        self.emailFieldId = 'email'
        self.passwordFieldId = 'password'
        self.registerButtonId = 'register'

    def enter_email(self, email):
        self.driver.find_element_by_id(self.emailFieldId).clear()
        self.driver.find_element_by_id(self.emailFieldId).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.passwordFieldId).clear()
        self.driver.find_element_by_id(self.passwordFieldId).send_keys(password)

    def click_register_button(self):
        self.driver.find_element_by_id(self.registerButtonId).click()
