# JapaneseConjugationFlashCards
Simple tool for conjugating Japanese verbs and adjectives.

All of the terminology used is derived from [Genki Volume One and Two](http://genki.japantimes.co.jp/index_en).

Note that the tool comes packaged with adjectives and verbs from a range of lessons from the aforementioned textbooks.

## External Dependencies
The only external dependency required to run the project is PyQt5. There are two additional packages that are used to support the project.
- If the [Romkan](https://pypi.python.org/pypi/romkan) Python library is installed, a Japanese keyboard is not required. Instead, characters are converted to Kana as they are typed (See Rōmaji Support).
- [Pyinstaller](http://www.pyinstaller.org/) is also used to turn the project into an executable for Windows and OSX.

## Running the Code
To run the project, simply call:
```
python3 gui.py
```

To create an executable for the project, run either the `create_exe.sh` script on OSX, or the `create_exe.bat` script on Windows. The resulting executable is placed in the `dist` directory. The Verbs and Adjectives directories are also copied into the `dist` directory so that the executable can be run.

In OSX, the create_exe.sh command also modifies the .plist file in the resulting application so that it correctly renders on a Retina display.

## Verb and Adjective Data Structure.
Verbs and Adjectives are stored in the "lists" directory using the JSON (JavaScript Object Notation) file format.

Each Word List is contained in a separate file and contains the following attributes:
1. Title - A string for representing the list inside the application.
3. Verbs - An array containing the verb definitions for the list.
3. Adjectives - An array containing the adjective definitions for the list.

Each word contains the following attributes:
1. Kana - The kana form of the verb.
2. Kanji - The kanji representation of the verb. Words without a kanji representation should contain the string "None".
3. English - The definition of the word in English.
4. Group - The group of the verb or adjective (one of う, る or irregular for verbs, and い, いい or な for adjectives).

### Some Assumptions Regarding Verb Conjugation
Due to some irregularities in how Japanese verbs conjugate, it is assumed that any う verb that ends in いく or 行く conjugates as the Japanese verb "To Go". Similarly, the same logic has been applied to irregular verbs ending in くる/来る (To Come) and する (To Do).

### The いい Adjective Group
The adjective いい (Good) is considered to come under the い grouping for adjectives (as well as any adjectives formed from compounding a word with いい, such as かっこいい) despite conjugating irregularly when compared to all other い adjectives.　Unfortunately there are also words such as かわいい that seem as if they might be an いい compound but conjugate regularly. As a result, any い adjectives that conjugate irregularly must be defined as part of the いい group to distinguish them from the rest of the regularly conjugating い adjectives.

## Rōmaji Support
Kana characters can also be entered using an English keyboard if the Romkan library is installed (See External Dependencies). As characters are entered, lowercase English characters are converted to Hiragana and uppercase English characters are converted to Katakana.

## To Do
- Add a separate category for specifying the formality of the conjugation.
- Rename variables and function names for consistency.
- Filtering based on verb/adjective class.
- Implement a way of stopping cards from showing up too frequently.
- Add a help window linking to documentation.
