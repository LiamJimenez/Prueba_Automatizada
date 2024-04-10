from pages.base_page import BasePage
from Data.locators import SearchPageLocators
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    def __init__(self, driver, wait):
        self.url = "https://www.facebook.com/?locale=es_LA"
        self.locator = SearchPageLocators
        super().__init__(driver, wait)

    def go_to_page(self):
        super().go_to_page(self.url)

    def make_a_login_fail(self, input_email, input_password):
        self.driver.find_element(
            *self.locator.SEARCH_INPUT_EMAIL).send_keys(input_email)
        
        self.driver.find_element(
            *self.locator.SEARCH_INPUT_PASSWORD).send_keys(input_password)
        
        self.driver.find_element(
            *self.locator.SEARCH_BUTTON).click()

        self.wait.until(EC.presence_of_element_located(
            self.locator.BUTTON_RESULT))
        
        self.driver.save_screenshot("results/fail_login.png")

    def make_a_registration_fail(self, input_firstname, input_lastname, input_reg_email, input_reg_password):
        self.driver.find_element(
            *self.locator.BUTTON_CREATE).click()
        
        self.wait.until(EC.presence_of_element_located(
            self.locator.BUTTON_SECOND_RESULT))
        
        # Agregar espera explícita antes de buscar el elemento SEARCH_INPUT_NAME
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Nombre"]')))

        self.driver.find_element(
            *self.locator.SEARCH_INPUT_NAME).send_keys(input_firstname)
        
        self.driver.find_element(
            *self.locator. SEARCH_INPUT_LASTNAME).send_keys(input_lastname)
        
        self.driver.find_element(
            *self.locator. SEARCH_INPUT_REG_EMAIL).send_keys(input_reg_email)
        
        self.driver.find_element(
            *self.locator. SEARCH_INPUT_REG_PASSWORD).send_keys(input_reg_password)
        
        self.driver.find_element(
            *self.locator.BUTTON_SUBMIT).click()

        self.wait.until(EC.presence_of_element_located(
            self.locator.BUTTON_REG_RESULT))
        
        self.driver.save_screenshot("results/fail_registration.png")
    
    

        


    

        

        

        






    
    
        
        

    

       



