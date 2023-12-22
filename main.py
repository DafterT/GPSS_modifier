import os
import re
import sys

# fix compile
sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w')
import eel
# fix compile


def find_all_names(input_text: str) -> set:
    """
    Ищет все строки, которые начинаются без пробелов (это будут имена)

    :param input_text: Текст
    :return: Множество из имен
    """
    line_with_name_pattern = re.compile(r'^([a-zA-Z0-9_]+).*$')
    names = {'ROOTER'}
    for line in input_text.split('\n'):
        match = line_with_name_pattern.match(line)
        if match and match.group(1).lower() != 'GENERATE'.lower():
            names.add(match.group(1))
    return names


def do_copy(input_text: str, postfix: str) -> str:
    """
    Выполняет копирование добавлением постфикса

    :param input_text: Текст
    :param postfix: Постфикс
    :return: Обновленный текст
    """
    all_names_in_text = find_all_names(input_text)
    names_pattern = re.compile(r'([a-zA-Z0-9_]+)')
    result = ""
    split_names = re.split(names_pattern, input_text)
    for name in split_names:
        result += re.sub(r'\r?\n', '\r\n', name)
        if name in all_names_in_text or 'COLNUM' in name:
            result += postfix
    return result


@eel.expose
def get_text_from_python(input_text: str, postfix: str) -> str:
    """
    Функция для js, которая выполняет обновление текста

    :param input_text: Текст
    :param postfix: Постфикс
    :return: Обновленный текст
    """
    return do_copy(input_text, postfix)


def main():
    """
    Запуск web интерфейса
    """
    eel.init('web')
    eel.start('index.html', size=(700, 700))


if __name__ == '__main__':
    main()
