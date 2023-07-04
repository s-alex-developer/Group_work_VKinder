import os

import bs4
import vk_api
import requests
from dotenv import find_dotenv, load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from application.vk_api.vk_apy import get_city_id, search_profiles, add_profiles_photos

from application.data_base.db_models import SearchResults, BlockedProfiles, FavoriteProfiles

from application.data_base.db_func import check_in_favorite_profiles, check_in_blocked_profiles
from application.data_base.db_func import get_next, show_favorite_profiles, clean_search_results
from application.data_base.db_func import add_search_results, add_to_favorite_profiles, add_to_blocked_profiles

load_dotenv(find_dotenv())

vk_session = vk_api.VkApi(token=os.getenv('vk_group_token'))

vk = vk_session.get_api()

longpool = VkLongPoll(vk_session)

res = {'user_id': None, 'city': None, 'sex': None, 'age_from': None, 'age_to': None}


def send_some_msg(id, some_text, attachment=None, keyboard=None):

    post = {
        "user_id": id,
        "message": some_text,
        "random_id": 0

    }

    if keyboard != None:

        post["keyboard"] = keyboard.get_keyboard()

    if attachment != None:

        post['attachment'] = attachment
    vk_session.method("messages.send", post)


def _clean_all_tag_from_str(string_line):

    """
    Очистка строки stringLine от тэгов и их содержимых
    :param string_line: Очищаемая строка
    :return: очищенная строка
    """

    result = ""
    not_skip = True

    for i in list(string_line):

        if not_skip:

            if i == "<":
                not_skip = False

            else:
                result += i

        else:

            if i == ">":
                not_skip = True

    return result


def get_user_name_from_vk_id(user_id):

    request = requests.get("https://vk.com/id" + str(user_id))
    bs = bs4.BeautifulSoup(request.text, "html.parser")

    user_name = _clean_all_tag_from_str(bs.findAll("title")[0])

    return user_name.split()[0]


while True:

    for event in longpool.listen():

        if event.type == VkEventType.MESSAGE_NEW:

            if event.to_me:

                msg = event.text.lower()
                id = event.user_id
                res['user_id'] = id
                name = get_user_name_from_vk_id(id)

                match msg:

                    case 'завершить' | 'начать поиск':

                        send_some_msg(id,
                                      'Привет, ' + name + "!" + ' Чтобы подобрать вам пару - ответьте на несколько '
                                                                'вопросов:\nВведите название вашего города')
                        flag = False

                        while not flag:

                            for event in longpool.listen():

                                if event.type == VkEventType.MESSAGE_NEW:

                                    if event.to_me:

                                        city = event.text.lower()
                                        res['city'] = city.title()

                                        if get_city_id(res):

                                            send_some_msg(id,
                                                          'Отлично, Ваш город' + ' ' + city.title() +
                                                          '\nС кем бы вы хотели познакомиться?')

                                            keyboard = VkKeyboard(inline=True)
                                            buttons = ["Мужчина", "Женщина"]
                                            keyboard.add_button('Мужчина', VkKeyboardColor.PRIMARY)
                                            keyboard.add_button('Женщина', VkKeyboardColor.POSITIVE)

                                            send_some_msg(id, "Нажмите на кнопку: ", keyboard=keyboard)
                                            flag = True

                                            break

                                        else:

                                            keyboard = VkKeyboard(one_time=True)

                                            keyboard.add_button('Начать поиск', VkKeyboardColor.POSITIVE)
                                            send_some_msg(id, "Ошибка, такого города не существует, давай еще раз",
                                                          )
                                            flag = False

                                            break

                        flag = False

                        while not flag:

                            for event in longpool.listen():

                                if event.type == VkEventType.MESSAGE_NEW and event.to_me:

                                    sex = event.text.lower()

                                    match sex:

                                        case "женщина":

                                            res['sex'] = 1
                                            flag = True

                                        case "мужчина":

                                            res['sex'] = 2
                                            flag = True

                                        case _:

                                            flag = False

                                            keyboard = VkKeyboard(inline=True)
                                            buttons = ["Мужчина", "Женщина"]
                                            keyboard.add_button('Мужчина', VkKeyboardColor.PRIMARY)
                                            keyboard.add_button('Женщина', VkKeyboardColor.POSITIVE)

                                            send_some_msg(id, "Нажмите на кнопку: ", keyboard=keyboard)

                                            break

                                    send_some_msg(id,
                                                  'Введите через дефис диапазон искомого возраста .\n'
                                                  'Пример : 20-30, означает что в'
                                                  ' результат попадут только пользователи от 20 до 30 лет ')
                                    break

                        flag = False

                        while not flag:

                            for event in longpool.listen():

                                if event.type == VkEventType.MESSAGE_NEW and event.to_me:

                                    try:
                                        age_from, age_to = event.text.split('-')

                                    except Exception as er:

                                        flag = False
                                        send_some_msg(id, 'Неверный формат ввода возраста, попробуй еще раз ', )

                                        break

                                    age_from, age_to = age_from.strip(), age_to.strip()

                                    try:
                                        res['age_from'] = int(age_from)
                                        res['age_to'] = int(age_to)

                                        if res['age_from'] <= res['age_to'] and type(res['age_from']) == int and type(
                                                res['age_to']) == int:

                                            keyboard = VkKeyboard(one_time=True)
                                            keyboard.add_button('Просмотреть результаты', VkKeyboardColor.PRIMARY)
                                            send_some_msg(id, 'Пристегнитесь! Выдаем результаты: ', keyboard=keyboard)

                                            flag = True

                                        else:
                                            flag = False
                                            send_some_msg(id, 'Неверный формат ввода возраста, попробуй еще раз ', )
                                            break

                                    except Exception as er:

                                        flag = False
                                        send_some_msg(id, 'Неверный формат ввода возраста, попробуй еще раз ', )
                                        break

                                    break

                    case 'просмотреть результаты':

                        keyboard = VkKeyboard()

                        keyboard.add_button('Добавить в избранное', VkKeyboardColor.PRIMARY)
                        keyboard.add_button('Следующий профиль', VkKeyboardColor.POSITIVE)
                        keyboard.add_line()
                        keyboard.add_button('Посмотреть избранное', VkKeyboardColor.SECONDARY)
                        keyboard.add_button('Игнорировать профиль', VkKeyboardColor.NEGATIVE)
                        keyboard.add_line()
                        keyboard.add_button('Завершить поиск', VkKeyboardColor.SECONDARY)

                        res['city'] = get_city_id(res)

                        profiles = search_profiles(res)

                        current_profile = add_profiles_photos(next(profiles))

                        add_search_results(id, current_profile, SearchResults)

                        response_to_user = get_next(id, current_profile['result_id'], SearchResults)

                        while check_in_favorite_profiles(id, response_to_user, FavoriteProfiles)[0] \
                                or check_in_blocked_profiles(id, response_to_user, BlockedProfiles)[0]:

                            print('Пользователь', current_profile['first_name'], current_profile['last_name'],
                                  'внесен в "Избраннное" или "Черный список"')

                            current_profile = add_profiles_photos(next(profiles))

                            add_search_results(id, current_profile, SearchResults)

                            response_to_user = get_next(id, current_profile['result_id'], SearchResults)

                        else:

                            send_some_msg(
                                id,
                                response_to_user[0]['1'],
                                attachment=response_to_user[1]['2'],
                                keyboard=keyboard)

                        flag = True

                        while flag:

                            for event in longpool.listen():

                                if event.type == VkEventType.MESSAGE_NEW and event.to_me:

                                    msg = event.text.lower()

                                    match msg:

                                        case 'следующий профиль':

                                            try:
                                                current_profile = add_profiles_photos(next(profiles))

                                            except Exception as er:

                                                keyboard = VkKeyboard()

                                                keyboard.add_button('Посмотреть избранное', VkKeyboardColor.POSITIVE)

                                                keyboard.add_button('Завершить поиск', VkKeyboardColor.SECONDARY)

                                                send_some_msg(id, "По запросу профили закончились, посмотрите "
                                                                  "избранное или начните новый поиск: ",
                                                              keyboard=keyboard)
                                                break

                                            add_search_results(id, current_profile, SearchResults)

                                            response_to_user = get_next(id, current_profile['result_id'], SearchResults)

                                            while check_in_favorite_profiles(id, response_to_user,
                                                                             FavoriteProfiles)[0] \
                                                    or check_in_blocked_profiles(id, response_to_user,
                                                                                 BlockedProfiles)[0]:

                                                print('Пользователя', current_profile['first_name'],
                                                      current_profile['last_name'],
                                                      'внесен в "Избраннное" или "Черный список"')

                                                current_profile = add_profiles_photos(next(profiles))

                                                add_search_results(id, current_profile, SearchResults)

                                                response_to_user = get_next(id, current_profile['result_id'],
                                                                            SearchResults)

                                            else:

                                                send_some_msg(
                                                    id,
                                                    response_to_user[0]['1'],
                                                    attachment=response_to_user[1]['2'],
                                                    keyboard=keyboard)

                                        case 'добавить в избранное':

                                            res_text = add_to_favorite_profiles(response_to_user, FavoriteProfiles)

                                            send_some_msg(
                                                id,
                                                res_text
                                            )

                                            try:
                                                current_profile = add_profiles_photos(next(profiles))

                                            except Exception as er:

                                                keyboard = VkKeyboard()

                                                keyboard.add_button('Посмотреть избранное', VkKeyboardColor.POSITIVE)

                                                keyboard.add_button('Завершить поиск', VkKeyboardColor.SECONDARY)

                                                send_some_msg(id, "По запросу профили закончились, посмотрите "
                                                                  "избранное или начните новый поиск: ",
                                                              keyboard=keyboard)

                                                break

                                            add_search_results(id, current_profile, SearchResults)

                                            response_to_user = get_next(id, current_profile['result_id'], SearchResults)

                                            while check_in_favorite_profiles(id, response_to_user,
                                                                             FavoriteProfiles)[0] \
                                                    or check_in_blocked_profiles(id, response_to_user,
                                                                                 BlockedProfiles)[0]:

                                                print('Пользователя', current_profile['first_name'],
                                                      current_profile['last_name'],
                                                      'внесен в "Избраннное" или "Черный список"')

                                                current_profile = add_profiles_photos(next(profiles))

                                                add_search_results(id, current_profile, SearchResults)

                                                response_to_user = get_next(id, current_profile['result_id'],
                                                                            SearchResults)
                                            else:

                                                send_some_msg(
                                                    id,
                                                    response_to_user[0]['1'],
                                                    attachment=response_to_user[1]['2'],
                                                    keyboard=keyboard)

                                        case 'игнорировать профиль':

                                            res_text = add_to_blocked_profiles(response_to_user, BlockedProfiles)

                                            send_some_msg(
                                                id,
                                                res_text
                                            )

                                            try:
                                                current_profile = add_profiles_photos(next(profiles))

                                            except Exception as er:

                                                keyboard = VkKeyboard()

                                                keyboard.add_button('Посмотреть избранное', VkKeyboardColor.POSITIVE)

                                                keyboard.add_button('Завершить поиск', VkKeyboardColor.SECONDARY)

                                                send_some_msg(id, "По запросу профили закончились, посмотрите "
                                                                  "избранное или начните новый поиск: ",
                                                              keyboard=keyboard)
                                                break

                                            add_search_results(id, current_profile, SearchResults)

                                            response_to_user = get_next(id, current_profile['result_id'], SearchResults)

                                            while check_in_favorite_profiles(id, response_to_user,
                                                                             FavoriteProfiles)[0] \
                                                    or check_in_blocked_profiles(id, response_to_user,
                                                                                 BlockedProfiles)[0]:

                                                print('Пользователя', current_profile['first_name'],
                                                      current_profile['last_name'],
                                                      'внесен в "Избраннное" или "Черный список"')

                                                current_profile = add_profiles_photos(next(profiles))

                                                add_search_results(id, current_profile, SearchResults)

                                                response_to_user = get_next(id, current_profile['result_id'],
                                                                            SearchResults)
                                            else:

                                                send_some_msg(
                                                    id,
                                                    response_to_user[0]['1'],
                                                    attachment=response_to_user[1]['2'],
                                                    keyboard=keyboard)

                                        case 'посмотреть избранное':

                                            favorites_list = show_favorite_profiles(id, FavoriteProfiles)

                                            for favorite in favorites_list:

                                                send_some_msg(
                                                    id,
                                                    favorite[0]['1'],
                                                    attachment=favorite[1]['2'], )

                                        case 'завершить поиск':

                                            res_text = clean_search_results(id, SearchResults)

                                            send_some_msg(
                                                id,
                                                res_text
                                            )

                                            keyboard = VkKeyboard(one_time=True)
                                            keyboard.add_button('Начать поиск', VkKeyboardColor.POSITIVE)

                                            send_some_msg(id, 'Для начала подбора пары нажмите <<Начать поиск>>',
                                                          keyboard=keyboard)

                                            flag = False
                                            break

                    case _:

                        keyboard = VkKeyboard(one_time=True)

                        keyboard.add_button('Начать поиск', VkKeyboardColor.POSITIVE)
                        send_some_msg(id, 'Для начала подбора пары нажмите <<Начать поиск>>', keyboard=keyboard)
