import requests

class Test_new_joke():
    """Создание новой шутки"""

    def __init__(self):
        pass

    def test_create_new_random_joke(self):
        """Создание случайно шутки"""
        url = 'https://api.chucknorris.io/jokes/random'
        print(url)
        result = requests.get(url)
        print(f'Статус код - {result.status_code}')
        assert 200 == result.status_code
        if result.status_code == 200:
            print('Успешно!')
        else:
            print('Провал!')
        result.encoding = 'utf-8'
        print(result.text)

random_joke = Test_new_joke()
random_joke.test_create_new_random_joke()

