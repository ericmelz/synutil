import os
import re
import shutil
from collections import Counter
from datetime import datetime

"""
Notes:
This copies files to a temporary dir, organized by year
These year directories can be merged with corresponding diskstation directories
by opening the src and dest finder window and dragging "{year}/Receipts" onto the corresponding ds year folder
Future implementation can copy to ds directly
After executing

rm -rf ${DEST_DIR} 

Remove local receipts
find '/Users/ericmelz/Desktop/For Filing/Receipts' -name "*.pdf" -exec rm {} \;
"""

SRC_DIR = '/Users/ericmelz/Desktop/For Filing/Receipts'
#DEST_DIR = '/tmp/receiptdemo'
DEST_DIR = '/Volumes/home/_Documents/_Records/_By Year'


def transfer():
    """
    Transfer receipts from local disk to diskstation
    :return:
    """
    pattern = r'(\d{4})_\d{2}_\d{2}_\d{2}.pdf'
    count = 0
    year_counter = Counter()
    prefix_counter = Counter()
    l1_prefix_counter = Counter()
    prefix_len = len(SRC_DIR)
    for root, dirs, files in os.walk(SRC_DIR, topdown=False):
        for name in files:
            m = re.match(pattern, name)
            if m:
                count += 1
                year = m[1]
                year_counter.update([year])
                relative_path = root[prefix_len+1:]
                l1_prefix = relative_path.split('/')[0]
                prefix_counter.update([relative_path])
                l1_prefix_counter.update([l1_prefix])
                dest_year_prefix = '_' if year == str(datetime.now().year) else ''
                dest_path_prefix = os.path.join(DEST_DIR, f'{dest_year_prefix}{year}', 'Receipts', relative_path)
                if not os.path.exists(dest_path_prefix):
                    os.makedirs(dest_path_prefix)
                dest_path = os.path.join(dest_path_prefix, name)
                # print(f'{year}: {root} -- {relative_path}  ---   {name}')
                src_path = os.path.join(root, name)
                print(f'copying {src_path} to {dest_path}')
                shutil.copyfile(src_path, dest_path)
    print(f'Count is {count}')
    print('\nYears:')
    for year, count in year_counter.most_common():
        print(f'{year} {count}')
    print('\nPrefixes:')
    for prefix, count in prefix_counter.most_common():
        print(f'{prefix} {count}')
    print('\nL1 Prefixes:')
    for prefix, count in l1_prefix_counter.most_common():
        print(f'{prefix} {count}')


if __name__ == '__main__':
    transfer()
