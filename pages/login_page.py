class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_field = "#user-name"
        self.password_field = "#password"
        self.login_button = "#login-button"
        self.error_message = ".error-message-container"
    
    def goto(self):
        self.page.goto("https://www.saucedemo.com/")
    
    def login(self, username, password):
        self.page.fill(self.username_field, username)
        self.page.fill(self.password_field, password)
        self.page.click(self.login_button)
    
    def is_error_visible(self):
        return self.page.is_visible(self.error_message)
    
    def get_error_text(self):
        return self.page.text_content(self.error_message)
