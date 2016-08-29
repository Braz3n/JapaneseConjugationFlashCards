#!/usr/bin/python3

import sys, platform, random, os, os.path, copy, re, json
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QMainWindow, QAction,
    QTextEdit, QGridLayout, QApplication, QPushButton, QMenuBar, QDialog, qApp,
    QCheckBox, QGroupBox, QVBoxLayout, QHBoxLayout, QSpacerItem, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont

from Verb import *
from Adjective import *

try:
    # Attempt to load the Kana to Romaji library.
    from romkan import to_hiragana, to_katakana
    ROMAJI = True
except:
    ROMAJI = False

verbs_dir = "./verbs/"
adjectives_dir = "./adjectives/"

if getattr(sys, 'frozen', False):
    if platform.system().lower() == "darwin":
        # If we're building an application for OSX, the executable is hidden in the application directory.
        application_path = os.path.normpath(os.path.join(os.path.dirname(sys.executable), "../../.."))
    else:
        application_path = os.path.dirname(sys.executable)
elif __file__:
        application_path = os.path.dirname(__file__)

verbs_dir = os.path.join(application_path, verbs_dir)
adjectives_dir = os.path.join(application_path, adjectives_dir)

class SettingsState(object):
    def __init__(self, verb_state, adj_state, form_state, tense_state, polarity_state, easy_mode):
        self.verb_state = verb_state
        self.adj_state = adj_state
        self.form_state = form_state
        self.tense_state = tense_state
        self.polarity_state = polarity_state
        self.easy_mode = easy_mode

class QuizState(object):
    def __init__(self, verb_list=[], adjective_list=[], form_list=["short", "te", "long"], tense_list=["present"], polarity_list=["negative", "affirmative"], easy_mode=False):
        self.word_list = []
        self.verb_list = verb_list
        self.adj_list = adjective_list
        self.form_list = form_list
        self.tense_list = tense_list
        self.polarity_list = polarity_list
        self.easy_mode = easy_mode

    def populateWordList(self):
        self.word_list = []
        for file_name in self.verb_list:
            self.load_word_list_json(os.path.join(verbs_dir, file_name))

        for file_name in self.adj_list:
            self.load_word_list_json(os.path.join(adjectives_dir, file_name))

    def load_word_list_json(self, file_name):
        raw_file = open(file_name, 'r', encoding='utf-8')
        try:
            json_data = json.load(raw_file)
        except:
            # This json file is not valid. Ignore it.
            return

        if json_data["ListType"] != "Verb" and json_data["ListType"] != "Adjective":
            raise ValueError("Unrecognized Word Type: \"{0}\"".format(json_data["ListType"]))

        for word in json_data["WordList"]:
            if "Verb" in word:
                if "ConjugateAs" in word:
                    word_obj = Verb(word["Verb"], word["Class"], word["Definition"], word["ConjugateAs"])
                else:
                    word_obj = Verb(word["Verb"], word["Class"], word["Definition"])
            elif "Adjective" in word:
                if "ConjugateAs" in word:
                    word_obj = Adjective(word["Adjective"], word["Class"], word["Definition"], word["ConjugateAs"])
                else:
                    word_obj = Adjective(word["Adjective"], word["Class"], word["Definition"])

            self.word_list.append(word_obj)

class QuizDialog(QDialog):
    def __init__(self, settings_state):
        super().__init__()

        self.settings_state = copy.deepcopy(settings_state)

        self.initUI()
        self.initSettings()

        self.setGeometry(300, 300, -1, -1)  # x, y, w, h
        self.setWindowTitle("Settings")

    def initSettings(self):
        # Update the Verb Checkbox States
        if len(self.settings_state.verb_state) == 0 or len(self.settings_state.verb_state) != len(self.verb_checkboxes):
            # We've only just started the app or new lists have been added,
            # so initiate the lists as True
            self.settings_state.verb_state = []
            for checkbox in self.verb_checkboxes:
                checkbox.setChecked(True)
                self.settings_state.verb_state.append(True)
        else:
            for i in range(len(self.verb_checkboxes)):
                self.verb_checkboxes[i].setChecked(self.settings_state.verb_state[i])


        # Update the Adjective Checkbox States
        if len(self.settings_state.adj_state) == 0 or len(self.settings_state.adj_state) != len(self.adj_checkboxes):
            # We've only just started the app or new lists have been added,
            # so initiate the lists as True
            self.settings_state.adj_state = []
            for checkbox in self.adj_checkboxes:
                checkbox.setChecked(True)
                self.settings_state.adj_state.append(True)
        else:
            for i in range(len(self.adj_checkboxes)):
                self.adj_checkboxes[i].setChecked(self.settings_state.adj_state[i])

        # Update the question filter states.
        self.form_checkboxes[0].setChecked(self.settings_state.form_state[0])
        self.form_checkboxes[1].setChecked(self.settings_state.form_state[1])
        self.form_checkboxes[2].setChecked(self.settings_state.form_state[2])

        self.tense_checkboxes[0].setChecked(self.settings_state.tense_state[0])
        self.tense_checkboxes[1].setChecked(self.settings_state.tense_state[1])

        self.polarity_checkboxes[0].setChecked(self.settings_state.polarity_state[0])
        self.polarity_checkboxes[1].setChecked(self.settings_state.polarity_state[1])

        self.easy_mode.setChecked(self.settings_state.easy_mode)

    def getSettings(self):
        # Update the Verb and Adjective Settings States
        for i in range(len(self.verb_checkboxes)):
            self.settings_state.verb_state[i] = self.verb_checkboxes[i].isChecked()

        for i in range(len(self.adj_checkboxes)):
            self.settings_state.adj_state[i] = self.adj_checkboxes[i].isChecked()

        # Update the question filter settings states.
        self.settings_state.form_state[0] = self.form_checkboxes[0].isChecked()
        self.settings_state.form_state[1] = self.form_checkboxes[1].isChecked()
        self.settings_state.form_state[2] = self.form_checkboxes[2].isChecked()

        self.settings_state.tense_state[0] = self.tense_checkboxes[0].isChecked()
        self.settings_state.tense_state[1] = self.tense_checkboxes[1].isChecked()

        self.settings_state.polarity_state[0] = self.polarity_checkboxes[0].isChecked()
        self.settings_state.polarity_state[1] = self.polarity_checkboxes[1].isChecked()

        self.settings_state.easy_mode = self.easy_mode.isChecked()

        return self.settings_state

    def initUI(self):
        ####################
        ## Options Layout ##
        ####################
        options_layout = QGridLayout()

        if os.path.isdir(verbs_dir):
            verb_lists = [f for f in os.listdir(verbs_dir) if os.path.isfile(os.path.join(verbs_dir, f)) and f[-5:] == '.json']
            verb_lists = verify_json_list(verb_lists, file_directory=verbs_dir)
        else:
            verb_lists = []
        if os.path.isdir(adjectives_dir):
            adj_lists = [f for f in os.listdir(adjectives_dir) if os.path.isfile(os.path.join(adjectives_dir, f)) and f[-5:] == '.json']
            adj_lists = verify_json_list(adj_lists, file_directory=adjectives_dir)
        else:
            adj_lists = []

        self.verb_checkboxes = []
        self.adj_checkboxes = []

        verb_box_layout = QVBoxLayout()
        for verb_file in verb_lists:
            check = QCheckBox(verb_file, self)
            check.setTristate(False)
            self.verb_checkboxes.append(check)
            verb_box_layout.addWidget(check)
        verb_box_layout.addStretch()
        verb_box = QGroupBox("Verbs")
        verb_box.setLayout(verb_box_layout)
        options_layout.addWidget(verb_box, 0, 0, 10, 1)

        adj_box_layout = QVBoxLayout()
        for adj_file in adj_lists:
            check = QCheckBox(adj_file, self)
            check.setTristate(False)
            self.adj_checkboxes.append(check)
            adj_box_layout.addWidget(check)
        adj_box_layout.addStretch()
        adj_box = QGroupBox("Adjectives")
        adj_box.setLayout(adj_box_layout)
        options_layout.addWidget(adj_box, 0, 1, 10, 1)

        # Form, Tense and Polarity
        form_box_layout = QVBoxLayout()
        form_long = QCheckBox("Long")
        form_long.setTristate(False)
        form_short = QCheckBox("Short")
        form_short.setTristate(False)
        form_te = QCheckBox("Te")
        form_te.setTristate(False)
        form_box_layout.addWidget(form_long)
        form_box_layout.addWidget(form_short)
        form_box_layout.addWidget(form_te)
        form_box = QGroupBox("Form")
        form_box.setLayout(form_box_layout)
        options_layout.addWidget(form_box, 0, 2, 4, 1)
        self.form_checkboxes = [form_long, form_short, form_te]

        tense_box_layout = QVBoxLayout()
        tense_present = QCheckBox("Present")
        tense_past = QCheckBox("Past")
        tense_box_layout.addWidget(tense_present)
        tense_box_layout.addWidget(tense_past)
        tense_box = QGroupBox("Tense")
        tense_box.setLayout(tense_box_layout)
        options_layout.addWidget(tense_box, 4, 2, 3, 1)
        self.tense_checkboxes = [tense_present, tense_past]

        polarity_box_layout = QVBoxLayout()
        polarity_positive = QCheckBox("Affirmative")
        polarity_negative = QCheckBox("Negative")
        polarity_box_layout.addWidget(polarity_positive)
        polarity_box_layout.addWidget(polarity_negative)
        polarity_box = QGroupBox("Polarity")
        polarity_box.setLayout(polarity_box_layout)
        options_layout.addWidget(polarity_box, 7, 2, 3, 1)
        self.polarity_checkboxes = [polarity_positive, polarity_negative]

        options_box = QGroupBox()
        options_box.setLayout(options_layout)

        ######################
        ## Easy Mode Layout ##
        ######################

        easy_layout = QHBoxLayout()
        self.easy_mode = QCheckBox("Show Japanese Word with English Definition in Question")
        easy_layout.addWidget(self.easy_mode)

        easy_box = QGroupBox()
        easy_box.setLayout(easy_layout)

        ##########################
        ## Accept/Cancel Layout ##
        ##########################
        button_layout = QHBoxLayout()
        accept = QPushButton('Accept', self)
        accept.clicked.connect(self.verifyAndAccept)
        cancel = QPushButton('Cancel', self)
        cancel.clicked.connect(self.reject)

        button_layout.addWidget(accept)
        button_layout.addWidget(cancel)

        button_box = QGroupBox()
        button_box.setLayout(button_layout)

        #################
        ## Main Layout ##
        #################
        main_layout = QVBoxLayout()
        main_layout.addWidget(options_box)
        main_layout.addWidget(easy_box)
        main_layout.addWidget(button_box)

        self.setLayout(main_layout)

    def verifyAndAccept(self):
        # Check whether or not the current settings make sense.
        self.getSettings()  # Update the local settingsState variable.
        list_selected = any(self.settings_state.verb_state) or any(self.settings_state.adj_state)
        te_form_selected = self.settings_state.form_state[2]
        other_form_selected = any(self.settings_state.form_state) and any(self.settings_state.tense_state) and any(self.settings_state.polarity_state)

        if list_selected and (te_form_selected or other_form_selected):
            self.accept()
        else:
            warning = QMessageBox(self)
            warning.setText("Invalid Set of Options")
            warning.setInformativeText("Please select at least one Verb or Adjective list and either:\n1) The Te form\n2) A Form, Tense and Polarity from the right hand side.")
            warning.exec_()

class QuizWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        # Determine the font size for the two systems.
        if platform.system().lower() == "windows":
            question_font = QFont("Yu Gothic UI Semibold", 11)
            response_font = QFont("Yu Gothic UI", 11)
        else:
            question_font = QFont("Yu Gothic", 14)
            response_font = QFont("Yu Gothic", 14)
        self.question = QLabel('')
        self.question.setFont(question_font)
        self.question.setAlignment(Qt.AlignHCenter)
        submit = QPushButton('Submit', self)
        submit.clicked.connect(self.submitAnswer)
        self.answer = QLineEdit()
        self.answer.returnPressed.connect(self.submitAnswer)
        if ROMAJI:
            self.answer.textEdited.connect(self.__convertToKana)
        self.response = QLabel("")
        self.response.setFont(response_font)
        self.response.setAlignment(Qt.AlignHCenter)

        grid = QGridLayout()
        grid.setColumnStretch(0, 1)
        grid.setColumnMinimumWidth(1, 550)
        grid.setColumnStretch(3, 1)
        grid.setRowStretch(0, 1)
        grid.setRowStretch(4, 1)
        grid.setSpacing(10)

        grid.addWidget(self.question, 1, 1, 1, 2)  # row, column, rowspan, columnspan
        grid.addWidget(self.answer, 2, 1)
        grid.addWidget(submit, 2, 2)
        grid.addWidget(self.response, 3, 1, 1, 2)

        self.setLayout(grid)

    def __convertToKatakana(self, match):
        if match.group() == "N":
            return "N"
        return to_katakana(match.group()).upper()

    def __convertToHiragana(self, match):
        if match.group() == "n":
            return "n"
        return to_hiragana(match.group())

    def __convertToKana(self):
        self.answer.setText(re.sub('[A-Z]+', self.__convertToKatakana, self.answer.text()))
        self.answer.setText(re.sub('[a-z]+', self.__convertToHiragana, self.answer.text()))

    def updateQuizState(self, quiz_state):
        self.quiz_state = quiz_state
        self.displayQuestion()

    def displayQuestion(self):
        self.randomQuestion()
        self.question.setText(self.question_string)

    def randomQuestion(self):
        word = self.quiz_state.word_list[random.randint(0, len(self.quiz_state.word_list)-1)]

        if len(self.quiz_state.tense_list) > 0:
            tense = self.quiz_state.tense_list[random.randint(0, len(self.quiz_state.tense_list)-1)]
        else:
            tense = None

        if len(self.quiz_state.polarity_list) > 0:
            polarity = self.quiz_state.polarity_list[random.randint(0, len(self.quiz_state.polarity_list)-1)]
        else:
            polarity = None

        if self.quiz_state.easy_mode:
            easy_mode_string = " ({0}) ".format(word.japanese)
        else:
            easy_mode_string = ""

        form = self.quiz_state.form_list[random.randint(0, len(self.quiz_state.form_list)-1)]
        if form == "te":
            self.question_string = "What is the {0} form of \"{1}\"{2}?".format(form, word.english, easy_mode_string)
        elif form == "long":
            self.question_string = "What is the {0}, {1} {2} form of \"{3}\"{4}?".format(form, tense, polarity, word.english, easy_mode_string)
        elif form == "short":
            self.question_string = "What is the {0}, {1} {2} form of \"{3}\"{4}?".format(form, tense, polarity, word.english, easy_mode_string)
        else:
            raise ValueError("Unexpected form_selector value.")

        self.answer_string = word.conjugate(tense, polarity, form)

    def submitAnswer(self):
        if self.answer.text() == self.answer_string:
            self.response.setText("Correct")
        else:
            self.response.setText("Incorrect. The answer was \"{0}\", you answered \"{1}\".".format(self.answer_string, self.answer.text()))

        self.answer.setText("")

        self.displayQuestion()


class QuizWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initSettings()
        self.initUI()

    def initUI(self):
        settingsAction = QAction(QIcon(''), 'Settings', self)
        settingsAction.setShortcut('Ctrl+S')
        settingsAction.setStatusTip('Settings')
        settingsAction.triggered.connect(self.showSettingsDialog)

        exitAction = QAction(QIcon(''), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.exit)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(settingsAction)
        fileMenu.addAction(exitAction)

        central = QuizWidget(self)
        self.setCentralWidget(central)
        self.sendSettingsToQuiz()

        self.setGeometry(300, 300, 600, -1)  # x, y, w, h
        self.setWindowTitle("Japanese Flash Cards")
        self.show()

    def initSettings(self):
        # When starting the application, just assume we want to use all of the
        # word lists available.
        if os.path.isdir(verbs_dir):
            verb = [True for f in os.listdir(verbs_dir) if os.path.isfile(os.path.join(verbs_dir, f)) and f[-5:] == '.json']
            verb = verify_json_list(verb, file_directory=verbs_dir)
        else:
            verb = []
        if os.path.isdir(adjectives_dir):
            adj = [True for f in os.listdir(adjectives_dir) if os.path.isfile(os.path.join(adjectives_dir, f)) and f[-5:] == '.json']
            verb = verify_json_list(adj, file_directory=adjectives_dir)
        else:
            adj = []
        form = [True, True, True]  # Long, Short, Te
        tense = [True, True]
        polarity = [True, True]
        easy_mode = False  # Assume that we don't want easy_mode.
        self.settingsState = SettingsState(verb, adj, form, tense, polarity, easy_mode)

    def sendSettingsToQuiz(self):
        # Convert SettingsState to QuizState and send to the central widget.
        verbList = []
        adjList = []
        formList = []
        tenseList = []
        polarityList = []

        if os.path.isdir(verbs_dir):
            tempList = [f for f in os.listdir(verbs_dir) if os.path.isfile(os.path.join(verbs_dir, f)) and f[-5:] == '.json']
            tempList = verify_json_list(tempList, file_directory=verbs_dir)
        else:
            tempList = []
        for i in range(len(self.settingsState.verb_state)):
            if self.settingsState.verb_state[i]:
                verbList.append(tempList[i])

        if os.path.isdir(adjectives_dir):
            tempList = [f for f in os.listdir(adjectives_dir) if os.path.isfile(os.path.join(adjectives_dir, f)) and f[-5:] == '.json']
            tempList = verify_json_list(tempList, file_directory=adjectives_dir)
        else:
            tempList = []
        for i in range(len(self.settingsState.adj_state)):
            if self.settingsState.adj_state[i]:
                adjList.append(tempList[i])

        if self.settingsState.form_state[0]:
            formList.append("long")
        if self.settingsState.form_state[1]:
            formList.append("short")
        if self.settingsState.form_state[2]:
            formList.append("te")

        if self.settingsState.tense_state[0]:
            tenseList.append("present")
        if self.settingsState.tense_state[1]:
            tenseList.append("past")

        if self.settingsState.polarity_state[0]:
            polarityList.append("affirmative")
        if self.settingsState.polarity_state[1]:
            polarityList.append("negative")

        easy_mode = self.settingsState.easy_mode

        quizState = QuizState(verbList, adjList, formList, tenseList, polarityList, easy_mode)
        quizState.populateWordList()
        self.centralWidget().updateQuizState(quizState)

    def showSettingsDialog(self):
        settingsDialog = QuizDialog(self.settingsState)
        if settingsDialog.exec_():
            self.settingsState = settingsDialog.getSettings()
            self.sendSettingsToQuiz()

def verify_json_list(json_list, file_directory=""):
    # Takes a list of .json file names. Returns the files that can be parsed successfully.
    valid_files = []
    # Don't list any invalid .json files.
    for json_file in json_list:
        try:
            raw_data = open(os.path.join(file_directory, json_file), 'r', encoding='utf-8')
            json.load(raw_data)
            valid_files.append(json_file)
        except:
            # If json.load raises an exception, then we can't use that file.
            pass
    return valid_files

if __name__ == '__main__':
    app = QApplication(sys.argv)

    if (os.path.isdir(verbs_dir) and len([f for f in os.listdir(verbs_dir) if os.path.isfile(os.path.join(verbs_dir, f)) and f[-5:] == '.json']) > 0) or (os.path.isdir(adjectives_dir) and len([f for f in os.listdir(adjectives_dir) if os.path.isfile(os.path.join(adjectives_dir, f)) and f[-5:] == '.json']) > 0):
        # Word list directories exist and have have word lists present.
        ex = QuizWindow()
        sys.exit(app.exec_())
    elif not os.path.isdir(verbs_dir) and not os.path.isdir(adjectives_dir):
        # Neither of the word list directories exist.
        warning = QMessageBox(None)
        warning.setText("Word List Directories Missing")
        warning.setInformativeText("Please create the \"verbs\" and/or \"adjectives\" directories in the same directory as the application.")
        warning.exec_()
    else:
        # At least one of the directories exist but there are no word lists present.
        warning = QMessageBox(None)
        warning.setText("Word Lists Missing")
        warning.setInformativeText("Please place at least one word list in either of the \"verbs\" or \"adjectives\" directories.")
        warning.exec_()
