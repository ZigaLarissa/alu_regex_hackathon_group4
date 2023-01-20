#!/usr/bin/python3

import re
from termcolor import colored


movie_title_pattern = re.compile(r"\w+\s+\w*\s*S\d{2,2}E\d{2,2}:\s(\w+\s+)*")


# code to ask the user to enter the episode titles
movive_title = input(f'''
    The episode titles should match the pattern "Show Name SXXEXX: Episode Title": ''')

# checking to see a match 
movie_match = movie_title_pattern.match(movive_title)

if movie_match:
    text = colored(f"""\n
    Your title {movive_title} matches the pattern 'Show Name SXXEXX: Episode Title'
    \n""","green", attrs=["blink","bold"])
    print(text)
else:
    test = colored('\nYour title doesnt match the pattern provided \n', "red",attrs=["blink","bold"])
    print(test)
