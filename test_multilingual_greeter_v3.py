from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import multilingual_greeter_v2 as mg




class MultilingualGreeterV2Test(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_language_options(self, stdout_mock):
        languages = {
            1: "English",
            2: "Spanish",
            3: "Portuguese"
        }

        expected = "Please choose a language: \n" \
                   "1: English\n" \
                   "2: Spanish\n" \
                   "3: Portuguese\n"

        mg.print_language_options(languages)
        self.assertEqual(expected, stdout_mock.getvalue())

    @patch('builtins.input', return_value="1")
    def test_language_input(self, user_input):
        actual = mg.language_input()
        self.assertEqual(1, actual)

    def test_language_choice_is_valid(self):
        languages = {
            1: "English",
            2: "Spanish",
            3: "Portuguese"
        }

        test_cases = [
            (1, True),
            (2, True),
            (3, True),
            (4, False),
            (5, False),
            (10, False),
            ('PIG LATIN', False)
        ]

        for key, expected in test_cases:
            with self.subTest(f"{key}, {expected}"):
                self.assertEqual(expected, mg.language_choice_is_valid(languages, key))

    def test_get_name_input(self):
        name_prompt_dict = {
            1: 'What is your name?',
            2: '¿Cómo te llamas?',
            3: 'Qual é o seu nome?'
        }

        for key, expected in name_prompt_dict.items():
            with self.subTest(f"{key} -> {expected}"):
                self.assertEqual(expected, mg.get_name_input(name_prompt_dict, key))

    @patch('builtins.input', return_value="Harry Potter")
    def test_name_input(self, user_input):
        self.assertEqual("Harry Potter", mg.name_input("What is your name?"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_greet(self, stdout_mock):
        greetings_dict = {
            1: 'Hello',
            2: 'Hola',
            3: 'Olá'
        }

        mg.greet("Winston Wolfe", greetings_dict, 1)
        self.assertEqual("Hello Winston Wolfe\n", stdout_mock.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test2_greet(self, stdout_mock):
        greetings_dict = {
            1: 'Hello',
            2: 'Hola',
            3: 'Olá'
        }
        mg.greet("Vincent Vega", greetings_dict, 2)
        self.assertEqual("Hola Vincent Vega\n", stdout_mock.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test3_greet(self, stdout_mock):
        greetings_dict = {
            1: 'Hello',
            2: 'Hola',
            3: 'Olá'
        }
        mg.greet("Jules Winnfield", greetings_dict, 3)
        self.assertEqual("Olá Jules Winnfield\n", stdout_mock.getvalue())

    @patch('builtins.input', side_effect=["French", "Quel est votre nom?", "Bonjour"])
    def test_add_language(self, mock_inputs):
        mg.add_language()
        new_id = max(mg.lang_dict.keys())
        self.assertIn(new_id, mg.lang_dict)
        self.assertEqual(mg.lang_dict[new_id], "French")
        self.assertEqual(mg.name_prompt_dict[new_id], "Quel est votre nom?")
        self.assertEqual(mg.greetings_dict[new_id], "Bonjour")

    @patch('builtins.input', side_effect=["2", "Salut"])
    def test_edit_greeting(self, mock_inputs):
        mg.edit_greeting()
        self.assertEqual(mg.greetings_dict[2], "Salut")


