# Code-courses-Platform

# 📑 Страницы

## Для всех пользователей

- ### Главная страница
- ### Все курсы
  - **Поиск**
  - **Фильтрация**
  - **Сортировка**
- ### Один курс
  - **Описание курса**
  - **Просмотр прогресса**
  - **Просмотр заданий и их завершенность**
  - **Возможность лайкнуть**
  - **Возможность поделиться**
  - **Отзывы и возможность оставить свой отзыв**
- ### Задание
  - **Задание**
  - **Список тем и заданий**
  - **Комментарии и возможность оставить свой комментарий**
  - **Возможность поделиться**
  - **Возможность лайкать**

- ### Все статьи
  - **Поиск**
  - **Фильтрация**
  - **Сортировка**
- ### Одна статья
  - **Статья**
  - **Возможность оставить реакцию**
  - **Возможность поделиться**
  - **Комментарии и возможность оставить свой комментарий**
  - **Похожие статьи**

- ### Регистрация / Вход в аккаунт
- ### Восстановление пароля по email
- ### Пользовательский профиль
  - **Главная информация**
  - **Детальная информация**
  - **Опыт прохождения других курсов**
  - **Сертификаты**
  - **Комментарии**


## Для зарегистрированных пользователей

- ### Страница быстрого доступа (dashboard)
  - **Топ 3 последних курса с погрессом**
- ### Настройки
- ### Лайкнутые курсы и статьи

## Для админов

- Создание курса
- Обновление курса
- Просмотр статистики и управление отзывами
- Панель для управления темами и заданиями
- Создание нового задания
- Обновление информации задания
- Просмотр ответов на задания и кол-во попыток (если писменное)
- Просмотр статистики и комментариев

- Создании статьи
- Обновление статьи
- Просмотр статистики и комментариев к статье

- Управление пользователями
  - **Поиск**
  - **Фильтрация**
  - **Сортировка**
  - **Блокировка**

## API

### Курс

- [x] Список курсов с возможностями поиска, сортировки и фильтрации по тэгам:  `GET /api/courses?q=;order_by_data=;filter_by_tag=;`
- [ ] Создание нового курса: `POST /api/courses/`
- [x] Показ информации курса по идентификатору: `GET /api/courses/:id/`
- [ ] Обновление информации курса по идентификатору: `PUT /api/courses/:id/`
- [ ] Удаление курса по идентификатору: `DELETE /api/courses/:id/`
- [x] Добавление и удаление лайка к курсу: `PATCH /api/courses/:id/like/`
- [x] Регистрация и удаление пользователя к курсу: `PATCH /api/courses/:id/user/`
- [x] Вывод всех отзывов к курсу: `GET /api/courses/:id/reviews/`
- [x] Создание нового отзыва к курсу: `POST /api/courses/:id/reviews`
- [x] Удаление отзыва `DELETE /api/courses/reviews/:id/delete/`

## Тема

- [x] Вывод всех тем с заданиями: `GET /api/courses/:id/titles/`
- [x] Создание новой темы: `POST /api/courses/:id/titles/`
- [x] Удаление темы: `DELETE /api/courses/titles/:title_id/`
- [x] Обновление названия темы: `PATCH /api/courses/titles/:title_id/update-title/`
- [x] Обновление типа публичности темы: `PATCH /api/courses/titles/:title_id/update-public/`
- [ ] Возможность менять темы местами: `PATCH /api/courses/:id/titles/:first_title_id/:second_title_id`

## Задание

- [x] Создание нового задания: `POST /api/courses/titles/:id/tasks/`
- [x] Вывод задания: `GET /api/courses/:id/titles/tasks/:task_id/`
- [x] Обновление задания: `PUT /api/courses/:id/titles/tasks/:task_id/`
- [x] Удаление задания: `DELETE /api/courses/:id/titles/tasks/:task_id/`
- [ ] Возможность менять задания местами: `PATCH /api/courses/:id/titles/tasks/:first_task_id/:second_task_id`
- [x] Добавление / удаление опыта к заданию: `PATCH /api/courses/:id/titles/tasks/:task_id/experience/`
- [x] Добавление / удаление закладки к заданию: `PATCH /api/courses/:id/titles/tasks/:task_id/bookmark/`

## Комментарии к заданию

- [x] Показ всех комментариев: `GET /api/courses/titles/tasks/:task_id/comments/`
- [x] Создание нового комментария: `POST /api/courses/titles/tasks/:task_id/comments/`
- [ ] Обновление текста комментария: `PATCH /api/courses/titles/tasks/:task_id/comments/:comment_id/text`
- [x] Удаление комментария: `DELETE /api/courses/titles/tasks/:task_id/comments/:comment_id/`
- [x] Добавление / Удаление лайка комментариям: `PATCH /api/courses/titles/tasks/:task_id/comments/:comment_id/react/`
- [x] Оставление жалобы на комментарий: `POST /api/courses/titles/tasks/:task_id/comments/:comment_id/complaint/`

## Пользователь

- [ ] Вывод главной информации о пользователе: `GET /api/user/:username/`
- [ ] Вывод подробной информации о пользователе: `GET /api/user/:username/detail/`
- [ ] Вывод курсов и процент прогресса в них: `GET /api/user/:username/experience/`
- [ ] Вывод сертификатов за окончание курсов: `GET /api/user/:username/certificates/`
- [ ] Вывод лайкнутых курсов: `GET /api/user/:username/favorites/`
- [ ] Вывод списка достижений пользователя: `GET /api/user/:username/achivements/`
- [ ] Блокировка пользователя: `PATCH /api/user/:username/block/`
- [ ] Показ всех пользователей с поиском и фильтрацией: `GET /api/users/?q=;`

## Достижения

- [ ] Вывод всех достижений: `GET /api/achivements/`
- [ ] Создание нового достижения: `POST /api/achivements/`
- [ ] Обновление достижения: `PUT /api/achivements/:id/`
- [ ] Удаление достижения: `DELETE /api/achivements/:id/`
- [ ] Добавление / удаление пользователя к достижению: `PATCH /api/achivements/:id/users/`


# Design
https://www.figma.com/file/z40JQFsGp7kKiv0B9GWfAU/Code-Course-Platform?type=design&node-id=0%3A1&mode=design&t=54RAnWCSfzZA6MU2-1

![image](https://github.com/Jaswine/Code-Cources-Platform/assets/82625479/0649ffe6-8cd3-4fee-8068-e0365d3d4d6d)

![image](https://github.com/Jaswine/Code-Cources-Platform/assets/82625479/c5d652a0-263c-4060-a0ca-da6436cb53ec)

![image](https://github.com/Jaswine/Code-Cources-Platform/assets/82625479/5b5e0cf4-1c66-49ab-8cb0-2799e9ceb99b)

![image](https://github.com/Jaswine/Code-Cources-Platform/assets/82625479/7bbcb75c-f8cd-4880-892a-754f42b0966b)

![image](https://github.com/Jaswine/Code-Cources-Platform/assets/82625479/5781680c-6a73-4509-8002-45357531568c)

![image](https://github.com/Jaswine/Code-Cources-Platform/assets/82625479/b72fbfb1-a0ca-4303-ac32-d4d0370f8448)


<hr>

![image](https://user-images.githubusercontent.com/82625479/217524313-28219893-c564-4d65-b180-a6193f1c0feb.png)

![image](https://user-images.githubusercontent.com/82625479/217524459-f0536502-d6c9-4257-9a23-65f6464c94b4.png)

![image](https://user-images.githubusercontent.com/82625479/218445573-24e2c1c3-ada1-4606-b5f8-632efa8109fa.png)

![image](https://user-images.githubusercontent.com/82625479/218445653-3c2dc876-0660-41b9-baad-63adcfef92ac.png)

![image](https://user-images.githubusercontent.com/82625479/218446163-f4652040-080f-4f02-8c71-e840249a6e90.png)

![image](https://user-images.githubusercontent.com/82625479/219077776-46f33c78-f005-42f3-aba7-ddbf0e06f244.png)

![image](https://user-images.githubusercontent.com/82625479/219078002-159f7e76-0ed4-462d-a673-db365749d6fb.png)

![image](https://user-images.githubusercontent.com/82625479/219078174-fb3b9844-08b5-4c42-95bb-5eab448e0766.png)



<h3>OLD DESIGN: </h3>

![image](https://user-images.githubusercontent.com/82625479/209466501-e3a7cb03-a77f-4922-9bcd-5611b51c7eea.png)

![image](https://user-images.githubusercontent.com/82625479/209466521-e06ab43a-bd29-4d5f-b692-ee25b50982f1.png)

![image](https://user-images.githubusercontent.com/82625479/209466424-26344cc6-e6ce-4f03-ad0a-fb5ffaec5152.png)

![image](https://user-images.githubusercontent.com/82625479/209559638-2a62a108-792b-4c05-ab77-d0739a281fd9.png)

![image](https://user-images.githubusercontent.com/82625479/210534097-eac8f194-0b18-409b-a7de-ce689c83fc1d.png)

![image](https://user-images.githubusercontent.com/82625479/210534269-2b2e75a9-7149-4243-8b56-b13ac4f78723.png)

![image](https://user-images.githubusercontent.com/82625479/212683727-2654380a-ec57-4cbf-acb4-58ef0c4febf6.png)

![image](https://user-images.githubusercontent.com/82625479/212683879-ad3b76be-638a-4157-85d4-68cdc42e0646.png)


