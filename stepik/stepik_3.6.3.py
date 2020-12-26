#!/usr/bin/env python3
'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
'''
import requests
url_starts = 'https://stepik.org/media/attachments/course67/3.6.3/699991.txt' 
url_base = 'https://stepik.org/media/attachments/course67/3.6.3/'

url_starts_get = requests.get(url_starts)
next_url = url_starts_get.text

while True:
    print(next_url)
    r = requests.get(url_base + next_url)
    next_url = r.text
    print(r.text)
    if 'We' in r.text:
        break