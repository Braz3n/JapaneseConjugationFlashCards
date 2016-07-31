#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create a bit
more complicated window layout using
the QGridLayout manager.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import sys, random, os, os.path, copy
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QMainWindow, QAction,
    QTextEdit, QGridLayout, QApplication, QPushButton, QMenuBar, QDialog, qApp,
    QCheckBox, QGroupBox, QVBoxLayout, QHBoxLayout, QSpacerItem, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from Verb import *
from Adjective import *

verbs_dir = "./verbs/"
adjectives_dir = "./adjectives/"

class SettingsState(object):
    def __init__(self, verb_state, adj_state, form_state, tense_state, polarity_state):
        self.verb_state = verb_state
        self.adj_state = adj_state
        self.form_state = form_state
        self.tense_state = tense_state
        self.polarity_state = polarity_state

class QuizState(object):
    def __init__(self, verb_list=[], adjective_list=[], form_list=["short", "te", "long"], tense_list=["present"], polarity_list=["negative", "positive"]):
        self.word_list = []
        self.verb_list = verb_list
        self.adj_list = adjective_list
        self.form_list = form_list
        self.tense_list = tense_list
        self.polarity_list = polarity_list

    def populateWordList(self):
        self.word_list = []
        for file_name in self.verb_list:
            self.load_word_list(os.path.join("./verbs/", file_name), "verb")

        for file_name in self.adj_list:
            self.load_word_list(os.path.join("./adjectives/", file_name), "adjective")

    def load_word_list(self, file_name, word_type):
        raw_file = open(file_name, 'r')
        raw_list = raw_file.readlines()
        for line in raw_list:
            line = line.strip()
            if len(line) < 3 or line[0] == "#":
                continue
            string = line.split(',')
            if word_type == "verb":
                if len(string) == 4:
                    word = Verb(string[0], string[1], string[2], conjugate_as=string[3])
                else:
                    word = Verb(string[0], string[1], string[2])
            elif word_type == "adjective":
                if len(string) == 4:
                    word = Adjective(string[0], string[1], string[2], conjugate_as=string[3])
                else:
                    word = Adjective(string[0], string[1], string[2])
            else:
                raise ValueError("Unrecognized word type: \"{0}\"".format(word_type))
            self.word_list.append(word)

class QuizDialog(QDialog):
    def __init__(self, settings_state):
        super().__init__()

        self.settings_state = copy.deepcopy(settings_state)

        self.initUI()
        self.initSettings()

        self.setGeometry(300, 300, -1, -1)  # x, y, w, h
        self.setWindowTitle("Settings")
        # self.show()
        # self.setWindowModality(Qt.ApplicationModal)
        # self.exec_()

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

        return self.settings_state

    def initUI(self):
        ####################
        ## Options Layout ##
        ####################
        options_layout = QGridLayout()

        verb_lists = [f for f in os.listdir(verbs_dir) if os.path.isfile(os.path.join(verbs_dir, f)) and f[0] != '.']
        adj_lists = [f for f in os.listdir(adjectives_dir) if os.path.isfile(os.path.join(adjectives_dir, f)) and f[0] != '.']

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
        polarity_positive = QCheckBox("Positive")
        polarity_negative = QCheckBox("Negative")
        polarity_box_layout.addWidget(polarity_positive)
        polarity_box_layout.addWidget(polarity_negative)
        polarity_box = QGroupBox("Polarity")
        polarity_box.setLayout(polarity_box_layout)
        options_layout.addWidget(polarity_box, 7, 2, 3, 1)
        self.polarity_checkboxes = [polarity_positive, polarity_negative]

        options_box = QGroupBox()
        options_box.setLayout(options_layout)

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

        # self.word_list = load_word_lists()

        self.initUI()
        # self.parentWidget().sendSettingsToQuiz()
        # self.displayQuestion()

    def initUI(self):
        self.question = QLabel('')
        self.question.setAlignment(Qt.AlignHCenter)
        submit = QPushButton('Submit', self)
        submit.clicked.connect(self.submitAnswer)
        self.answer = QLineEdit()
        self.answer.returnPressed.connect(self.submitAnswer)
        self.response = QLabel("")
        self.response.setAlignment(Qt.AlignHCenter)

        grid = QGridLayout()
        grid.setColumnStretch(0, 1)
        grid.setColumnMinimumWidth(1, 350)
        grid.setColumnStretch(3, 1)
        grid.setRowStretch(0, 1)
        grid.setRowStretch(4, 1)
        grid.setSpacing(10)

        grid.addWidget(self.question, 1, 1, 1, 2)  # row, column, rowspan, columnspan
        grid.addWidget(self.answer, 2, 1)
        grid.addWidget(submit, 2, 2)
        grid.addWidget(self.response, 3, 1, 1, 2)

        self.setLayout(grid)

        # self.setGeometry(300, 300, 500, -1)  # x, y, w, h
        # self.setWindowTitle("Japanese Flash Cards")
        # self.show()

    def updateQuizState(self, quiz_state):
        self.quiz_state = quiz_state
        self.displayQuestion()

    def displayQuestion(self):
        # self.question_string, self.answer_string = random_question_data(self.word_list,
        #                     form_list=["short", "te", "long"], tense_list=["present"], polarity_list=["negative", "positive"])
        # self.question.setText(self.question_string)
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

        form = self.quiz_state.form_list[random.randint(0, len(self.quiz_state.form_list)-1)]
        if form == "te":
            self.question_string = "What is the {0} form of \"{1}\"?".format(form, word.english)
        elif form == "long":
            self.question_string = "What is the {0}, {1} {2} form of \"{3}\"?".format(form, tense, polarity, word.english)
        elif form == "short":
            self.question_string = "What is the {0}, {1} {2} form of \"{3}\"?".format(form, tense, polarity, word.english)
        else:
            raise ValueError("Unexpected form_selector value.")

        self.answer_string = word.conjugate(tense, polarity, form)

    def submitAnswer(self):
        if self.answer.text() == self.answer_string:
            self.response.setText("Correct")
        else:
            self.response.setText("Incorrect. The answer was \"{0}\".".format(self.answer_string))

        self.answer.setText("")

        self.displayQuestion()


class QuizWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.initUI()
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
        menubar.setNativeMenuBar(False)  # TODO Check this works outside of OSX.
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(settingsAction)
        fileMenu.addAction(exitAction)

        central = QuizWidget(self)
        self.setCentralWidget(central)
        self.sendSettingsToQuiz()

        self.setGeometry(300, 300, 500, -1)  # x, y, w, h
        self.setWindowTitle("Japanese Flash Cards")
        self.show()

    def initSettings(self):
        # When starting the application, just assume we want to use all of the
        # word lists available.
        verb = [True for f in os.listdir(verbs_dir) if os.path.isfile(os.path.join(verbs_dir, f)) and f[0] != '.']
        adj = [True for f in os.listdir(adjectives_dir) if os.path.isfile(os.path.join(adjectives_dir, f)) and f[0] != '.']
        form = [True, True, True]  # Long, Short, Te
        tense = [True, True]
        polarity = [True, True]
        self.settingsState = SettingsState(verb, adj, form, tense, polarity)
        # Send the initial settings to the central quiz widget.
        # self.sendSettingsToQuiz()

    def sendSettingsToQuiz(self):
        # Convert SettingsState to QuizState and send to the central widget.
        verbList = []
        adjList = []
        formList = []
        tenseList = []
        polarityList = []

        tempList = [f for f in os.listdir(verbs_dir) if os.path.isfile(os.path.join(verbs_dir, f)) and f[0] != '.']
        for i in range(len(self.settingsState.verb_state)):
            if self.settingsState.verb_state[i]:
                verbList.append(tempList[i])

        tempList = [f for f in os.listdir(adjectives_dir) if os.path.isfile(os.path.join(adjectives_dir, f)) and f[0] != '.']
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
            polarityList.append("positive")
        if self.settingsState.polarity_state[1]:
            polarityList.append("negative")

        quizState = QuizState(verbList, adjList, formList, tenseList, polarityList)
        quizState.populateWordList()
        self.centralWidget().updateQuizState(quizState)

    def showSettingsDialog(self):
        settingsDialog = QuizDialog(self.settingsState)
        if settingsDialog.exec_():
            self.settingsState = settingsDialog.getSettings()
            self.sendSettingsToQuiz()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QuizWindow()
    sys.exit(app.exec_())