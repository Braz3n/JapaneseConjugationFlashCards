#!/bin/bash

pyinstaller gui.py --onefile --noconsole --name ConjugationFlashCards --clean -p /Users/zane/python_virtual/pyinstaller-py3.5/lib/python3.5/site-packages/
cp -R ./verbs ./dist/verbs
cp -R ./adjectives ./dist/adjectives
