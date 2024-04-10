from selenium.webdriver.common.by import By

class SearchPageLocators:
    SEARCH_INPUT_EMAIL = (By.XPATH, "//*[@id='email']")
    SEARCH_INPUT_PASSWORD = (By.XPATH, "//*[@id='pass']")
    SEARCH_BUTTON = (By.NAME, "login")
    BUTTON_RESULT = SEARCH_BUTTON

    BUTTON_CREATE = (By.CSS_SELECTOR, "[rel='async']")
    BUTTON_SECOND_RESULT = BUTTON_CREATE
    SEARCH_INPUT_NAME = (By.CSS_SELECTOR, '[aria-label="Nombre"]')  
    SEARCH_INPUT_LASTNAME = (By.NAME, "lastname")
    SEARCH_INPUT_REG_EMAIL = (By.NAME, "reg_email__")
    SEARCH_INPUT_REG_PASSWORD = (By.NAME, "reg_passwd__")
    BUTTON_SUBMIT = (By.NAME, "websubmit")
    BUTTON_REG_RESULT = BUTTON_SUBMIT

   
   


    
    
    
   