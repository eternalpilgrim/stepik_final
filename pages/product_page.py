from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    # нажатие кнопки "Добавить в корзину"
    def add_product_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn_add_to_basket.click()  
       
    # проверить наличие сообщения о добавлении продукта product_name в корзину
    def should_be_message_with_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        messages = self.browser.find_elements(*ProductPageLocators.MESSAGES)
        assert product_name in messages[0].text, "Wrong product in basket!"
   
    def should_be_message_with_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        messages = self.browser.find_elements(*ProductPageLocators.MESSAGES)
        assert product_price in messages[2].text, "Wrong product price in basket!"

