import time
from .pages.product_page import ProductPage
    
def test_guest_can_add_product_to_basket(browser):
    # открываем страницу с товаром
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,link)
    page.open()
    
    # жмём кнопку "Добавить в корзину"
    page.add_product_to_basket()
    # решаем пример
    page.solve_quiz_and_get_code()
    #time.sleep(150)
    
    # проверяем наличие сообщения о том, что товар добавлен в корзину
    page.should_be_message_with_product_name()
    
    # проверяем сообщение со стоимостью корзины
    page.should_be_message_with_product_price()
