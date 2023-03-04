import os
import re

#BASE_DIR = '/volume1/homes/eric/_Documents/_Records/By Type/Jobs/LinkedIn/notes/voldemort_emails'
BASE_DIR = '/volume1/homes/eric/_Documents/_Records/By Type/Jobs/LinkedIn/notes'


def is_valid(name):
    if name.endswith('@SynoResource'):
        return True
    pattern = r'[\/:*?"><|]'
    return not re.search(pattern, name)


def crawl(directory):
    listing = os.listdir(directory)
    for item in listing:
        path = BASE_DIR + '/' + item
        if os.path.isdir(path):
            crawl(path)
        if not is_valid(item):
            print(path)


def main():
    crawl(BASE_DIR)


if __name__ == '__main__':
    main()
