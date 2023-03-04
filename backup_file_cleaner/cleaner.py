import os

BASE_DIR = '/volume1/homes/eric/_Documents/_Records/By Type/Jobs/LinkedIn/notes/voldemort_emails'


def main():
    print("hey")
    dir_list = os.listdir(BASE_DIR)
    print(f'Files and directories:')
    print(dir_list)


if __name__ == '__main__':
    main()
