import os
import re
import sys

# fix compile
sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w')
import eel
# fix compile


def find_all_names(input: str) -> set:
    """
    Ищет все строки, которые начинаются без пробелов (это будут имена)

    :param input: Текст
    :return: Множество из имен
    """
    line_with_name_pattern = re.compile(r'^([a-zA-Z0-9_]+).*$')
    names = {'ROOTER'}
    for line in input.split('\n'):
        match = line_with_name_pattern.match(line)
        if match and match.group(1).lower() != 'GENERATE'.lower():
            names.add(match.group(1))
    return names


def do_copy(input: str, postfix: str) -> str:
    """
    Выполняет копирование добавлением постфикса

    :param input: Текст
    :param postfix: Постфикс
    :return: Обновленный текст
    """
    all_names_in_GPSS = find_all_names(input)
    names_pattern = re.compile(r'([a-zA-Z0-9_]+)')
    result = ""
    split_line = re.split(names_pattern, input)
    for name in split_line:
        result += re.sub(r'\r?\n', '\r\n', name)
        if name in all_names_in_GPSS or 'COLNUM' in name:
            result += postfix
    return result


@eel.expose
def get_text_from_python(text: str, postfix: str) -> str:
    """
    Функция для js, которая выполняет обновление текста

    :param text: Текст
    :param postfix: Постфикс
    :return: Обновленный текст
    """
    return do_copy(text, postfix)


def main():
    """
    Запуск web интерфейса
    """
    eel.init('web')
    eel.start('index.html', size=(700, 700))


if __name__ == '__main__':
    main()
