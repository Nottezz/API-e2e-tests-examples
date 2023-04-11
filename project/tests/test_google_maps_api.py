from requests import Response

from project.utils.api import Google_maps_api

"""Создание, изменение и удаление новой локации"""
class Test_create_location():

    def test_create_new_place(self):

        print('\nМетод POST')
        # result_post: Response = Google_maps_api.create_new_place() # Устаревший вариант
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')

        print('\nМетод GET POST')
        result_get = Google_maps_api.get_new_place(place_id)

        print('\nМетод PUT')
        result_put = Google_maps_api.put_new_place(place_id)

        print('\nМетод GET PUT')
        result_get = Google_maps_api.get_new_place(place_id)

        print('\nМетод DELETE')
        result_get = Google_maps_api.delete_new_place(place_id)

        print('\nМетод GET DELETE')
        result_get = Google_maps_api.get_new_place(place_id)