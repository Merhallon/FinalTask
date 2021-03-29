from time import sleep

from .base_page import BasePage
from .locators import ProductPageLocators


# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class ProductPage(BasePage):
    def add_product_to_basket(self, link):
        self.browser.get(link)
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button_add_to_basket.click()
        self.solve_quiz_and_get_code()

        self.should_be_name_product()
        self.should_be_price()

    def should_be_name_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ALERT).text

        assert product_name == name_in_message

    def should_be_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        self.browser.find_element(*ProductPageLocators.ALERT_MESSAGE)
        price_in_message = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MESSAGE).text

        assert product_price == price_in_message
