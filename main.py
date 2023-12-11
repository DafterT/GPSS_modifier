import re

import eel


def find_all_names(gpss):
    line_with_name_pattern = re.compile(r'^([a-zA-Z0-9_]+).*$')
    names = set()
    for line in gpss:
        match = line_with_name_pattern.match(line)
        if match:
            names.add(match.group(1))
    return names


def do_copy(input, postfix):
    input_split = input.split('\n')
    all_names_in_GPSS = find_all_names(input_split)
    names_pattern = re.compile(r'([a-zA-Z0-9_]+)')
    result = ""
    for line in input_split:
        split_line = re.split(names_pattern, line)
        for name in split_line:
            result += name
            if name in all_names_in_GPSS or 'COLNUM' in name or 'ROOTER' in name:
                result += postfix
    return result


@eel.expose
def get_text_from_python(text: str, postfix: str) -> str:
    return do_copy(text, postfix)


def main():
    eel.init('web')
    eel.start('index.html', size=(700, 700))


if __name__ == '__main__':
    main()
