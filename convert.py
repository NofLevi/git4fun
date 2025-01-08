import re

def convert_to_windows(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace shebang with Windows batch header
    content = re.sub(r'^#!/bin/bash', '@echo off', content)
    
    # Replace touch with type nul
    content = re.sub(r'touch foobar\.txt', 'type nul > foobar.txt', content)
    
    # Add carets before special characters in echo statements
    content = re.sub(r'echo \'(.*?) -> \((.*?)\)\'', r'echo \1 ^-^> (\2)', content)
    
    # Replace single quotes with double quotes in git commit commands
    content = re.sub(r"git commit --date='(.*?)' -m '(.*?)'", r'git commit --date="\1" -m "\2"', content)
    
    # Write the converted content
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    convert_to_windows("github_painter.sh", "github_painter_new.bat")
    print("Conversion completed! Check windows_script.bat")