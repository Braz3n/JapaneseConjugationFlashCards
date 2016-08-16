#!/bin/bash

pyinstaller gui.py --onefile --noconsole --name ConjugationFlashCards --clean -p /Users/zane/python_virtual/pyinstaller-py3.5/lib/python3.5/site-packages/
cp -R ./verbs ./dist/verbs
cp -R ./adjectives ./dist/adjectives
# Remove the standalone executable.
rm ./dist/ConjugationFlashCards
# Add an entry into the .plist file so that PyQt5 makes the most of a Retina display.
sed -i'' -e 's^</dict>^<key>NSHighResolutionCapable</key>\
<string>True</string>\
</dict>^g' ./dist/ConjugationFlashCards.app/Contents/info.plist
