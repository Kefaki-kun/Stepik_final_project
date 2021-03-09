from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_THE_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, "#messages div.alertinner strong")
    PRODUCT_NAME_IN_STORE = (By.CSS_SELECTOR, "#content_inner h1:first-child")
    PRODUCT_PRICE_CART = (By.CSS_SELECTOR, ".alert-info p:first-child strong")
    PRODUCT_PRICE_STORE = (By.CSS_SELECTOR, "#content_inner p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alertinner")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class CartPageLocators():
    CART_BUTTON = (By.PARTIAL_LINK_TEXT, "basket")
    EMPTY_MESSAGE = (By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/p")
    CART_ITEMS = (By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/div[1]")
