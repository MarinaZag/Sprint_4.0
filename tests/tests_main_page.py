import allure
from data.urls import TestUrls
from pages.main_page import MainPage
from conftest import driver


@allure.feature('Действия на главной странице')
class TestMainPage:

    @allure.title('Проверка перехода со стартовой страницы по клику логотип "Яндекса"')
    @allure.description('На странице нажать на логотип "Яндекса" в хедере, и происходит переход на страницу Яндекс.Дзен')
    def test_click_on_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.main_url()
        main_page.click_yandex_logo()
        assert driver.current_url == TestUrls.DZEN_PAGE_LINK

    @allure.title('Проверка перехода по логотипу "Самокат"')
    @allure.description('По клику на логотип "Самокат" осуществляется переход на главную страницу')
    def test_base_page_transition_logo_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.main_url()
        main_page.click_scooter_logo()
        assert driver.current_url == TestUrls.START_PAGE_LINK
