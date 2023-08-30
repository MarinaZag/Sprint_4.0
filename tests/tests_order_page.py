import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from conftest import driver


@allure.feature('Действия на странице оформления заказа')
class TestOrderPage:
    @allure.title('Проверка оформления заказа через кнопку "Заказать" в хедере]')
    @allure.description('Нажать на кнопку "Заказать" в хедере и оформить заказ')
    def test_order_header_order_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.main_url()
        main_page.click_header_order_button()
        order_page.fill_info_who_is_scooter_for_page()
        order_page.fill_info_about_rent_for_page()
        order_page.get_new_order_title()
        assert 'Заказ оформлен' in order_page.find_text(OrderPageLocators.WINDOW_ORDER_IS_PLACED)

    @allure.title('Проверка оформления заказа через кнопку "Заказать" в body')
    @allure.description('Нажать на кнопку "Заказать" в хедере и оформить заказ')
    def test_order_body_order_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.main_url()
        main_page.click_to_order_body_button()
        order_page.fill_info_who_is_scooter_for_page()
        order_page.fill_info_about_rent_for_page()
        order_page.get_new_order_title()
        assert 'Заказ оформлен' in order_page.find_text(OrderPageLocators.WINDOW_ORDER_IS_PLACED)