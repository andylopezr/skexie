#!/usr/bin/python3
""" Skexie module. """
from os.path import abspath
import spacy
import re


def skexie(text):
    """
    SK         EX         I               E
    ││         ││         │               │
    Skills and Experience Interpreter and Extractor.

    This script uses the spacy3 library for Natural Language Processing
    and a custom trained model for Named Entity Recognition to read the
    skills and experience required by the job offer.

    ┌ Usage:
    │
    ├──── from skexie import skexie
    │
    └──── skexie("<Text as a string>")

    ┌ Also:
    │
    └──── ./skexie.py <file.txt>

    ┌ Returns: a list of dictionaries, with a dictionary per skill found.
    │
    └ In the following format:

    [
      {
        "experience": 0,    ─────── Numbers of years, by default 0.
        "skill": "<skill_1>"   ──── String of the read skill.
      },
      {
        "experience": 0,
        "skill": "<skill_2>"
      },
      .
      .
      .
    ]
    """
    # Get absolute path of this script.
    path = abspath(__file__)

    # Concatenate absolute path of the model.
    model = path[0:-9] + 'model'

    nlp = spacy.load(model)
    return_json = []
    text_num_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                     'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
                     'a': 1}

    # Preprocessing of text. - - - - - - - - - - - - - - - - - - - - - - - - -|
    no_hash = text.replace("#", "")
    no_star = no_hash.replace("*", "")
    no_tabs = no_star.replace("\t", "")
    no_extra_spaces = re.sub(' +', ' ', no_tabs)
    sentences = no_extra_spaces.split("\n")

    # Iterate sentence by sentence on the sentences list. - - - - - - - - - - |
    for sent in sentences:
        sent_list = []
        sent_list.append(sent)

        for doc in nlp.pipe(sent_list, disable=["tagger", "parser"]):
            switch = False
            for ent in doc.ents:

                # Set default values for skill entity to return. - - - - - - -|
                if switch is False:
                    json_item = {'skill': '', 'experience': 0}

                # If experience time TAG was found, set it. - - - - - - - - - |
                if ent.label_ == 'time':
                    switch = True
                    time_text = ent.text

                    # Find the digit in the string.
                    try:
                        num = re.search(r'(\d+)', time_text)
                        num = num.group()
                    except Exception as e:
                        pass

                    # If no digit was found look for text, e.g 'two'
                    if num is None:
                        char_num = time_text.split(' ')[0]
                        num = text_num_dict[char_num]

                    num = int(num)

                    # If the word months instead of years is found.
                    if "months" in time_text:
                        num = round((num / 12), 1)

                    json_item['experience'] = num
                    continue

                # If skill TAG was found set it. - - - - - - - - - - - - - - -|
                if ent.label_ == 'skill':
                    switch = False
                    json_item['skill'] = ent.text
                return_json.append(json_item)

    return(return_json)

if __name__ == '__main__':
    with open(av[1], 'r') as f:
        skexie(f.read())
