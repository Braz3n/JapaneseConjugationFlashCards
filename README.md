# JapaneseConjugationFlashCards
Simple tool for conjugating Japanese verbs and adjectives.

All of the terminology used is derived from [Genki Volume One](http://genki.japantimes.co.jp/index_en).

Note that the tool comes packaged with adjectives and verbs up to and including Lesson Nine.

## External Dependencies
The only external dependency required to run the project is PyQt5.

If the [Romkan](https://pypi.python.org/pypi/romkan) Python library is installed, a Japanese keyboard is not required. Instead, characters are converted to Kana as they are typed (See Rōmaji Support).

## Running the Code
To run the project, simply call:
```
python3 gui.py
```

To create an executable for the project, run either the `create_exe.sh` script on OSX, or the `create_exe.bat` script on Windows. The resulting executable is placed in the `dist` directory. The Verbs and Adjectives directories are also copied into the `dist` directory so that the executable can be run.

In OSX, the create_exe.sh command also modifies the .plist file in the resulting application so that it correctly renders on a Retina display.

## Verb and Adjective Data Structure.
Verbs and Adjectives are stored in their own respective folders in the root directory of the project. The word lists are stored in .json files (JavaScript Object Notation) in the appropriate folder.

Each Word List is contained in a separate file and contains the following attributes:
1. ListType - Either "Verb" or "Adjective" as appropriate.
2. Lesson - The Lesson Number for the Word List.
3. WordList - An array containing the word definitions for the list.

Each Verb contains the following attributes:
1. Verb - Contains the Kana form of the verb.
2. Class - Either "う", "る", or "irregular" depending on the verb class.
3. Definition - The definition of the verb in English.
4. ConjugateAs - The second verb in a compound verb if that verb is especially irregular (See Below). This attribute is not required.

Each Adjective contains the following attributes:
1. Adjective - Contains the Kana form of the adjective.
2. Class - Either "い" or "な" depending on the adjective class.
3. Definition - The definition of the adjective in English.
4. ConjugateAs - The second adjective in a compound adjective if that adjective is "いい" (See Below). This attribute is not required.

### The ConjugateAs Attribute
This is only needed for compound verbs ending with "行く" (To Go) or compound adjectives ending with "いい" (Good). It is necessary as 行く is considered a う verb but conjugates irregularly in the て form. Similarly, いい is considered an い adjective but conjugates irregularly too. Furthermore, filtering for adjectives ending in いい is insufficient as かわいい conjugates normally but かっこいい does not.

For verbs and adjectives that conjugate normally according to their respective class, this attribute is not required.

## Rōmaji Support
Kana characters can also be entered using an English keyboard if the Romkan library is installed (See External Dependencies). As characters are entered, lowercase English characters are converted to Hiragana and uppercase English characters are converted to Katakana.

## To Do
- Rename variables and function names for consistency.
- Filtering based on verb/adjective class.
- Implement a way of stopping cards from showing up too frequently.
- Add a help window linking to documentation.
