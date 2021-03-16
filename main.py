from functools import wraps
from PyInquirer import prompt
from os import system

from sets import hanoi, relation, representation

ABOUT_CMD = 'About'
RUN_AGAIN_CMD = 'Run again'
BACK_CMD = 'BACK'
QUIT_CMD = 'QUIT'


def clear():
    system('cls||clear')


def ask_chapter():
    clear()
    chapters_prompt = {
        'type': 'list',
        'name': 'chapter',
        'message': 'Which chapter would you like to go?',
        'choices': ['Sets', '...', ABOUT_CMD, QUIT_CMD]
    }
    answers = prompt(chapters_prompt)
    return answers['chapter']


def show_basic_options():
    print()
    options_prompt = {
        'type': 'list',
        'name': 'option',
        'message': 'Options',
        'choices': [RUN_AGAIN_CMD, BACK_CMD, QUIT_CMD]
    }
    return prompt(options_prompt)['option']


def show_todo():
    clear()
    output = ' ____  _____  ____  _____ \n'
    output += '(_  _)(  _  )(  _ \\(  _  ) \n'
    output += '  )(   )(_)(  )(_) ))(_)(  \n'
    output += ' (__) (_____)(____/(_____) \n'
    print(output)
    todo_prompt = {
        'type': 'list',
        'name': 'about',
        'message': 'Options',
        'choices': [BACK_CMD]
    }
    prompt(todo_prompt)


def show_about():
    clear()
    about_prompt = {
        'type': 'list',
        'name': 'about',
        'choices': [BACK_CMD],
        'message': 'Solutions by Luigi Russo'
    }
    prompt(about_prompt)


def ask_sets_exercise():
    clear()
    sets_prompt = {
        'type': 'list',
        'name': 'set',
        'message': 'Which exercise would you like to run?',
        'choices': ['Representation', 'Hanoi', 'Relation', 'Recursion', BACK_CMD, QUIT_CMD]
    }
    answers = prompt(sets_prompt)
    return answers['set']


def exercise_loop(f):
    @wraps(f)
    def loop(*args, **kwargs):
        while True:
            f(*args, **kwargs)
            option = show_basic_options()
            if option == QUIT_CMD:
                quit()
            if option == BACK_CMD:
                return
            if option == RUN_AGAIN_CMD:
                continue
    return loop


@exercise_loop
def hanoi_loop():
    return hanoi.main()


@exercise_loop
def relation_loop():
    return relation.main()


@exercise_loop
def representation_loop():
    return representation.main()


def quit():
    clear()
    exit(0)


def main():
    while True:
        chapter = ask_chapter()
        if chapter == QUIT_CMD:
            break
        if chapter == ABOUT_CMD:
            show_about()
        elif chapter == 'Sets':
            while True:
                exercise = ask_sets_exercise()
                if exercise == 'Hanoi':
                    hanoi_loop()
                elif exercise == 'Relation':
                    relation_loop()
                elif exercise == 'Representation':
                    representation_loop()
                if exercise == BACK_CMD:
                    break
                else:
                    show_todo()
        else:
            show_todo()
    clear()


if __name__ == '__main__':
    main()
