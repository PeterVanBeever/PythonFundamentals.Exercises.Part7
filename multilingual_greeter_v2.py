from typing import Dict
from typing import Dict, List

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {1: "English", 
             2:"Spanish",
             3:"Dutch",
             4:"Chinese",
             5:"Indonesian"}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = {1: "What is your name?",
                    2: "¿Cómo te llamas?",
                    3: "Hoe heet je?", 
                    4: "你叫什麼名字？",
                    5: "Siapa namamu"}
                    

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = {1: "Hello", 
                  2: "Hola!", 
                  3: "Hallo!", 
                  4: "你好",
                  5: "Halo"}


def print_language_options(lang_options: Dict[int, str]) -> None:
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """
    #pass  # remove pass statement and implement me
    print("Please choose a language: ")
    for key, value in lang_options.items():
        print(f"{key}: {value}")

def language_input() -> int:
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """
    # pass  # remove pass statement and implement me
    selection = input("Enter your choice")
    return int(selection)

def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    """
    This method determines if the choice the user made is valid.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language

    :param lang_choice: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """
    #pass  # remove pass statement and implement me
    
    return lang_choice in lang_options

def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """

    return name_prompt_options.get(lang_choice)
    #pass  # remove pass statement and implement me


def name_input(name_prompt: str) -> str:
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """

    print(name_prompt)
    return input()

    #pass  # remove pass statement and implement me
    
#FUNC - PRINTS - take a name(as string), take a greeting(as dictionary pair values, take a language choice as int, don't return anything)
def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """
    # new variable = the taken greeting options (dictionary pair values), 
    greeting = greetings_options.get(lang_choice)
    print(f"{greeting} {name}")
    
    #pass  # remove pass statement and implement me


#---------------------#---------------------
# Admin mode functions 
#---------------------#---------------------
 
def prompt_options(prompt: str, options: Dict[int, str]) -> int:
    print(prompt)
    for key, value in options.items():
        print(f"{key}: {value}")
    selection = int(input("Enter your choice: "))
    return selection

def user_mode():
    print("Entering user mode...")
    chosen_lang = prompt_options("Please choose a language: ", lang_dict)
    if language_choice_is_valid(lang_dict, chosen_lang):
        selected_prompt = get_name_input(name_prompt_dict, chosen_lang)
        chosen_name = name_input(selected_prompt)
        greet(chosen_name, greetings_dict, chosen_lang)
    else:
        print("Invalid language choice.")

def admin_mode():
        #indicate working
    print("Entering admin mode...")
    admin_mode_options = {1: "Add a new language", 2: "Edit greeting"}
    chosen_action = prompt_options("Please choose an action.", admin_mode_options)

    if chosen_action == 1:
        add_language()
    elif chosen_action == 2:
        edit_greeting()
    else:
        print("Invalid action choice.")

def add_language():
    new_id = max(lang_dict, default=0) + 1
    lang_dict[new_id] = input("Enter the name of the new language: ")
    name_prompt_dict[new_id] = input(f"Enter the name prompt for {lang_dict[new_id]}: ")
    greetings_dict[new_id] = input(f"Enter the greeting for {lang_dict[new_id]}: ")

def edit_greeting():
    lang_id = int(input("Enter the language ID to update: "))
    if lang_id in greetings_dict:
        greetings_dict[lang_id] = input("Enter the new greeting: ")
    else:
        print("Language ID not found.")


#---------------------#---------------------
# Main  
#---------------------#---------------------        

if __name__ == '__main__':
    # strip leading spaces
    mode = input("Choose mode (admin/user): ").strip().lower()
    if mode == "admin":
        admin_mode()
    elif mode == "user":
        user_mode()
    else:
        print("Invalid mode. Please choose enter 'admin' or 'user' on keyboard.")
