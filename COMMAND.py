"""
Створити віртуальне оточення, де другий venv це назва оточення (може бути будь яка)
python -m venv venv


перейти до директорії
cd E:\PycharmProjects\Django_lessons\djsite


Активувати віртуальне оточення
.\venv\Scripts\activate


Деактивувати віртуальне оточення
deactivate
"""

"""
Перейти до директорії сайту
cd testsite

Запускаєм сервер
python manage.py runserver

Завершити роботу серверу
Ctrl + Break / Ctrl + C

Інший порт 
python manage.py runserver 4000

Інша адреса
python manage.py runserver 192.168.1.1:4000
"""

"""
Створити новий додаток
python manage.py startapp women

Потім додати його в settings.py

Потім додати паттерн в urls.py

"""






"""
=======================================================================================================================
Як полагодити запуск віртуального оточення якщо PowerShell блокує його.
Ця помилка пов'язана з обмеженнями безпеки PowerShell, які не дозволяють виконувати сценарії PowerShell.
 Щоб вирішити цю проблему, потрібно змінити політику виконання PowerShell, дозволяючи виконання сценаріїв PowerShell.

Щоб змінити політику виконання PowerShell, відкрийте PowerShell з правами адміністратора і введіть команду
 Set-ExecutionPolicy RemoteSigned. Після цього вам буде запропоновано підтвердити зміну політики виконання,
  введіть "Y" і натисніть "Enter".

Це дозволить виконувати сценарії PowerShell з локальних дисков та з довірених віддалених джерел.

Після того, як ви змінили політику виконання, спробуйте знову активувати свій віртуальний середовище
 Python за допомогою команди .\venv\Scripts\activate відповідно до вашого шляху.
"""