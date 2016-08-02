# JapaneseConjugationFlashCards
Simple tool for conjugating Japanese verbs and adjectives.

All of the terminology used is derived from [Genki Volume One](http://genki.japantimes.co.jp/index_en).

Note that the tool is currently missing the ability to conjugate the Past Tense of the Short Form of Adjectives and Verbs, as well as anything more advanced than has been taught in Lesson 8. Furthermore, the first commit is simply the state of the code from the moment it started working.

## External Dependencies
The only external dependency required to run the project is PyQt5.

If the [Romkan](https://pypi.python.org/pypi/romkan) Python library is installed, questions can also be answered in Rōmaji, but this is not necessary for the project to run.

## Running the Code
To run the project, simply call:
```
python3 gui.py
```

## Verb and Adjective Data Structure.
Verbs and Adjectives are stored in their own respective folders in the root directory of the project. Groupings of words are delineated by separate files.

Each word is entered on its own line and consists of at least three fields (comma-separated):

1. The Dictionary Form of the word in Hiragana or Katakana. Kanji works too as long as the word isn't irregular (For example, '行く' will not conjugate correctly yet).
2. The Verb or Adjective Class. Either 'う', 'る', or 'irregular' for verbs, and 'い' or 'な' for adjectives.
3. The definition of the verb or adjective, in English.
4. For 行く compound verbs or compound いい adjectives only. This specifies how the word should be conjugated. For example, もっていく conjugates the same way as 行く, which conjugates irregularly for the Te Form but is otherwise considered to be an う verb. For もっていく, the naive Te conjugation would be もっていいて, instead of もっていって, hence why an additional field is used.

Lines that start with '#' or are empty are ignored.

## Rōmaji Support
Instead of answering with Kana characters, Rōmaji can also be used if the Romkan library is installed (See External Dependencies). To verify the answer, the generated conjugation is converted to Rōmaji using the Hepburn Romanization system.

## To Do
- Rename variables and function names for consistency.
- Use a better storage method for storing verbs (XML or JSON?).
