from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def check_cart_empty(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEMS), \
            "Product is displayed in the cart but should not be"

    def check_empty_message_in_cart(self):
        empty_cart_message = self.browser.find_element(*CartPageLocators.EMPTY_MESSAGE)
        assert empty_cart_message and self.is_element_present(*CartPageLocators.EMPTY_MESSAGE), \
            "Empty message is not displayed, but should be"
