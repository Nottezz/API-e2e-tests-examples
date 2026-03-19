import allure
from src.utils.api import Google_maps_api
from src.utils.cheking import Checking

"""Создание, изменение и удаление новой локации"""


@allure.epic('Test create place')
class Test_create_location():
    @allure.description("Test create, update, delete new location")
    def test_create_new_place(self):
        print('\nМетод POST')
        # result_post: Response = Google_maps_api.create_new_place() # Устаревший вариант
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_post, 200)
        Checking.check_js_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        # token = json.loads(result_post.text)
        # print(list(token)) # Для вывода всех нужных полей при ответе
        Checking.check_json_value(result_post, 'status', 'OK')

        print('\nМетод GET POST')
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_js_token(result_get,
                                ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print('\nМетод PUT')
        result_put = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_js_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print('\nМетод GET PUT')
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_js_token(result_get,
                                ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                 'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print('\nМетод DELETE')
        result_delete = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_js_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print('\nМетод GET DELETE')
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_js_token(result_get, ['msg'])
        Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")

        print('\nТестирование создания, изменения и удаления новой локации прошло успешно')
