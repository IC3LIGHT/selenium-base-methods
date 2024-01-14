from selenium.webdriver.common.by import By
import time
from helpers.base import Base

class OperatorApplication(Base):
    # Переход к форме
    CONTENT_BUTTON = (By.XPATH, '(//*[contains(text(), "Контент")])')
    MAP_POINT_SELL = (By.XPATH, '(//*[contains(text(), "Точки продаж")])')

    # Заполнение формы заявки
    CALL_BUTTON = (By.CSS_SELECTOR, '.js-admin-form-new-call')
    CITY_SELECT_FIELD = (By.CSS_SELECTOR, '.select2-selection__arrow')
    CITY_SELECT = (By.CSS_SELECTOR, '.select2-results')
    CITY_SELECT_FIELD = (By.CSS_SELECTOR, '.select2-selection__arrow')
    CITY_SEARCH_FIELD = (By.CSS_SELECTOR, '.select2-search__field')
    CITY_SELECT = (By.CSS_SELECTOR, '.select2-results')
    APPLICATION_NAME = (By.CSS_SELECTOR, '[name="USER_NAME"]')
    APPLICATION_PHONE = (By.CSS_SELECTOR, '[name="USER_PHONE"]')
    APPLICATION_COMMENT = (By.CSS_SELECTOR, '[name="USER_COMMENT"]')
    APPLICATION_SEND_BUTTON = (By.XPATH, "//input[@type='submit']")

    # Открытие заявки
    SEARCH_INPUT = (By.CSS_SELECTOR, '.adm-header-search-block')
    APPLICATION_INFOBLOCK = (By.CSS_SELECTOR, '.adm-submenu-item-name-link-text[1]')

   #Открытие форму с заявкой
  
    def go_to_form(self):
        self.click(self.CONTENT_BUTTON)
        self.scroll(self.MAP_POINT_SELL)
        self.click(self.MAP_POINT_SELL)

    #Заполнение формы

    def do_application(self, name, phone, text):
        self.click(self.CALL_BUTTON)
        self.click(self.CITY_SELECT_FIELD)
        self.enter_text(self.CITY_SEARCH_FIELD, 'Краснодар')
        self.click(self.CITY_SELECT)
        self.enter_text(self.APPLICATION_NAME, name)
        self.enter_text(self.APPLICATION_PHONE, phone)
        self.enter_text(self.APPLICATION_COMMENT, text)
        self.click(self.APPLICATION_SEND_BUTTON)
        time.sleep(2)
        self.alert_ok()
