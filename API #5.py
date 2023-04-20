import requests


class Darth_Vader():
    """Список актёров, которые играли с Дартом Вейдером"""

    def list_of_actors(self):
        """Запрос списка фильмов"""

        base_url = 'https://swapi.dev/api/'
        key = 'people/4/'

        "Метод GET для получения списка фильмов"

        get_url = base_url + key
        print(get_url)

        result_get = requests.get(get_url)
        # print(result_get.text)

        films_list = result_get.json()
        films = films_list.get('films')

        "Метод GET для получения всех фильмов где снимался Вейдер"

        for film in films:

            get_url_film = film
            print(get_url_film)

            result_get = requests.get(get_url_film)
            print(result_get.text)

            films_list = result_get.json()
            characters = films_list.get('characters')
            title_name = films_list.get('title')
            # with open('actors_name.txt', mode='a', encoding='utf-8') as file:
            #     file.write("\n" + title_name + "\n")


        #     "Метод GET для вывода имени актёра"
        #
        #     list_name = []
        #
        #     for character_name in characters:
        #         get_url_actor = character_name
        #         result_get = requests.get(get_url_actor)
        #         # print(result_get.text)
        #
        #         character_name = result_get.json()
        #         name = character_name.get('name')
        #         print(name)
        #         list_name.append(name)
        #         # print(list_name)
        #         lis_name = set(list_name)
        #         print(lis_name)
        #
        #         with open('actors_name.txt', mode='a', encoding='utf-8') as file:
        #             file.write(str(list(list_name)) + '\n')
        #
        # print('Имена актёров успешно сохранены!')


actors = Darth_Vader()
actors.list_of_actors()
