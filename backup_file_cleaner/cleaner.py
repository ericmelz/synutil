import os
import re

BASE_DIR = '/volume1/homes/eric/_Documents/_Records/By Type/Jobs/LinkedIn/notes/voldemort_emails'
# BASE_DIR = '/volume1/homes/eric/_Documents/_Records/By Type/Jobs/LinkedIn/notes'


def is_valid(name):
    pattern = '[\/:*?"><|]'
    return re.search(pattern, name)


def main():
    print("hey")
    listing = os.listdir(BASE_DIR)
    print(f'Files and directories:')
    for item in listing:
        dir_char = 'd' if os.path.isdir(BASE_DIR + '/' + item) else ' '
        valid_char = ' ' if is_valid(item) else '*'
        label = f'{dir_char} {item}'
        print(label)


if __name__ == '__main__':
    main()
