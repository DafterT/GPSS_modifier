import logging
import msvcrt
import os
import re


def find_all_names(gpss):
    line_with_name_pattern = re.compile(r'^([a-zA-Z0-9_]+).*$')
    names = {'COLNUM', 'ROOTER'}
    for line in gpss:
        match = line_with_name_pattern.match(line)
        if match:
            names.add(match.group(1))
    return names


def do_copy(GPSS_out, GPSS_in, postfix):
    all_names_in_GPSS = find_all_names(GPSS_in)
    GPSS_in.seek(0)  # go to start of line
    logging.debug(f'Found names: {all_names_in_GPSS}')
    names_pattern = re.compile(r'([a-zA-Z0-9_]+)')
    for line in GPSS_in:
        split_line = re.split(names_pattern, line)
        logging.debug(f'Split line: {split_line}')
        for name in split_line:
            GPSS_out.write(name if name not in all_names_in_GPSS else (name + postfix))
    logging.debug(f'File created!')


def main():
    # Enter paths
    path_to_gpss = input("Enter path to GPSS file: ")
    while not os.path.isfile(path_to_gpss):
        path_to_gpss = input("File not found, please try again!\nEnter path to GPSS file: ")
    path_to_new_gpss = input("Enter name for new GPSS file: ")
    # Enter postfix
    postfix_pattern = re.compile(r'^[a-zA-Z0-9_]+$')
    postfix = input("Enter postfix: ")
    while not postfix_pattern.match(postfix):
        input("Incorrect postfix, try again.\nEnter postfix: ")
    # Copy
    try:
        logging.debug(f'Entered path to pgss: {path_to_gpss}')
        logging.debug(f'Entered path to new pgss: {path_to_new_gpss}')
        with open(path_to_new_gpss, 'w') as GPSS_out:
            with open(path_to_gpss, 'r') as GPSS_in:
                do_copy(GPSS_out, GPSS_in, postfix)
        print(f'File created in: {os.path.abspath(path_to_new_gpss)}\n')
    except FileNotFoundError:
        print('File not found!')
        logging.critical('Exception: FileNotFoundError.')
    except IOError as e:
        print(f'IOError occurred: {e}')
        logging.critical(f'Exception: IOError {e}.')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        logging.critical(f'Exception: Exception {e}.')
    print('Press eny key to close console...')
    msvcrt.getch()


if __name__ == '__main__':
    logging.basicConfig(filename='./logs.log', encoding='utf-8', level=logging.DEBUG)
    main()
