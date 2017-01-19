"""
Anagram solver based on Wikipedia title dump

Wikipedia dump needs to be `downloaded <https://dumps.wikimedia.org/enwiki/latest/enwiki-20170101-all-titles-in-ns0.gz>`
and placed in the directory of this script.

Step 1: Define the groups of characters you want to base the anagram on. The
  script ignores the order in the input, and is case insensitive.

    YELLOW = ['B', 'Al', 'In', 'N', 'S', 'Te' ,'I', 'Er']
    RED = ['Si', 'I', 'Ne', 'Y', 'W', 'Ho', 'Am', 'U']

Step 2: Call the function that filters the wikipedia titles, with your sets of
  characters.

    %run anagram.py
    print(filter_wiki_titles([pre_process_anagram(YELLOW),
                              pre_process_anagram(RED)]))

Step 3: Scan the matching results for the best fit. E.g.:

    YELLOW -> 'Albert Einstein'
"""
import gzip
import re

from collections import Counter, defaultdict

CLEAN_REGEX = re.compile('[!_\- ]+')


def filter_wiki_titles(inputs):
    titles = defaultdict(set)

    with gzip.open('./enwiki-20170101-all-titles-in-ns0.gz', 'rb') as f:
        for line in f:
            line = line.decode('utf8')
            clean = CLEAN_REGEX.sub('', line).strip().lower()

            for inp in inputs:
                if len(clean) >= len(inp):
                    if len(set(clean) - inp) == 0:
                        if len(inp - set(clean)) == 0:
                            print(line.strip())


def pre_process_anagram(inp):
    clean_inp_str = CLEAN_REGEX.sub('', ''.join(inp))
    return frozenset(clean_inp_str.lower().strip())
