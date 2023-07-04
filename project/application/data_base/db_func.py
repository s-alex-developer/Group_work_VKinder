"""
    Модуль "db_func.py" содержит функции для работы с Базой данных.

    Состав модуля:

        1. Функция create_engine - создает "движок" для открытия рабочей сессии с базой данных.

        2. Функция create_session - открывает сессию работы с базой данных.

        3. Функция add_search_results - выполняет запись одной строки в таблицу БД "search_results"

        4. Функция get_next - выполняет SELECT запрос к таблице БД "search_results", получает одну запись,
           соответсвующую текущему значению параметра "result_id".

        5. Функция add_to_favorite_profiles - выполняет INSERT запрос к таблице БД 'favorite_profiles',
           "Избранные профили", и добавляет в неё одну запись.

        6. Функция add_to_blocked_profiles - выполняет INSERT запрос к таблице БД 'blocked_profiles',
           ("Игнорируемые профили") и добавляет в неё одну запись.

        7. Функция show_favorite_profiles - выполняет SELECT запрос к таблице БД 'favorite_profiles',
           получает из неё все данные, соответствующие параметрам запроса, и возвращает их для последующей отправки
           пользователю ВК.

        8. Функция clean_search_results - удаляет из таблицы БД "search_results" все результаты текущей сессии поиска
           для пользователя ВК соответствующему параметру user_id.

        9. Функция check_in_favorite_profiles - выполняет SELECT запрос к таблице БД 'favorite_profiles',
           "Избранные профили" и проверяет наличие в ней записи, соответствующей условиям запроса.

        10. Функция check_in_blocked_profiles - выполняет SELECT запрос к таблице БД 'blocked_profiles',
            "Заблокированные профили" и проверяет наличие в ней записи, соответствующей условиям запроса.

"""

import os

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from dotenv import find_dotenv, load_dotenv


def create_engine():

    """
        Функция создает "движок" для открытия рабочей сессии с базой данных.

        Returns: engine
    """

    load_dotenv(find_dotenv())

    _DNS_ = f"postgresql://{os.getenv('db_username')}:{os.getenv('db_user_password')}" \
            f"@{os.getenv('db_hostname')}:{os.getenv('db_port')}/{os.getenv('db_name')}"

    engine = sqlalchemy.create_engine(_DNS_)

    return engine


def create_session():

    """
        Функция открывает сессию работы с базой данных.

        Returns: session
    """

    engine = create_engine()

    _Session_ = sessionmaker(bind=engine)

    session = _Session_()

    return session


def add_search_results(user_id: int, work_dict: dict, SearchResults):

    """
        Функция выполняет запись одной строки в таблицу БД "search_results" ("Результаты поиска").

        Args:
            user_id: id пользователя ВК, который общается с ботом.

            work_dict: словарь, содержащий данные для записи в БД.

            SearchResults: ссылка на класс SearchResults, создающий модель таблицы "search_results",
                           импортируется из модуля db_models.py
        Returns:

    """

    session = create_session()

    session.add(SearchResults(
                user_id=user_id,
                result_id=work_dict['result_id'],
                vk_profile_href=work_dict["vk_profile_href"],
                first_name=work_dict["first_name"],
                last_name=work_dict["last_name"],
                photo_href_1=work_dict["photo_href_1"],
                photo_href_2=work_dict["photo_href_2"],
                photo_href_3=work_dict["photo_href_3"])
                )

    session.commit()

    session.close()

    return


def get_next(user_id: int, result_id: int, SearchResults) -> list[dict]:

    """
        Функция выполняет SELECT запрос к таблице БД "search_results", получает одну запись,
        соответсвующую текущему значению параметра "result_id".

        Args:
            user_id: id пользователя ВК, который общается с ботом.

            result_id: идентификатор, присваиваемый каждой записи в таблице БД "search_results".

            SearchResults: ссылка на класс SearchResults, создающий модель таблицы "search_results",
                           импортируется из модуля db_models.py

        Returns: list[dict]  - список из трех словарей.
                               Первые два элемента списка с индексами 0 и 1 используются для формирования и отправки
                               очередного результата поиска пользователю ВК бота.
                               Третий элемент списка с индексом 2 содержит все необходимые данные
                               в установленном формате, для записи текущего результата поиска
                               в таблицы 'favorite_profiles' и 'blocked_profiles', "Избранные" и "Игнорируемые"
                               пользователи соответственно.
    """

    session = create_session()

    for c in session.query(SearchResults).filter(SearchResults.user_id == f'{user_id}')\
            .filter(SearchResults.result_id == f'{result_id}'):

        result = [
            {'1': f'{c.first_name} {c.last_name} \n{c.vk_profile_href}'},
            {'2': f'{c.photo_href_1},{c.photo_href_2},{c.photo_href_3}'},
            {'user_id': f'{user_id}', "vk_profile_href": f'{c.vk_profile_href}', "first_name": f'{c.first_name}',
             "last_name": f'{c.last_name}', "photo_href_1": f'{c.photo_href_1}', "photo_href_2": f'{c.photo_href_2}',
             "photo_href_3": f'{c.photo_href_3}'}
        ]

        return result


def add_to_favorite_profiles(work_dict: list[dict], FavoriteProfiles) -> str:

    """
        Функция выполняет INSERT запрос к таблице БД 'favorite_profiles', "Избранные профили",
        и добавляет в неё одну запись.

        Args:
            work_dict: список словарей, элемент списка с индексом 2 содержит все необходимые для записи в БД данные.

            FavoriteProfiles: ссылка на класс FavoriteProfiles, создающий модель таблицы 'favorite_profiles',
                              импортируется из модуля db_models.py

        Returns: res_text - переменную, содержащую текстовые данные, для ответа пользователю ВК.

    """

    session = create_session()

    session.add(FavoriteProfiles(
        user_id=work_dict[2]["user_id"],
        vk_profile_href=work_dict[2]["vk_profile_href"],
        first_name=work_dict[2]["first_name"],
        last_name=work_dict[2]["last_name"],
        photo_href_1=work_dict[2]["photo_href_1"],
        photo_href_2=work_dict[2]["photo_href_2"],
        photo_href_3=work_dict[2]["photo_href_3"])
    )

    session.commit()

    session.close()

    res_text = 'Профиль добавлен в "Избранное"!'

    return res_text


def add_to_blocked_profiles(work_dict: list[dict], BlockedProfiles) -> str:

    """
        Функция выполняет INSERT запрос к таблице БД 'blocked_profiles', "Игнорируемые профили"
        и добавляет в неё одну запись.

        Args:
            work_dict: список словарей, элемент списка с индексом 2 содержит все необходимые для записи в БД данные.

            BlockedProfiles: ссылка на класс BlockedProfiles, создающий модель таблицы 'blocked_profiles',
                             импортируется из модуля db_models.py

        Returns: res_text - переменную, содержащую текстовые данные, для ответа пользователю ВК.

    """

    session = create_session()

    session.add(BlockedProfiles(
        user_id=work_dict[2]["user_id"],
        vk_profile_href=work_dict[2]["vk_profile_href"])
    )

    session.commit()

    session.close()

    res_text = f'Пользователь {work_dict[2]["first_name"]} {work_dict[2]["last_name"]} добавлен в "Черный список"!'

    return res_text


def show_favorite_profiles(user_id: int, FavoriteProfiles) -> list[list[dict]]:

    """
        Функция выполняет SELECT запрос к таблице БД 'favorite_profiles', получает из неё все данные,
        соответствующие параметрам запроса, и возвращает их для последующей отправки пользователю ВК.

        Args:
            user_id: id пользователя ВК, который общается с ботом.

            FavoriteProfiles: ссылка на класс FavoriteProfiles, создающий модель таблицы 'favorite_profiles',
                              импортируется из модуля db_models.py

        Returns: список, элементами которого являются списки со вложенными словарями.
                 Данные используются для отправки ответа пользователю ВК.

    """

    session = create_session()

    sql_resp = session.query(FavoriteProfiles).filter(FavoriteProfiles.user_id == user_id)

    work_list = []

    for row in sql_resp:

        work_list.append([{'1': f'{row.first_name} {row.last_name} \n{row.vk_profile_href}'},
                         {'2': f'{row.photo_href_1},{row.photo_href_2},{row.photo_href_3}'}])

    return work_list


def clean_search_results(user_id: int, SearchResults) -> str:

    """

        Функция удаляет из таблицы БД "search_results" все результаты текущей сессии поиска для пользователя ВК
        соответствующему параметру user_id.

        Args:
            user_id: id пользователя ВК, который общается с ботом.

            SearchResults: ссылка на класс SearchResults, создающий модель таблицы "search_results",
                           импортируется из модуля db_models.py

        Returns: res_text - переменную, содержащую текстовые данные, для ответа пользователю ВК.

    """

    session = create_session()

    session.query(SearchResults).filter(SearchResults.user_id == user_id).delete()

    session.commit()

    session.close()

    res_text = "Поиск завершен."

    return res_text


def check_in_favorite_profiles(user_id: int, work_dict: list[dict], FavoriteProfiles) -> list:

    """

        Функция выполняет SELECT запрос к таблице БД 'favorite_profiles', "Избранные профили" и проверяет наличие в ней
        записи, соответствующей условиям запроса.

        Args:
            user_id: id пользователя ВК, который общается с ботом.

            work_dict: список словарей, элемент списка с индексом 2 содержит все необходимые данные для проверки.

            FavoriteProfiles: ссылка на класс FavoriteProfiles, создающий модель таблицы 'favorite_profiles',
                              импортируется из модуля db_models.py

        Returns: True or False

    """

    session = create_session()

    sql_resp = session.query(FavoriteProfiles).filter(FavoriteProfiles.user_id == user_id)

    for result in sql_resp:

        if result.vk_profile_href == work_dict[2]['vk_profile_href']:

            return [True, f'Совпадение по "Избранным": {result.first_name} {result.last_name}.']

    return [False, f'Совпадение по "Избранным" нет.']


def check_in_blocked_profiles(user_id: int, work_dict: list[dict], BlockedProfiles) -> list:

    """

        Функция выполняет SELECT запрос к таблице БД 'blocked_profiles', "Игнорируемые профили" и проверяет наличие
        в ней записи, соответствующей условиям запроса.

        Args:
            user_id: id пользователя ВК, который общается с ботом.

            work_dict: список словарей, элемент списка с индексом 2 содержит все необходимые данные для проверки.

            BlockedProfiles: ссылка на класс BlockedProfiles, создающий модель таблицы 'blocked_profiles',
                             импортируется из модуля db_models.py

        Returns: True or False

    """

    session = create_session()

    sql_resp = session.query(BlockedProfiles).filter(BlockedProfiles.user_id == user_id)

    for result in sql_resp:

        if result.vk_profile_href == work_dict[2]['vk_profile_href']:

            return [True, f'Совпадение по "Заблокированным", ссылка на страницу: {result.vk_profile_href}.']

    return [False, f'Совпадение по "Заблокированным" нет.']


if __name__ == "__main__":

    print('*' * 225)
    help(create_engine)
    print('*' * 225)
    help(create_session)
    print('*' * 225)
    help(add_search_results)
    print('*' * 225)
    help(get_next)
    print('*' * 225)
    help(add_to_favorite_profiles)
    print('*' * 225)
    help(add_to_blocked_profiles)
    print('*' * 225)
    help(show_favorite_profiles)
    print('*' * 225)
    help(clean_search_results)
    print('*' * 225)
    help(check_in_favorite_profiles)
    print('*' * 225)
    help(check_in_blocked_profiles)
    print('*' * 225)