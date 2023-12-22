import os
import unittest

from code.main import find_all_names, do_copy


class TestFindAllNames(unittest.TestCase):
    def setUp(self) -> None:
        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'files'))

    def test_finding_words(self):
        input_text = 'Text_1\r\n  Text_2\r\nText_3$'
        self.assertEqual(find_all_names(input_text), {'Text_1', 'Text_3', 'ROOTER'})

    def test_fix_generate(self):
        input_text = 'GENERATE\r\nGENERATE\r\n  GENERATE'
        self.assertEqual(find_all_names(input_text), {'ROOTER'})

    def test_fix_unix(self):
        input_text = 'Text_1\n  Text_2\nText_3$'
        self.assertEqual(find_all_names(input_text), {'Text_1', 'Text_3', 'ROOTER'})

    def test_real_text_windows(self):
        with open(f'{self.file_path}/input_file_win.gpss', 'rb') as file:
            input_text = file.read().decode('utf-8')
        result_set = find_all_names(input_text)
        self.assertNotIn('GENERATE', result_set)
        self.assertEqual(len(result_set), 31)

    def test_real_text_unix(self):
        with open(f'{self.file_path}/input_file_unix.gpss', 'rb') as file:
            input_text = file.read().decode('utf-8')
        result_set = find_all_names(input_text)
        self.assertNotIn('GENERATE', result_set)
        self.assertEqual(len(result_set), 41)


class TestDoCopy(unittest.TestCase):
    def setUp(self) -> None:
        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'files'))

    def test_copping_win(self):
        input_text = 'Text_1\r\n  Text_2\r\nText_3$Text_1'
        postfix = '_1'
        expected_output = 'Text_1_1\r\n  Text_2\r\nText_3_1$Text_1_1'
        self.assertEqual(do_copy(input_text, postfix), expected_output)

    def test_copping_unix(self):
        input_text = 'Text_1\n  Text_2\nText_3$Text_1'
        postfix = '_1'
        expected_output = 'Text_1_1\r\n  Text_2\r\nText_3_1$Text_1_1'
        self.assertEqual(do_copy(input_text, postfix), expected_output)

    def test_real_text_windows(self):
        with open(f'{self.file_path}/input_file_win.gpss', 'rb') as file:
            input_text = file.read().decode('utf-8')
        with open(f'{self.file_path}/expected_file_win.gpss', 'rb') as file:
            expected_output = file.read().decode('utf-8')
        self.assertEqual(do_copy(input_text, '_1'), expected_output)

    def test_real_text_unix(self):
        with open(f'{self.file_path}/input_file_unix.gpss', 'rb') as file:
            input_text = file.read().decode('utf-8')
        with open(f'{self.file_path}/expected_file_unix.gpss', 'rb') as file:
            expected_output = file.read().decode('utf-8')
        self.assertEqual(do_copy(input_text, '_1'), 0)


if __name__ == '__main__':
    unittest.main()
