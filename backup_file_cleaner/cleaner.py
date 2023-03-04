import os
import re

#BASE_DIR = '/volume1/homes/eric/_Documents/_Records/By Type/Jobs/LinkedIn/notes/voldemort_emails'
#BASE_DIR = '/volume1/homes/eric/_Documents/_Records/By Type/Jobs/LinkedIn/notes'
BASE_DIR = '/volume1/homes/eric/_Documents/_Records/By Type/Jobs/LinkedIn'
COUNT_INTERVAL = 100


def is_valid(name):
    if name.endswith('@SynoResource'):
        return True
    pattern = r'[\/:*?"><|]'
    return not re.search(pattern, name)


class Crawler:
    def __init__(self, root):
        self.root = root
        self.counter = 0

    def _crawl(self, directory):
        # print(f'Crawling {directory}')
        listing = os.listdir(directory)
        for item in listing:
            if self.counter % COUNT_INTERVAL == 0:
                print(self.counter)
            self.counter += 1
            path = directory + '/' + item
            if os.path.isdir(path):
                self._crawl(path)
            if not is_valid(item):
                print(f'  *{path}')
            # else:
            #     print(f'   {path}')

    def crawl(self):
        try:
            self._crawl(self.root)
        except Exception as e:
            print(e)


def main():
    Crawler(BASE_DIR).crawl()


if __name__ == '__main__':
    main()
