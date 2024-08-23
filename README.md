# Форматирование телефонной книги
## Описание
Программа предназначена для обработки телефонной книги в формате CSV. Она читает исходные данные из файла `phonebook_raw.csv`, парсит и объединяет контакты с дубликатами, а затем записывает обработанные данные в новый файл `phonebook_formatted.csv` в папке `formatted_data`.

## Запуск программы
Программа запускается с помощью команды:
```
python main.py
```
Либо можно запустить программу из IDE (например, PyCharm).

## Структура программы
```
root
├── .gitignore
├── README.md
├── requirements.txt
├── log_start.py
├── main.py
├── data
│   └── phonebook_raw.csv
└── modules
    ├── fs_tools
    │   ├── __init__.py
    │   ├── abs_path.py
    │   ├── csv_utils.py
    │   └── make_dir.py
    ├── phonebook
    │   ├── __init__.py
    │   ├── duplicate_remover.py
    │   ├── full_name_parser.py
    │   ├── phone_parser.py
    │   └── phone_patterns.py
    └── validators
        ├── __init__.py
        └── fs_validate.py
```
### Основные папки и файлы
* `.gitignore` - список игнорируемых файлов
* `README.md` - описание проекта
* `requirements.txt` - зависимости проекта
* `log_start.py` - модуль для логирования
* `main.py` - основной файл проекта
* `data` - папка с исходными данными
    * `phonebook_raw.csv` - исходные данные телефонной книги

### Модули и пакеты
* `modules` - основной пакет для работы программы
  * `fs_tools` - подпакет для работы с файлами
    * `__init__.py` - инициализация библиотеки
    * `abs_path.py` - модуль для получения абсолютного пути к файлам
    * `csv_utils.py` - модуль для работы с файлами CSV
    * `make_dir.py` - модуль для создания папки "formatted_data"
  * `phonebook` - подпакет для работы с телефонной книгой
    * `__init__.py` - инициализация библиотеки
    * `duplicate_remover.py` - модуль для объединения контактов с дубликатами
    * `full_name_parser.py` - модуль для парсинга ФИО телефонной книги
    * `phone_parser.py` - модуль для парсинга телефонов телефонной книги
    * `phone_patterns.py` - модуль для хранения регулярных выражений для парсинга телефонов
  * `validators` - подпакет для валидации данных
    * `__init__.py` - инициализация библиотеки
    * `fs_validate.py` - модуль для валидации путей к файлам

## Пример исходных данных
```csv
lastname,firstname,surname,organization,position,phone,email
Усольцев Олег Валентинович,,,ФНС,главный специалист – эксперт отдела взаимодействия с федеральными органами власти Управления налогообложения имущества и доходов физических лиц,+7 (495) 913-04-78,opendata@nalog.ru
Мартиняхин Виталий Геннадьевич,,,ФНС,,+74959130037,
Наркаев,Вячеслав Рифхатович,,ФНС,,8 495-913-0168,
Мартиняхин,Виталий,Геннадьевич,ФНС,cоветник отдела Интернет проектов Управления информационных технологий,,
Лукина Ольга,,Владимировна,Минфин,,+7 (495) 983-36-99 доб. 2926,Olga.Lukina@minfin.ru
Паньшин Алексей Владимирович,,,Минфин,,8(495)748-49-73,1248@minfin.ru
Лагунцов Иван Алексеевич,,,Минфин,,+7 (495) 913-11-11 (доб. 0792),
Лагунцов Иван,,,,,,Ivan.Laguntcov@minfin.ru
Лукина,Оксана,Владимировна,Минфин,,+7 (495) 983-36-99 доб. 2929,OLukina@minfin.ru
```

## Пример обработанных данных
```csv
lastname,firstname,surname,organization,position,phone,email
Усольцев,Олег,Валентинович,ФНС,главный специалист – эксперт отдела взаимодействия с федеральными органами власти Управления налогообложения имущества и доходов физических лиц,+7(495)913-04-78,opendata@nalog.ru
Мартиняхин,Виталий,Геннадьевич,ФНС,cоветник отдела Интернет проектов Управления информационных технологий,+7(495)913-00-37,
Наркаев,Вячеслав,Рифхатович,ФНС,,+7(495)913-01-68,
Лукина,Ольга,Владимировна,Минфин,,+7(495)983-36-99 доб.2926,Olga.Lukina@minfin.ru
Паньшин,Алексей,Владимирович,Минфин,,+7(495)748-49-73,1248@minfin.ru
Лагунцов,Иван,Алексеевич,Минфин,,+7(495)913-11-11 доб.0792,
Лукина,Оксана,Владимировна,Минфин,,+7(495)983-36-99 доб.2929,OLukina@minfin.ru
```

## Требования
- Python 3.x
- Дополнительные библиотеки (указаны в `requirements.txt`)

## Автор
Author: [STORMOZOV](https://github.com/stormozov)   
Telegram: [@s_tormozov](https://t.me/s_tormozov)    
Discord: sergeytormozov  
Email: sergei.tormozow@yandex.ru