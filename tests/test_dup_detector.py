import os
import unittest


def find_all_case_insensitive_duplicates(directory):
    files = os.listdir(directory)
    lowercase_files = {}

    result = []
    for file in files:
        lowercase_file = file.lower()
        if lowercase_file in lowercase_files:
            result.append((file, lowercase_files[lowercase_file]))
        lowercase_files[lowercase_file] = file
    return result


def walk_data_directory(root):
    for root, dirs, files in os.walk(root):
        for directory in dirs:
            yield os.path.join(root, directory)


def find_and_print_duplicates(directory):
    result = find_all_case_insensitive_duplicates(directory)
    if result:
        print(f"Found duplicates in {directory}:")
        for file1, file2 in result:
            print(f"  {file1} and {file2}")


class MyTestCase(unittest.TestCase):
    def test_walk_data_directory(self):
        print("Testing walk_data_directory")

        counter = 0
        for directory in walk_data_directory("/data"):
            if counter % 1000 == 0:
                print(f"  {counter} {directory}")
            counter += 1
            find_and_print_duplicates(directory)


if __name__ == '__main__':
    unittest.main()
