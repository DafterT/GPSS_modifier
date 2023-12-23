<p align="center">
<img src="https://github.com/DafterT/GPSS_modifier/actions/workflows/tests.yaml/badge.svg">
<img src="https://img.shields.io/badge/made%20by-Dafter-orange.svg">
<img src="https://img.shields.io/github/license/DafterT/GPSS_modifier">
<img src="https://img.shields.io/github/last-commit/DafterT/GPSS_modifier">
</p>

# Задача
Существует генератор тектовых файлов формата gpss, 
необходимо модифицировать текстовый файл таким образом, 
чтоб к всем именам добавить постфикс, выбранный пользователем.
# Реализация
Для реализации был создан веб интерфейс, используя `html, css, js`.

Этот интерфейс вызывается, используя python и библиотеку `eel`.

Сама реализация анализа написана так же на python.
# Приложение
Вся кодовая составляющая находится в папке `code`. Веб интерфейс
находится в папке `code/web`. 

Так же были реализованы юнит-тесты, их можно найти в папке `tests`.
Они запускаются автоматически при пуше комита в main.
# Компиляция
Для компиляции используется python версии 3.8.10, для большей совместимости
(windows 8+).

Для сборки используется pyinstaller, поэтому клонируем его и пересобираем:
```commandline
git clone https://github.com/pyinstaller/pyinstaller  
cd pyinstaller
cd bootloader
python ./waf distclean all
cd ..
pip install . 
```
Для сборки проекта используется следующая команда (в папке code):
```commandline
python -m eel main.py ./web --onefile --icon=img/icon.ico --noconsole
```
На выходе получается файл `/dist/main.exe`.