import fileinput
import re

# Define the file to be modified
file_path = '/StudentManagementSystemComplete.py'

# Define the regular expression pattern to match font declarations
pattern = re.compile(r"font=\((?:'times'|\s*'times')\s*,\s*\d+\s*,\s*'bold'\)")

# Define the replacement pattern
replacement = "font=('sans-serif', 10, 'bold')"

# Iterate through the file and replace font declarations
with fileinput.FileInput(file_path, inplace=True) as file:
    for line in file:
        line = pattern.sub(replacement, line)
        print(line, end='')
