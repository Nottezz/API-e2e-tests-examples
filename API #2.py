import requests

class Categories_joke():
    """Отображение шуток по всем категороиям"""

    def __init__(self):
        pass

    def categories_joke(self):
        url = 'https://api.chucknorris.io/jokes/categories'

        request = requests.get(url)
        print('Стасус код ' + str(request.status_code))
        assert 200 == request.status_code
        request.encoding = 'utf-8'

        print(request.text + '\n')  # Показывает весь список категорий
        categories = input('Выберите категорию: ')
        categories_disc = request.json()

        for result in categories_disc:
            if categories.lower() == result:
                url = f'https://api.chucknorris.io/jokes/random?category={result}'
                print(url)
                request = requests.get(url)
                joke_categories = request.json()
                joke_result = joke_categories.get('value')
                print(joke_result)
                break
        else:
            print('Вы выброали неправильную категорию')


joke = Categories_joke()
joke.categories_joke()