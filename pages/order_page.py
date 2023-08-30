import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from data.urls import TestUrls


class OrderPage(BasePage):
    @allure.step('Открыть страницу заказа')
    def open_page_order(self):
        self.start_page(TestUrls.ORDER_PAGE_LINK)

    @allure.step('Заполнить контактную информацию для заказа')
    def fill_customer_data(self, firstname="Ирина", lastname="Усачева", address="Профсоюзная, 19", phone="+79260004567"):
        self.add_value(OrderPageLocators.FIELD_NAME, firstname)
        self.add_value(OrderPageLocators.FIELD_SURNAME, lastname)
        self.add_value(OrderPageLocators.FIELD_ADDRESS, address)
        self.add_value(OrderPageLocators.FIELD_PHONE, phone)

    @allure.step('Выбрать станцию метро')
    def choose_metro_station(self):
        self.click_element(OrderPageLocators.FIELD_SUBWAY_STATION)
        self.click_element(OrderPageLocators.METRO_STATION_CLICK)

    @allure.step('Нажать кнопку "Далее"')
    def click_button_next(self):
        self.click_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Выбрать дату "Когда привезти самокат?"')
    def choose_date(self):
        self.click_element(OrderPageLocators.FIELD_CALENDAR)
        self.click_element(OrderPageLocators.CALENDAR)

    @allure.step('Выбрать срок аренды')
    def choose_rent_period(self):
        self.click_element(OrderPageLocators.RENT_PERIOD)
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DAY)

    @allure.step('Выбрать цвет самоката')
    def choose_color(self):
        self.click_element(OrderPageLocators.CHECKBOX_BLACK)

    @allure.step('Кликнуть на кнопку "Заказать"')
    def click_order_button(self):
        self.click_element(OrderPageLocators.BUTTON_ORDER)

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.click_element(OrderPageLocators.BUTTON_CONFIRMATION_ORDER)

    @allure.step('Открыть страницу "Для кого самокат" и заполнить данными для заказа')
    def fill_info_who_is_scooter_for_page(self):
        self.fill_customer_data()
        self.choose_metro_station()
        self.click_button_next()

    @allure.step('Открыть страницу "Про аренду" и заполнить данными для заказа')
    def fill_info_about_rent_for_page(self):
        self.choose_date()
        self.choose_rent_period()
        self.choose_color()
        self.click_element(OrderPageLocators.BUTTON_ORDER)
        self.find_wait_location_element(OrderPageLocators.BUTTON_CONFIRMATION_ORDER)
        self.confirm_order()

    @allure.step('Проверяем наличие модального окна с номером заказа')
    def verify_if_order_is_created(self):
        return self.find_text(OrderPageLocators.WINDOW_ORDER_IS_PLACED)

    @allure.step('Получить окно с текстом "Заказ оформлен"')
    def get_new_order_title(self):
        new_order_text = self.find_text(OrderPageLocators.WINDOW_ORDER_IS_PLACED)
        result = new_order_text.split('\n')
        return result[0]