import requests

class New_location():
    """Работа с новой локацией"""

    def create_new_location(self):
        """Создание новой локации"""

        base_url = 'https://rahulshettyacademy.com' # Базовый URL
        key = "?key=qaclick123"                   # Параметр для всех запросов

        """Создание метода POST"""
        post_resourece = '/maps/api/place/add/json' # Ресурст метода POST

        post_url = base_url + post_resourece + key
        print(post_url)

        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        result_post = requests.post(post_url, json=json_for_create_new_location)
        print(result_post.text)
        print(f'Статус код - {result_post.status_code}')
        assert 200 == result_post.status_code
        print('Успешно!')
        check_post = result_post.json()
        check_info_post = check_post.get('status')
        print('Статус код ответа: ' + check_info_post)
        assert check_info_post == 'OK'
        print('Статус ответа верен')
        place_id = check_post.get('place_id')
        print(place_id)

        """Проверка созданной локации"""

        get_resourece = "/maps/api/place/get/json"
        get_url = base_url + get_resourece + key + "&place_id=" + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print(f'Статус код - {result_get.status_code}')
        assert 200 == result_get.status_code
        print('Успешно! Проверка пройдена')

        """Изменение новой локации"""

        put_resourece = "/maps/api/place/update/json"
        put_url = base_url + put_resourece + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = requests.put(put_url, json=json_for_update_new_location)
        print(result_put.text)
        print(f'Статус код - {result_put.status_code}')
        assert 200 == result_put.status_code
        check_msg = result_put.json()
        msg = check_msg.get('msg')
        print(msg)
        assert msg == "Address successfully updated"
        print('Сообщение верно')

        """Проверка изменений в локации"""

        result_get = requests.get(get_url)
        print(result_get.text)
        print(f'Статус код - {result_get.status_code}')
        assert 200 == result_get.status_code
        print('Успешно! Проверка пройдена')
        check_address = result_get.json()
        adress = check_address.get('address')
        print(adress)
        assert adress == "100 Lenina street, RU"
        print('Адрес изменён верно')

        """Удаление новой локации"""

        delete_resource = '/maps/api/place/delete/json'
        delete_url = base_url + delete_resource + key
        print(delete_url)

        json_for_delete_new_location = {
            "place_id": place_id
        }
        result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
        print(result_delete.text)
        print(f'Статус код - {result_delete.status_code}')
        assert 200 == result_delete.status_code
        print('Успешно! Проверка пройдена')
        check_status = result_delete.json()
        status = check_status.get('status')
        print(status)
        assert status == "OK"
        print('Локация удалена')



place = New_location()
place.create_new_location()
