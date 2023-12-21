import os
import re
import sys

# fix compile
sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w')
import eel


# fix compile

def find_all_names(input):
    line_with_name_pattern = re.compile(r'^([a-zA-Z0-9_]+).*$')
    names = set()
    for line in input.split('\n'):
        match = line_with_name_pattern.match(line)
        if match:
            names.add(match.group(1))
    return names


def do_copy(input, postfix):
    all_names_in_GPSS = find_all_names(input)
    names_pattern = re.compile(r'([a-zA-Z0-9_]+)')
    result = ""
    split_line = re.split(names_pattern, input)
    for name in split_line:
        result += name.replace('\n', '\r\n').replace('\r\r', '\r')
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
