import allure
import time
from helpers.bitrix import Bitrix
from helpers.operator_call_application import OperatorApplication
from helpers.data_for_tests.data_for_tests import urls, data


@allure.epic('VEKA')
@allure.feature('Заявка оператора')
def test_make_application(browser):
    with allure.step('Заходим в админку битрикса'):
        bitrix = Bitrix(browser=browser, url=urls['url_bitrix'])
        bitrix.do_login()

    with allure.step('Переход к форме'):
        bitrix_application = OperatorApplication(browser=browser, url=urls['url_operator_applications_bitrix'])
        bitrix_application.go_to_form()

    with allure.step('Заполнение и отправка формы'):
        bitrix_application.do_application(data['FIO'], data['phone'], data['comment'])

    with allure.step('Заходим в админку битрикса для проверки'):
        bitrix_application.open()

    with allure.step('Проверка заявки'):
        bitrix.screen('operator_applications', 'Заявки от операторов')
        bitrix.click(bitrix.enter_to_order())

    with allure.step('Проверка полей в админке'):
        assert bitrix.get_attr(bitrix.INPUT_OPERATOR_NAME, value='value') == data['FIO']

    with allure.step('Удаляем данные из админки'):
        time.sleep(3)
        bitrix.del_test_data()
        time.sleep(5)
        bitrix.is_not_visible(bitrix.enter_to_order())
