Консольное приложение "Заметки"
Консольное приложение "Заметки" позволяет создавать, редактировать, просматривать, удалять заметки, а также выводить список всех заметок с возможностью фильтрации и сортировки.

Команды
add: Добавить новую заметку.

Аргументы:
--title: Заголовок заметки (обязательный).
--message: Тело заметки (обязательный).
list: Вывести список всех заметок.

Аргументы:
--date: Фильтрация заметок по определенной дате (необязательный).
--sort: Сортировать заметки по дате (необязательный).
edit: Редактировать существующую заметку.

Аргументы:
--id: Идентификатор заметки для редактирования (обязательный).
--title: Новый заголовок заметки (необязательный).
--message: Новое тело заметки (необязательный).
delete: Удалить существующую заметку.

Аргументы:
--id: Идентификатор заметки для удаления (обязательный).
show: Показать детали определенной заметки.

Аргументы:
--id: Идентификатор заметки для просмотра деталей (обязательный).
Заметки
Заметка содержит уникальный идентификатор (id), заголовок (title), тело (message) и дату/время создания (created_at).
Заметки сохраняются в файл в формате JSON для долгосрочного хранения.
Как использовать
Запустите скрипт с помощью Python: python notes.py [команда] [аргументы].
Выберите одну из доступных команд и предоставьте необходимые аргументы.
Ваши заметки будут сохранены и доступны для просмотра, редактирования и удаления.
Начните управлять своими заметками прямо из командной строки с помощью этого простого и удобного приложения! Удачи!

Список доступных команд:

- `add`: Добавить новую заметку. Требует аргументы `--title` (заголовок заметки) и `--message` (тело заметки).
- `list`: Вывести список всех заметок. Вы можете использовать аргумент `--date` для фильтрации заметок по определенной дате, и `--sort`, чтобы отсортировать заметки по дате.
- `edit`: Редактировать существующую заметку. Требует аргументы `--id` (идентификатор заметки), `--title` (новый заголовок) и `--message` (новое тело заметки).
- `delete`: Удалить существующую заметку. Требует аргумент `--id` (идентификатор заметки).
- `show`: Показать детали определенной заметки. Требует аргумент `--id` (идентификатор заметки).
