from ..code.main import do_copy

file_path = 'tests/files'


def test_copping_win():
    input_text = 'Text_1\r\n  Text_2\r\nText_3$Text_1'
    postfix = '_1'
    expected_output = 'Text_1_1\r\n  Text_2\r\nText_3_1$Text_1_1'
    assert do_copy(input_text, postfix) == expected_output


def test_copping_unix():
    input_text = 'Text_1\n  Text_2\nText_3$Text_1'
    postfix = '_1'
    expected_output = 'Text_1_1\r\n  Text_2\r\nText_3_1$Text_1_1'
    assert do_copy(input_text, postfix) == expected_output


def test_real_text_windows():
    with open(f'{file_path}/input_file_win.gpss', 'rb') as file:
        input_text = file.read().decode('utf-8')
    with open(f'{file_path}/expected_file_win.gpss', 'rb') as file:
        expected_output = file.read().decode('utf-8')
    postfix = '_1'
    assert do_copy(input_text, postfix) == expected_output


def test_real_text_unix():
    with open(f'{file_path}/input_file_unix.gpss', 'rb') as file:
        input_text = file.read().decode('utf-8')
    with open(f'{file_path}/expected_file_unix.gpss', 'rb') as file:
        expected_output = file.read().decode('utf-8')
    postfix = '_1'
    assert do_copy(input_text, postfix) == expected_output
