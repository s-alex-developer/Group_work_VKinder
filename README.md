<details>
    <summary>Инструкция по работе с ботом для пользователей и администраторов сообществ "ВКонтакте".</summary>

### - Администратору сообщества ВК.

**Для начала использования бота в чатах сообщества "ВКонтакте" необходимо:**

1. Произветси настройку сообщества ВК и получить токен доступа, для подключения бота.
2. База данных подключена и настроена, все таблицы созданы. (*На персональном компьютере или удаленном сервере*).
3. Основной скрипт ВК бота должен быть запущен. (*На персональном компьютере или удаленном сервере*).


### - Пошаговая инструкция пользователю ВК бота.
1. Вступаем в сообщество, где реализована возможность использования данного ВК бота и нажимае кнопку "Сообщение":
   
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/README_and_img/user_guide/1.png)

***

2. Вводим любое сообщение для активации работы бота:
   
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/README_and_img/user_guide/2.png)

***

3. Возвращаемся в на главную стринцу своего профила ВК и переходимв раздел "Мессенджер":
   
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/README_and_img/user_guide/3.png)

***
4. Если бот настроен верно и активен, будет предложено нажать на кнопку "Начать поиск".

![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/README_and_img/user_guide/4.png)

***
5. Далее в формате диалога с ботом будет необходимо ответить на три вопроса и указать город, пол кандидатов и их возрастной диапазон.
 
   По этим трём параметрам будет осуществлен подбор профилей пользователей "ВКонтакте", нажимаем на кнопку "Просмотреть результаты", чтобы продолжить.

![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/README_and_img/user_guide/5.png)

***
6. Отлично! Мы получили первый результат поиска: Имя, Фамилию пользователя, ссылку на профиль "ВКонтакте" и три самые популярные фотографии профиля, имеющие наибольшее колличество "лайков.
      
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/README_and_img/user_guide/6.png)

***
7. Кнопка "Следующий профиль" позволит увидеть другие результаты поиска.

![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/README_and_img/user_guide/9.png)

***
8. При помощи кнопок "Добавить в избранное" и "Просмотреть избранное" мы можем сохранять и просматривать заинтересовавшие нас профили.

   После завершения текущего сеанса поиска избранные профили буду сохранены и Вы сможете вернуться к их просмотру в будущем.
   
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/README_and_img/user_guide/7.png)
***

9. Кнопка "Просмотреть избранное".

![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/README_and_img/user_guide/10.png)
***

10. Профили, которые нам показались не интересными можно внести "черный список" нажатием кнопки "Игнорировать профиль".

![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/README_and_img/user_guide/8.png)
***

11. Если Вы уже отметили какой-то профиль как "Избранный" или "Игнорируемый", то при запуске следующего сеанса поиска этот профиль не попадет в результаты и повторно показан не будет.

    После нажатия кнопок "Добавить в избранное" или "Игнорировать профиль" автоматически будет загружен и показан следующий результат поиска.

***
12. Нажатие кнопки "Завершить поиск" прекращает текущую сессию поиска, удаляет не сохраненные результаты поиска из памяти и возвращает нас в начало беседы с ВК ботом.
    
![](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/README_and_img/user_guide/11.png)

***
## *Удачных поисков! Кто ищет, тот обязательно найдет!!!*

</details>

<details>
    <summary>Визуализация алгоритма работы проекта "Vkinder".</summary>

![image](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/README_and_img/diagram_1.png)

</details>


<details>
    <summary> Структура БД и основная информация. </summary>

![image](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/README_and_img/%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D0%91%D0%94%20%D0%B8%20%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B.png)

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
    <summary>Запуск ВК бота и основная логика его работы.</summary>
    
### Для запуска бота на PC необходимо (ОС Windows):

1. Клонировать данный репозиторий: `git clone git@github.com:s-alex-developer/Group_work_VKinder.git`
   
2. Из файла **requirements.txt** установить виртуальное окружение: `pip install -r requirements.txt`

3. Создать базу данных, например: **VKinder_db** (_имя по умолчанию в файле **.env**_)
   
4. Заполнить файл с переменными окружения **.env** - шаблон для данного проекта доступен для скачивания ниже.

6. Для запуска ВК бота будет необходимо:
   - Получить ключ доступа к сообществу, от имени которой будет общаться бот.
   - Получить токен разработчика "ВКонтакте" [dev.vk](https://dev.vk.com/)

7. Создать необходимые для работы бота таблицы в базе данных:
   
   * Для этого нужно запустить модуль `db_models.py`
   * При первом запуске модуля `db_models.py` комментируем вызов функции `#delete_tables()`, чтобы избежать ошибки при попытке удалить несуществующие таблицы в БД. (116-ая строка модуля).
   * Последующие запуски модуля в процессе тестирования и проверки необходимо выполнять с функцией `delete_tables()`

### Логика работы ВК бота и последовательность выполняемых операций:

1. В процессе общения ВК бота и пользователя мы получаем данные, которые будут составлять основные параметры поиска профилей пользователей СС "ВКонтакте":
   - Город
   - Пол
   - Возрастной диапазон

2. Реализована проверка на корректность предоставляемых данных, нельзя передать в запрос несуществующий город или возрастной диапазон, если он не соответсвует предложенному шаблону.

3. Если при вводе данных пользователю допустил ошибку, будет предложено повторить попытку ввода, пока введенные данные не будут корректными.

4. Общение с пользователем ВК реализовано функцией `send_some_msg` (модуль **VKinder_bot.py**), каждый раз в процесе работы скрипта ВК бота, отправляя информационные/навигационные сообщения, результаты поиска или данные из БД текущему пользователю, мы будет выполнять эти операцию при помощи данной функции.

5. Вспомогательные функции `get_user_name_from_vk_id` и `cleans_all_tag_from_str` (модуль **VKinder_bot.py**) - позволяют используя id пользователся, который ведет общение с ботом, получить его имя и использовать в процессе дальнейшего общения в чате сообщества.

6. В результате предварительного этапа общения пользователя и ВК бота у нас формируется следующий формат данных для запроса:

   ```python
   {'user_id': ..., 'city': type_str, 'sex': ..., 'age_from': ..., 'age_to': ...}
   ```

7. Данный словарь мы передаем в качестве аргумента в функцию `get_city_id` (модуль **vk_api.py**), чтобы заменить название города, на его id в БД "ВКонтакте".
   Это будет необходимо для последующего запроса через VK API.

8. Теперь данные для запроса выглядят следующим образом:
   
    ```python
   {'user_id': ..., 'city': type_int, 'sex': ..., 'age_from': ..., 'age_to': ...}
    ```
    
9. Обновленный словарь мы передаем в функцию `search_profiles` (модуль **vk_api.py**)
    - Данная функция выполняет `get`-запросы через `VK API` и мы получаем данные профилей, которые подходят под критерии подбора, заданные пользователем ВК.
    - Дополнительно мы установили в качестве параметров поиска **"открытый профиль"** и **"наличие хотя бы одной фотографии в профиле"**.
    - В результате выполнения и обработки запросов мы получаем список словарей, имеющий следующую структуру:

      ```python
      {'first_name': ...,
      'last_name': ...,
      'photo_href_1': None,
      'photo_href_2': None,
      'photo_href_3': None,
      'result_id': ...,
      'user_id': ...,
      'vk_profile_href': ...}
      ```
    - Так же внутри данной функции реализован генератор.

10. Далее при помощи функции `add_profiles_photos` (модуль **vk_api.py**), мы дополняем полученные ранее данные тремя самыми популярным по колличеству "лайков" фотографиями.
    
    - Данная функция принимает в качестве аргумента результаты работы функции `search_profiles`
      
    - Используя возможности генератора, реализованные в функции `search_profiles` за один вызов функции `add_profiles_photos` мы получаем и наполняем фотографиями все один профиль, что ускоряет работу и процесс выдачи очередного результат поиска пользователю ВК.

11. На данном этапе нами получены все данные, необходимые для отправки пользователю ВК в качестве результата поиска:

    ```python
    {'first_name': 'Жанна',
     'last_name': 'Мидлтон',
     'photo_href_1': 'photo441843197_457239518',
     'photo_href_2': None,
     'photo_href_3': None,
     'result_id': 1,
     'user_id': 441843197,
     'vk_profile_href': 'https://vk.com/id441843197'}
     ```
12. При помощи функции `add_to_favorite_profiles` (модуль **db_func.py**) производим запись текущего/очередного результата поиска в таблицу БД `"search_results"`.
    
    - Все данные в таблице `"search_results"` храняться только для текущей сессии поиска и будут автоматичесски удалены после ее завершения.
      
13. Далее функцией `get_next` (модуль **db_func.py**) мы производит извлечение текущего результата поиска из таблицы `"search_results"` и приводим данные в пригодный формат, для отправки пользователю ВК.
    
      - В результате работы функции `get_next` мы получаем список словарей:

         ```python
         [
            {'1': f'{c.first_name} {c.last_name} \n{c.vk_profile_href}'},
            {'2': f'{c.photo_href_1},{c.photo_href_2},{c.photo_href_3}'},
            {'user_id': f'{user_id}', 'vk_profile_href': f'{c.vk_profile_href}', 'first_name': f'{c.first_name}',
             'last_name': f'{c.last_name}', 'photo_href_1': f'{c.photo_href_1}', 'photo_href_2': f'{c.photo_href_2}',
             'photo_href_3': f'{c.photo_href_3}'}
         ]
         ```
      - Первые два элемента списка с индексами 0 и 1 используются для формирования и отправки очередного результата поиска пользователю ВК бота.
     
      - Третий элемент списка с индексом 2 содержит все необходимые данные в установленном формате, для записи текущего результата поиска
     в таблицы `'favorite_profiles'` и `'blocked_profiles'`, **"Избранные"** и **"Игнорируемые"** пользователи соответственно.
     
14. Каждый раз перед отправкой очередного результата поиска пользователю ВК производится проверка:

    - Функция `check_in_favorite_profiles` (модуль **db_func.py**) - проверяет наличие текущего пользователя в таблице БД `'favorite_profiles'` - **"Избранные профили"**.
      
    - Функция `check_in_blocked_profiles` (модуль **db_func.py**) - проверяет наличие текущего пользователя в таблице БД `'blocked_profiles'` - **"Игнорируемые профили"**.
      
    - Если профиль был ранее добавлен текущим пользователем ВК в **"Избранные профили"** или **"Игнорируемые профили"** то повторно показан он не будет.
      
    - Автоматически будет вызвана функция `get_next` (модуль **db_func.py**) и мы перейдем к следующему результату поиска.
      
    - Проверка будет производится до тех пор, пока мы не дойдем до профиля, который не никак ранее не был отмечен текущим пользователем ВК.

15. Просматриваемый в данный момент пользователем ВК результат поиска, может быть добавлен в **"Избранные профили"** или **"Игнорируемые профили"**:

    - Функция `add_to_favorite_profiles` (модуль **db_func.py**) - добавляет текущий результат поиска в таблицу БД `"favorite_profiles"` - **"Избранные профили"**.
      
    - Функция `add_to_blocked_profiles` (модуль **db_func.py**) - добавляет текущий результат поиска в таблицу БД `"blocked_profiles"` - **"Игнорируемые профили"**.
   
    - По завершению работы функции `add_to_favorite_profiles` или `add_to_blocked_profiles` автоматически будет вызвана функция `get_next` (модуль **db_func.py**) и мы перейдем к следующему результату поиска.

16. Функция `show_favorite_profiles` (модуль **db_func.py**) - выгружает из таблицы БД `"favorite_profiles"` и отправляет текущему пользователю ВК сохраненные ранее результаты поиска, отмеченные им как **"Избранные профили"**.

17. При завершении текущей сессии поиска пользователем ВК нажатием кнопки **"Завершить поиск"**, вызывается функция `cleans_search_results` (модуль **db_func.py**), которая производит удаление всех записанных в рамках данной сессии результатов поиска из таблицы БД `"search_profiles"`.

18. Все записанные данные в таблицах `'favorite_profiles'` и `'blocked_profiles'`, **"Избранные"** и **"Игнорируемые"** профили по завершении текущей сессии поиска остаются на хранении в базе данных.

19. Функции `create_engine` и `create_session` (модуль **db_func.py**) являются вспомогательными, первая создает "движок", а вторая, принимая "движок" в качестве аргумента, открывает рабочую сессию с базой данных для получения, внесени и обновления данных.
    </details>
    
<details>
    <summary>Шаблон файла с переменными окружения .env для нашего проекта. </summary>
    
[Перейти и скачать файл.](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/files/.env)

</details>
