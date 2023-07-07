
"""
    Модуль "vk_api.py" содержит функции для взаимодействия с VK API.

    Состав модуля:

    1. Функция get_city_id - позволяет получить id города из БД CC "ВКонтакте" по его названию.

    2. Функция search_profiles - принимает данные запроса от пользователя ВК бота в виде словаря,
        предварительно обработанные функцией get_city_id, выполняет запрос через VK API
        на сервер CC "ВКонтакте".

        Полученные ответ преобразует в список словарей, где каждый элемент списка (словарь) хранит данные
        по одному профилю ВК.

        При каждом последующем вызове данной функции, при помощи метода next(), в качестве результата
        будет возвращаться один элемент списка.

    3. Функция add_profiles_photos - принимает словарь с данными, полученными в результате работы
       функции search_profiles.

       Выполняет запрос через VK API н

       Позволяет получить три самые популярные фотографии по кол-ву like'ов для текущего
       профиля ('user_id').

       Производит объединение переданных в функцию и полученных в результате работы функции данных в один словарь.

    Детально ознакомится с работой функций и структурой используемых данных, можно запустив этот модуль.
"""


import os
from pprint import pprint
from datetime import datetime

import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
token = os.getenv('vk_Token')
version = os.getenv('vk_version')

access_params = {
    'access_token': token,
    'v': version
}


def get_city_id(work_dict: dict) -> int:

    """

        Функция позволяет получить id города из БД CC "ВКонтакте" по его названию.

        Args:

            city_name: dict, словарь содержащий данные запроса от пользователя ВК бота.
                       Структура словаря: {'user_id': ..., 'city': type str, 'sex': ..., 'age_from': ..., 'age_to': ...}

        Returns: int, id города из БД CC "ВКонтакте"
                 Структура словаря: {'user_id': ..., 'city': type int, 'sex': ..., 'age_from': ..., 'age_to': ...}

    """

    search_city_url = 'https://api.vk.com/method/database.getCities'

    search_params = {
        'q': work_dict['city'],
        'count': 1
    }

    res = requests.get(search_city_url, params={**access_params, **search_params}).json()

    for i in res['response']['items']:

        return i['id']


def search_profiles(work_dict: dict):

    """
        Функция принимает данные запроса от пользователя ВК бота в виде словаря,
        предварительно обработанные функцией get_city_id, выполняет запрос через VK API
        на сервер CC "ВКонтакте".

        Полученные ответ преобразует в список словарей, где каждый элемент списка (словарь) хранит данные
        по одному профилю ВК.

        При каждом последующем вызове данной функции, при помощи метода next(), в качестве результата
        будет возвращаться один элемент списка.

        Args:
            work_dict: dict - словарь содержащий данные запроса от пользователя ВК бота.
    """

    search_params = {
        'city': work_dict['city'],
        'city_id': work_dict['city'],
        'sex': work_dict['sex'],
        'age_from': work_dict['age_from'],
        'age_to': work_dict['age_to'],
        'count': 1000,
        'has_photo': 1  # только пользователи с фото
    }

    search_clients_url = 'https://api.vk.com/method/users.search'

    info = requests.get(search_clients_url, params={**access_params, **search_params}).json()

    work_list = []

    current_result = 0  # счетчик для нумерации результатов поиска в БД

    for person in info['response']['items']:

        if person['can_access_closed']:  # Отбираем только открытые профили

            try:

                current_result += 1

                work_list.append({'result_id': current_result,
                                  'vk_profile_href': 'https://vk.com/id' + str(person["id"]),
                                  'user_id': person['id'],
                                  'first_name': person['first_name'],
                                  'last_name': person['last_name'],
                                  'photo_href_1': None,
                                  'photo_href_2': None,
                                  'photo_href_3': None
                                  })

            except Exception:

                continue

    for i in work_list:

        yield i


def add_profiles_photos(work_dict: dict) -> dict:

    """
        Функция принимает словарь с данными, полученными в результате работы функции search_profiles.

        Выполняет запрос через VK API на сервер CC "ВКонтакте".

        Позволяет получить три самые популярные фотографии по кол-ву like'ов для текущего профиля ('user_id').

        Производит объединение переданных в функцию и полученных в результате работы функции данных в один словарь.

        Args:
            work_dict: dict, словарь с данными профиля, полученными в результате работы функции search_profiles.

                       Структура словаря: {'first_name': ...,
                                           'last_name': ...,
                                           'photo_href_1': None,
                                           'photo_href_2': None,
                                           'photo_href_3': None,
                                           'result_id': ...,
                                           'user_id': ...,
                                           'vk_profile_href': ...}

        Returns: dict, словарь содержащий все необходимые данные текущего профиля,
                 для дальнейшей работы с БД и ВК ботом.

                 Структура словаря: {'first_name': ...,
                                     'last_name': ...,
                                     'photo_href_1': href_type_str or None,
                                     'photo_href_2': href_type_str None,
                                     'photo_href_3': href_type_str None,
                                     'result_id': ...,
                                     'user_id': ...,
                                     'vk_profile_href': ...}
    """

    need_dict = {}

    search_params = {
        'owner_id': work_dict['user_id'],
        'album_id': 'profile',
        'extended': 1,
        'count': 1000
        }

    search_photos_url = 'https://api.vk.com/method/photos.get'

    res = requests.get(search_photos_url, params={**access_params, **search_params}).json()

    responses = res['response']['items']

    for response in responses:

        if response['owner_id'] not in need_dict.keys():

            need_dict[response['owner_id']] = {
                'photo' + str(response['owner_id']) + '_' + str(response['id']): response['likes']['count']}

        else:

            need_dict[response['owner_id']].update(
                {'photo' + str(response['owner_id']) + '_' + str(response['id']): response['likes']['count']})

    for user_id, links in need_dict.items():

        need_dict[user_id] = (list(sorted(links.items(), key=lambda x: -x[1])))

    for user, value in need_dict.items():

        try:
            work_dict['photo_href_1'] = value[0][0]
            work_dict['photo_href_2'] = value[1][0]
            work_dict['photo_href_3'] = value[2][0]

        except Exception:

            continue

    return work_dict


if __name__ == "__main__":

    start_time = datetime.now()

    req = {'user_id': 787770251, 'city': "Тамбов", 'sex': 1, 'age_from': 20, 'age_to': 35}

    print('*' * 225)
    print("\nИсходный запрос от пользователя ВК: ", req)
    print()

    req['city'] = get_city_id(req)
    print('Запрос от пользователя ВК, после применения функции get_city_id", замена названия города на id: ', req)

    profile = search_profiles(req)
    print('\nРезультат вызова функции "search_profiles": ', profile)

    work_profile = add_profiles_photos(next(profile))
    print('\nВремя получения одного результата по запросу пользователя при помощи функций "get_city_id", '
          '"search_profiles" и "add_profiles_photos" составило: ', datetime.now() - start_time)
    print("\nФормат данных, с которым мы будем работать далее:\n")
    pprint(work_profile)
    print('\n' + '*' * 225)




