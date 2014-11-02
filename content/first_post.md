Title: Основны работы со статичным сайтом блогом
Date: Wed Oct 29 22:47:06 MSK 2014
Category: Web
Tags: Python, Blog
Slug: first
Author: dgihangesht
Summary: Учимяс работать с pelican system

# Главный заголовок

## Первоначальная установка и настройка

Для начала нам потребуется создать виртуальное окружение для нашего блог/сайти, точнее не для него а для генератора статических скайтов "pelican"

    :::Bash shell scripts
    virtualenv ~/virtualenv/pelican -p /usr/bin/python2.7 --no-site-packages

Устанавливаем pelicat, markdown

    :::Bash shell scripts
    pip install pelican markdown

Инициализируем наш проект

    :::Bash shell scripts
    pelican-quickstart

Отвечаем на вопросы, тем самым создав директорию с нашим проектом и набором скриптов pelican'a

Далее создадим alias для удобного быстрого старта работы с блогом ( в .bashrc )

    :::Bash shell scripts
    alias Blog="source /home/bezrukov/virtualenv/pelican/bin/activate;\
                cd /home/bezrukov/Desktop/${NAME_PROGECT}/"
    
В директории проекта мы видим примерно следующий набор файлов

    :::Bash shell scripts
    (pelican)bezrukov@demo:~/Desktop/testblog$ tree -d
    .
    ├── cache
    ├── content                 # Диреткория исходных текстовых фалов, формата Markdown
    └── output                  # сгенерированные страницы ( html, css, js, jpg....)
        ├── author
        ├── category
        ├── feeds
        ├── tag
        └── theme
            ├── css
            ├── images
            │   └── icons
            └── js

    12 directories


## Порядок работы с pelican
    

### Написание контента

Пожалуй самая простая вещь, переходим в директорию проекта и далее в поддиректорию content.
Для создания новой статьи просто создаем новый файл с расширением .md.
И в шапку только что созданного файла добавляем

    Title: ${Заголовок статьи/поста}
    Date: ${Текущая дата и время}
    Category: ${Категория поста}
    Tags: Теги характеризующие данный пост
    Slug: URL'ий адресс поста 
    Author: Автор
    Summary: Некоторая описательная часть поста

*В дальнейшем я постараюсь скоратить количество обязательных полей и автоматизировать процесс создания нового файла.*


Текст пишется в формате Markdown
ссылка на синтаксис будет тут;)

### Работа с изображениями

для публикации изображений кладем файл картинки в папку .content/images

и пишим следующее

    \![Alt Text]\({filename}/images/darksidemoon.jpeg)

![Alt Text]({filename}/images/darksidemoon.jpeg)


### Генерация html страниц

убедившись что находитесь в корневом каталоге проекта и virtualenv активирован,
для чего можно вызвать недавно созданный alias - Blog, выполняем команду:
    :::Bash shell scripts
    make html

все необходимые файлы будут сгенерированы в директории output



### Вопрос публикации оставим на потом %)


 * [a link relative to current file](/articles/inna_test)
