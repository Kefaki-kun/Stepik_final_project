from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_THE_CART_BUTTON)
        button.click()

    def guest_can_see_product_name(self):
        product_name_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_CART)
        product_name_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_STORE)
        assert product_name_in_store.text == product_name_in_cart.text, \
            "Different names for a product in store and in cart"

    def product_price_is_correct(self):
        product_price_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_CART)
        product_price_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_STORE)
        assert product_price_in_store.text == product_price_in_cart.text, "Incorrect price"

    def check_message_about_adding_to_cart(self):
        cart_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        assert cart_message and self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def check_success_message_on_product_page(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def check_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"
