import os, json
from conj.Word import Verb, Adjective
from conj import Long, Potential, Short, Te
from copy import deepcopy

def find_lists(directory="."):
    # Start by looking at anything with a .json file name.
    file_list = [file_name for file_name in os.listdir(directory) if ".json" in file_name]

    valid_json = []
    # Try and parse all the files to determine which ones are actually valid.
    for json_file in file_list:
        try:
            # Record the full path for each file.
            json_file = os.path.join(directory, json_file)
            raw_data = open(json_file, 'r', encoding='utf-8')
            json.load(raw_data)
            valid_json.append(json_file)
        except:
            # Ignore invalid json files.
            pass

    valid_json.sort()
    return valid_json

def load_word_lists(json_files, return_verb=False, return_adj=False):
    word_list = []
    for j in json_files:
        json_data = json.load(open(j, 'r', encoding='utf-8'))

        if "Verbs" in json_data and return_verb:
            for word_data in json_data["Verbs"]:
                if word_data["kanji"].lower() == "none":
                    word_data["kanji"] = None
                word_obj = Verb(word_data["kana"], word_data["kanji"], word_data["english"], word_data["group"])
                word_list.append(word_obj)
        if "Adjectives" in json_data and return_adj:
            for word_data in json_data["Adjectives"]:
                if word_data["kanji"].lower() == "none":
                    word_data["kanji"] = None
                word_obj = Adjective(word_data["kana"], word_data["kanji"], word_data["english"], word_data["group"])
                word_list.append(word_obj)

    return word_list

def get_word_list_names(directory="."):
    # Finds the names and file paths for word lists containing verbs and adjectives.
    verb_names_list = []
    adj_names_list = []
    for json_file in find_lists(directory):
        json_data = json.load(open(json_file, 'r', encoding='utf-8'))
        if "Verbs" in json_data:
            verb_names_list.append((json_data["Title"], json_file))
        if "Adjectives" in json_data:
            adj_names_list.append((json_data["Title"], json_file))

    return verb_names_list, adj_names_list
