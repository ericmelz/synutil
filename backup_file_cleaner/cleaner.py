from datetime import datetime
import os
import re

#BASE_DIR = '/volume1/homes/eric/_Documents/_Records/By Type/Jobs/LinkedIn/notes/voldemort_emails'
BASE_DIR = '/volume1/homes'
COUNT_INTERVAL = 1000000


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
        if directory.endswith('@eaDir'):
            return
        listing = os.listdir(directory)
        for item in listing:
            if self.counter % COUNT_INTERVAL == 0:
                print(f'*{self.counter} {datetime.now()}')
            self.counter += 1
            path = directory + '/' + item
            if os.path.isdir(path):
                self._crawl(path)
            if not is_valid(item):
                print(path)

    def crawl(self):
        try:
            self._crawl(self.root)
        except Exception as e:
            print(e)


def main():
    Crawler(BASE_DIR).crawl()
    print(f'Done! {datetime.now()}')


if __name__ == '__main__':
    main()
