from selenium.webdriver.common.by import By
from random import randint
class FormPageLocators: #https://demoqa.com/automation-practice-form
    LAST_NAME = (By.CSS_SELECTOR, "#lastName") #lastName чтобы проверить уникальность в элементах
    FIRST_NAME = (By.CSS_SELECTOR, "#firstName")
    EMAIL = (By.CSS_SELECTOR, "#userEmail")
    GENDER = (By.CSS_SELECTOR, f"[for='gender-radio-{randint(1,3)}']")  #radint нужен для рандома, а label[for='gender-radio-1'] проверка в элементах
    MOBILE = (By.CSS_SELECTOR, "#userNumber")
    SUBJECT = (By.CSS_SELECTOR, "#subjectsInput")
    HOBBIES = (By.CSS_SELECTOR, f"[for='hobbies-checkbox-{randint(1,3)}']") #radint нужен для рандома
    FILE_INPUT = (By.CSS_SELECTOR, "#uploadPicture")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress")
    SUBMIT = (By.CSS_SELECTOR, "#submit")

    RESULT_TABLE = (By.XPATH, '//div[@class="table-responsive"]//td[2]') #//div[@class="table-responsive"]//td[2] найти в элементах только td локаторы


