from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
#от него наследуются все остальные страницы
class BasePage:
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url #говорим что при открытии страницы драйвер и урл обязательно должны быть

    def open(self):
        self.driver.get(self.url) #функция открытия страниц. чтобы сделать первую логику.

    def element_is_visible (self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove()") #в консоли убрать проверить document.getElementsByTagName('footer')[0].remove()
        self.driver.execute_script('document.getElementById("fixedban").style.display="none"') #тоже проверка document.getElementById("fixedban").style.display="none"