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
    <summary>Алгоритм работы основного скрипта проекта.</summary>

![image](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/img/diagram_1.png)

</details>


<details>
    <summary> Структура БД и описание взаимодействия с ней. </summary>

![image](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/img/%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D0%91%D0%94%20%D0%B8%20%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B.png)

</details>

<details>
    <summary>Шаблон файла с переменными окружения .env для нашего проекта. </summary>
    
[Перейти и скачать файл.](https://github.com/s-alex-developer/github.com_supporting-files/blob/main/Group_work_VKinder/files/.env)

</details>
