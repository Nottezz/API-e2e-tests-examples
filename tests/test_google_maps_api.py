import allure
from src.utils.api import Google_maps_api
from src.utils.cheking import Checking

@allure.epic('Google Maps API')
@allure.feature('Create, Update, Delete Place')
class TestCreateLocation:

    place_id = None

    @allure.title("Создание новой локации (POST)")
    def test_post_create_place(self):
        with allure.step("Выполняем POST запрос для создания локации"):
            result_post = Google_maps_api.create_new_place()
            allure.attach(str(result_post.json()), "POST Response", allure.attachment_type.JSON)

        with allure.step("Проверяем статус код"):
            Checking.check_status_code(result_post, 200)

        with allure.step("Проверяем наличие ключей в JSON"):
            Checking.check_js_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])

        with allure.step("Проверяем значение ключа 'status'"):
            Checking.check_json_value(result_post, 'status', 'OK')

        TestCreateLocation.place_id = result_post.json().get('place_id')

    @allure.title("Получение созданной локации (GET)")
    def test_get_created_place(self):
        with allure.step(f"Выполняем GET запрос для place_id={TestCreateLocation.place_id}"):
            result_get = Google_maps_api.get_new_place(TestCreateLocation.place_id)
            allure.attach(str(result_get.json()), "GET POST Response", allure.attachment_type.JSON)

        with allure.step("Проверяем статус код"):
            Checking.check_status_code(result_get, 200)

        with allure.step("Проверяем ключи JSON"):
            Checking.check_js_token(result_get,
                                    ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])

        with allure.step("Проверяем значение адреса"):
            Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

    @allure.title("Обновление адреса локации (PUT)")
    def test_put_update_place(self):
        with allure.step(f"Выполняем PUT запрос для place_id={TestCreateLocation.place_id}"):
            result_put = Google_maps_api.put_new_place(TestCreateLocation.place_id)
            allure.attach(str(result_put.json()), "PUT Response", allure.attachment_type.JSON)

        with allure.step("Проверяем статус код"):
            Checking.check_status_code(result_put, 200)

        with allure.step("Проверяем ключи JSON"):
            Checking.check_js_token(result_put, ['msg'])

        with allure.step("Проверяем сообщение об обновлении"):
            Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

    @allure.title("Проверка обновлённой локации (GET после PUT)")
    def test_get_updated_place(self):
        with allure.step(f"Выполняем GET запрос для проверки обновления place_id={TestCreateLocation.place_id}"):
            result_get = Google_maps_api.get_new_place(TestCreateLocation.place_id)
            allure.attach(str(result_get.json()), "GET PUT Response", allure.attachment_type.JSON)

        with allure.step("Проверяем статус код"):
            Checking.check_status_code(result_get, 200)

        with allure.step("Проверяем ключи JSON"):
            Checking.check_js_token(result_get,
                                    ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])

        with allure.step("Проверяем новый адрес"):
            Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

    @allure.title("Удаление локации (DELETE)")
    def test_delete_place(self):
        with allure.step(f"Выполняем DELETE запрос для place_id={TestCreateLocation.place_id}"):
            result_delete = Google_maps_api.delete_new_place(TestCreateLocation.place_id)
            allure.attach(str(result_delete.json()), "DELETE Response", allure.attachment_type.JSON)

        with allure.step("Проверяем статус код"):
            Checking.check_status_code(result_delete, 200)

        with allure.step("Проверяем ключи JSON"):
            Checking.check_js_token(result_delete, ['status'])

        with allure.step("Проверяем значение ключа 'status'"):
            Checking.check_json_value(result_delete, 'status', 'OK')

    @allure.title("Проверка удаления локации (GET после DELETE)")
    def test_get_deleted_place(self):
        with allure.step(f"Выполняем GET запрос для проверки удаления place_id={TestCreateLocation.place_id}"):
            result_get = Google_maps_api.get_new_place(TestCreateLocation.place_id)
            allure.attach(str(result_get.json()), "GET DELETE Response", allure.attachment_type.JSON)

        with allure.step("Проверяем статус код"):
            Checking.check_status_code(result_get, 404)

        with allure.step("Проверяем ключи JSON"):
            Checking.check_js_token(result_get, ['msg'])

        with allure.step("Проверяем сообщение об ошибке"):
            Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")