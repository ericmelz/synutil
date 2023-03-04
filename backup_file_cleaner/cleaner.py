import os

# BASE_DIR = '/volume1/homes/eric/_Documents/_Records/By Type/Jobs/LinkedIn/notes/voldemort_emails'
BASE_DIR = '/volume1/homes/eric/_Documents/_Records/By Type/Jobs/LinkedIn/notes'


def main():
    print("hey")
    listing = os.listdir(BASE_DIR)
    print(f'Files and directories:')
    for item in listing:
        isdir = os.path.isdir(BASE_DIR + '/' + item)
        dir_char = 'd' if isdir else ' '
        label = f'{dir_char}{item}'
        print(label)


if __name__ == '__main__':
    main()
