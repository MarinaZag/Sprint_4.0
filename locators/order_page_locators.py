from selenium.webdriver.common.by import By


class OrderPageLocators:
    PAGE_ORDER_HEADER = By.XPATH, ".//div[text() = 'Для кого самокат']"
    FIELD_NAME = By.XPATH, "//input[contains(@placeholder, '* Имя')]"
    FIELD_SURNAME = By.XPATH, "//input[contains(@placeholder, '* Фамилия')]"
    FIELD_ADDRESS = By.XPATH, "//input[contains(@placeholder, '* Адрес: куда привезти заказ')]"
    FIELD_PHONE = By.XPATH, "//input[contains(@placeholder, '* Телефон: на него позвонит курьер')]"
    FIELD_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")
    SELECTED_STATION = (By.CSS_SELECTOR, '[class="select-search__select"]')
    FIELD_CALENDAR = By.XPATH, "//input[contains(@placeholder, '* Когда привезти самокат')]"
    CALENDAR = By.XPATH, ".//div[contains(@class, 'react-datepicker__day--today')]"
    RENTAL_PERIOD_DAY = By.XPATH, "//div[contains(@class, 'Dropdown-option') and (text()='сутки')]"
    RENT_PERIOD = By.XPATH, ".//div[contains(@class, 'Dropdown-control')]"
    CHECKBOX_BLACK = By.XPATH, "//div[starts-with(@class, 'Order_Checkboxes')]/*/input[@id='black']"
    BUTTON_ORDER = By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[contains(@class, 'Button_Button') and (text()='Заказать')]"
    BUTTON_CONFIRMATION_ORDER = By.XPATH, "//button[contains(text(), 'Да')]"
    FIELD_SUBWAY_STATION = By.XPATH, "//input[@class='select-search__input']"
    METRO_STATION_CLICK = By.XPATH, ".//button[@value = '1']"
    WINDOW_ORDER_IS_PLACED = By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"

