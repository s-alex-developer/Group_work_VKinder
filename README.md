<details>
    <summary>Инструкция по работе с ботом для пользователей и администраторов сообществ "ВКонтакте".</summary>

### - Администратору сообщества ВК.

**Для начала использования бота в чатах сообщества "ВКонтакте" необходимо:**

1. Произветси настройку сообщества ВК и получить токен доступа, для подключения бота.
2. База данных подключена и настроена, все таблицы созданы. (*На персональном компьютере или удаленном сервере*).
3. Основной скрипт ВК бота должен быть запущен. (*На персональном компьютере или удаленном сервере*).


### - Пошаговая инструкция пользователю ВК бота.
1. Вступаем в сообщество, где реализована возможность использования данного ВК бота и нажимае кнопку "Сообщение":
   
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/img/user_guide/1.png)

***

2. Вводим любое сообщение для активации работы бота:
   
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/img/user_guide/2.png)

***

3. Возвращаемся в на главную стринцу своего профила ВК и переходимв раздел "Мессенджер":
   
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/img/user_guide/3.png)

***
4. Если бот настроен верно и активен, будет предложено нажать на кнопку "Начать поиск".

![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/img/user_guide/4.png)

***
5. Далее в формате диалога с ботом будет необходимо ответить на три вопроса и указать город, пол кандидатов и их возрастной диапазон.
 
   По этим трём параметрам будет осуществлен подбор профилей пользователей "ВКонтакте", нажимаем на кнопку "Просмотреть результаты", чтобы продолжить.

![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/img/user_guide/5.png)

***
6. Отлично! Мы получили первый результат поиска: Имя, Фамилию пользователя, ссылку на профиль "ВКонтакте" и три самые популярные фотографии профиля, имеющие наибольшее колличество "лайков.
      
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/img/user_guide/6.png)

***
7. Кнопка "Следующий профиль" позволит увидеть другие результаты поиска.

![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/img/user_guide/9.png)

***
8. При помощи кнопок "Добавить в избранное" и "Просмотреть избранное" мы можем сохранять и просматривать заинтересовавшие нас профили.

   После завершения текущего сеанса поиска избранные профили буду сохранены и Вы сможете вернуться к их просмотру в будущем.
   
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/img/user_guide/7.png)
***

9. Кнопка "Просмотреть избранное".

![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/img/user_guide/10.png)
***

10. Профили, которые нам показались не интересными можно внести "черный список" нажатием кнопки "Игнорировать профиль".

![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/img/user_guide/8.png)
***

11. Если Вы уже отметили какой-то профиль как "Избранный" или "Игнорируемый", то при запуске следующего сеанса поиска этот профиль не попадет в результаты и повторно показан не будет.

    После нажатия кнопок "Добавить в избранное" или "Игнорировать профиль" автоматически будет загружен и показан следующий результат поиска.

***
12. Нажатие кнопки "Завершить поиск" прекращает текущую сессию поиска, удаляет не сохраненные результаты поиска из памяти и возвращает нас в начало беседы с ВК ботом.
    
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/img/user_guide/11.png)

***
## *Удачных поисков! Кто ищет, тот обязательно найдет!!!*

</details>

<details>
    <summary>Визуализация алгоритма работы проекта "Vkinder".</summary>

![image](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/img/diagram_1.png)

</details>


<details>
    <summary> Структура БД и основная информация. </summary>

![image](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/img/%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D0%91%D0%94%20%D0%B8%20%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B.png)

</details>

<details>
    <summary> Основные файлы проекта "VKinder". </summary>

## Описание модулей и функций:

1 **"Vkinder_bot.py"** - основной модуль проекта, содержащий всю логику работы ВК бота.

    Взаимодействует с модулями:

        1. db_models.py - содержит классы и методы для создания таблиц БД.

        2. db_func.py - содержит функции для работы с Базой данных.

        3. vk_api содержит функции для взаимодействия с VK API.

  ### /application/data_base/...
        
  2. Модуль **"db_models.py"** содержит классы и методы для создания таблиц БД.

    Для создания таблиц в БД необходимо запустить этот модуль и заполнить файл с переменными окружения.

    Состав модуля:

        1. class SearchResults - описывает модель создания таблицы БД "search_results", "Результаты поиска.

        2. class FavoriteProfiles - описывает модель создания таблицы БД 'favorite_profiles', "Избранные профили."

        3. class BlockedProfiles - описывает модель создания таблицы БД 'blocked_profiles', "Игнорируемые профили."

        4. Метод create_tables - создает таблицы в БД используя модели описанные в этом модуле.

        5. Метод delete_tables - удаляет все таблицы БД, созданные при помощи этого модуля.
        
  3. Модуль **"db_func.py"** содержит функции для работы с Базой данных.

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
            
### /application/vk_api/...
4. Модуль **"vk_api.py"** содержит функции для взаимодействия с VK API.

    ```Состав модуля:

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

</details>

<details>
    <summary>Шаблон файла с переменными окружения .env для нашего проекта. </summary>
    
[Перейти и скачать файл.](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/files/.env)

</details>
