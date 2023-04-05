import requests


class New_joke():
    """Создание новой шутки"""

    def __init__(self):
        pass

    def create_new_random_joke(self):
        """Создание случайно шутки"""
        url = 'https://api.chucknorris.io/jokes/random'
        print(url)
        result = requests.get(url)
        print(f'Статус код - {result.status_code}')
        assert 200 == result.status_code
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        # check_info = check.get('categories')
        # print(check_info)
        # assert check_info == []
        # print('Категория верна')
        check_info_value = check.get('value')
        print(check_info_value)
        name = 'Chuck'
        if name in check_info_value:
            print('Chuck присутсвует')
        else:
            print('Chuck отсутсвует ')

    def create_new_random_categories_joke(self):
        """Создание случайно шутки на определённую тему"""
        category = "spor"
        url = f'https://api.chucknorris.io/jokes/random?category={category}'
        print(url)
        result = requests.get(url)
        print(f'Статус код - {result.status_code}')
        assert 200 == result.status_code
        print('Успешно!')
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get('categories')
        print(check_info)
        assert check_info == ['sport']
        print('Категория верна')
        # check_info_value = check.get('value')
        # print(check_info_value)
        # name = 'Chuck'
        # if name in check_info_value:
        #     print('Chuck присутсвует')
        # else:
        #     print('Chuck отсутсвует ')


random_joke = New_joke()
# random_joke.create_new_random_joke()
random_joke.create_new_random_categories_joke()
