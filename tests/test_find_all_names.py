from ..code.main import find_all_names

file_path = 'tests/files'


def test_finding_words():
    input_text = 'Text_1\r\n  Text_2\r\nText_3$'
    assert find_all_names(input_text) == {'Text_1', 'Text_3', 'ROOTER'}


def test_fix_generate():
    input_text = 'GENERATE\r\nGENERATE\r\n  GENERATE'
    assert find_all_names(input_text) == {'ROOTER'}


def test_fix_unix():
    input_text = 'Text_1\n  Text_2\nText_3$'
    assert find_all_names(input_text) == {'Text_1', 'Text_3', 'ROOTER'}


def test_real_text_windows():
    with open(f'{file_path}/input_file_win.gpss', 'rb') as file:
        input_text = file.read().decode('utf-8')
    result_set = find_all_names(input_text)
    assert 'GENERATE' not in result_set
    assert len(result_set) == 31


def test_real_text_unix():
    with open(f'{file_path}/input_file_unix.gpss', 'rb') as file:
        input_text = file.read().decode('utf-8')
    result_set = find_all_names(input_text)
    assert 'GENERATE' not in result_set
    assert len(result_set) == 41
