import os
import tempfile
import unittest
from pathlib import Path


class MyTestCase(unittest.TestCase):

    def find_case_insensitive_duplicates(self, directory):
        files = os.listdir(directory)
        lowercase_files = {}

        for file in files:
            lowercase_file = file.lower()
            if lowercase_file in lowercase_files:
                return True, file, lowercase_files[lowercase_file]
            lowercase_files[lowercase_file] = file

    def test_case_insensitive_duplicates(self):
        # Create a temporary directory and add test files
        with tempfile.TemporaryDirectory() as tmpdir:

            print(f"Created temporary directory {tmpdir}")

            path = Path(tmpdir)

            # Add test files (change or add files as necessary for your test)
            (path / "file.txt").write_text("content")
            (path / "FILE.TXT").write_text("content")
            (path / "another_file.txt").write_text("content")

            # Perform the test
            result, file1, file2 = self.find_case_insensitive_duplicates(tmpdir)
            assert result, f"Files {file1} and {file2} are the same except for case"


if __name__ == '__main__':
    unittest.main()
