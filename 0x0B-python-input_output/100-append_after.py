#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing a specific string."""
    new_lines = []
    with open(filename, 'r') as file:
        for line in file:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)
    with open(filename, 'w') as file:
        file.writelines(new_lines)
