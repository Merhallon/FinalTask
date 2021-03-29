from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, '//form[@id="login_form"]')
    RIGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")

    PRODUCT_FORM = (By.CSS_SELECTOR, ".product.main")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1:nth-child(1)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color:nth-child(2)")

    ALERT_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1)")
    PRODUCT_NAME_IN_ALERT = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")

    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alertinner>p>strong")
