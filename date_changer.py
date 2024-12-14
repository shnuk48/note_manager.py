# Запрашиваем информацию у пользователя
username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")

# Форматируем даты для вывода
temp_created_date = format_date(created_date)
temp_issue_date = format_date(issue_date)

# Выводим информацию о заметке
print(f"Пользователь: {username}")
print(f"Заголовок: {title}")
print(f"Описание: {content}")
print(f"Статус: {status}")
print(f"Дата создания: {temp_created_date}")
print(f"Дата истечения: {temp_issue_date}")