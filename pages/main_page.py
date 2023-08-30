import allure
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from data.urls import TestUrls

class MainPage(BasePage):

    @allure.step('Главная страница')
    def main_url(self):
        self.start_page(TestUrls.START_PAGE_LINK)

    @allure.step('Кликнуть на логотип Яндекса в хедере страницы')
    def click_yandex_logo(self):
        self.wait_visibility_element(BasePageLocators.LOGO_YANDEX)
        self.click_element(BasePageLocators.LOGO_YANDEX)
        self.cross_new_window()
        self.wait_url_to_be(TestUrls.DZEN_PAGE_LINK)

    @allure.step('Кликнуть на логотип "Самокат" в хедере страницы')
    def click_scooter_logo(self):
        self.wait_visibility_element(BasePageLocators.LOGO_SCOOTER)
        self.click_element(BasePageLocators.LOGO_SCOOTER)

    @allure.step('Кликнуть по кнопке "Заказать" в хедере страницы')
    def click_header_order_button(self):
        self.click_element(BasePageLocators.BUTTON_ORDER_HEADER)
        self.find_wait_location_element(OrderPageLocators.PAGE_ORDER_HEADER)

    @allure.step('Скролл до кнопки "Заказать" в body')
    def scroll_to_order_body_button(self):
        self.scroll_to_element(MainPageLocators.BUTTON_ORDER)
        self.find_wait_location_element(MainPageLocators.BUTTON_ORDER)

    @allure.step('Кликнуть по кнопке "Заказать" в body')
    def click_to_order_body_button(self):
        self.scroll_to_order_body_button()
        self.wait_element_click(MainPageLocators.BUTTON_ORDER)
        self.click_element(MainPageLocators.BUTTON_ORDER)

    @allure.step('Cкролл до блока вопросов')
    def scroll_question_path(self):
        self.scroll_to_element(MainPageLocators.QUESTIONS_SECTION)

    @allure.step('Кликнуть на вопрос в аккордеоне')
    def click_on_question(self, num):
        self.wait_visibility_element(MainPageLocators.QUESTIONS_SECTION)
        questions = self.find_elements_located(MainPageLocators.QUESTIONS)
        questions[num-1].click()

    @allure.step('Получить ответ на вопрос')
    def get_answers(self):
        self.wait_visibility_element(MainPageLocators.CURRENT_ANSWER)
        return self.find_element(MainPageLocators.CURRENT_ANSWER).text

