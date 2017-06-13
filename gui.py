import sys, platform, random, os, os.path, copy, re, json
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QMainWindow, QAction,
    QTextEdit, QGridLayout, QApplication, QPushButton, QMenuBar, QDialog, qApp,
    QCheckBox, QGroupBox, QVBoxLayout, QHBoxLayout, QSpacerItem, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont

from misc import get_word_list_names, load_word_lists

from conj import Advice, Become, Long, Maybe, PleaseDo, Potential, Seems, Short, Te, Want, Hearsay, Volitional
conjugation_forms_global = ["Advice", "Become", "Long", "Maybe", "PleaseDo", "Potential", "Seems", "Short", "Te", "Want", "Hearsay", "Volitional"]

# print(conj.conjugations)

try:
    # Attempt to load the Kana to Romaji library.
    from romkan import to_hiragana, to_katakana
    ROMAJI = True
except:
    ROMAJI = False

WORD_LIST_DIRECTORY = "./lists/"

if getattr(sys, 'frozen', False):
    if platform.system().lower() == "darwin":
        # If we're building an application for OSX, the executable is hidden in the application directory.
        application_path = os.path.normpath(os.path.join(os.path.dirname(sys.executable), "../../.."))
    else:
        application_path = os.path.dirname(sys.executable)
elif __file__:
        application_path = os.path.dirname(__file__)

WORD_LIST_DIRECTORY = os.path.join(application_path, WORD_LIST_DIRECTORY)

class SettingsState(object):
    def __init__(self, verb_state, adj_state, form_state, tense_state, polarity_state, easy_mode, kanji_mode):
        self.verb_state = verb_state
        self.adj_state = adj_state
        self.form_state = form_state
        self.tense_state = tense_state
        self.polarity_state = polarity_state
        self.easy_mode = easy_mode
        self.kanji_mode = kanji_mode

    def __repr__(self):
        return "Verbs = {}\nAdjectives = {}\nForms = {}\nTense = {}\nPolarity = {}\nEasy Mode = {}\nKanij Mode = {}".format(
                    self.verb_state, self.adj_state, self.form_state,
                    self.tense_state, self. polarity_state, self.easy_mode, self.kanji_mode)

class QuizData(object):
    def __init__(self, verb_list, adj_list, forms, tenses, polarities, easy_mode, kanji_mode):
        self.verb_list = verb_list
        self.adj_list = adj_list
        self.forms = forms
        self.tenses = tenses
        self.polarities = polarities
        self.easy_mode = easy_mode
        self.kanji_mode = kanji_mode

class SettingsDialog(QDialog):
    def __init__(self, settings_state=None):
        super().__init__()
        self.settings_state = settings_state

        self.initUI()
        self.initSettings()

    def initUI(self):
        ####################
        ## Options Layout ##
        ####################
        options_layout = QGridLayout()

        # Verb and Adjectives
        self.verb_checkboxes = []
        self.adj_checkboxes = []
        verb_lists, adj_lists = get_word_list_names(WORD_LIST_DIRECTORY)

        verb_box_layout = QVBoxLayout()
        for verb in verb_lists:
            check = QCheckBox(verb[0])
            check.setChecked(False)
            check.path = verb[1]
            self.verb_checkboxes.append(check)
            verb_box_layout.addWidget(check)
        verb_box_layout.addStretch()
        toggle_verb_checkbox = QCheckBox("Set/Clear All")
        toggle_verb_checkbox.setChecked(True)
        toggle_verb_checkbox.stateChanged.connect(self.set_clear_verbs)
        verb_box_layout.addWidget(toggle_verb_checkbox)
        verb_box = QGroupBox("Verbs")
        verb_box.setLayout(verb_box_layout)
        options_layout.addWidget(verb_box, 0, 0, -1, 1)

        adj_box_layout = QVBoxLayout()
        for adj in adj_lists:
            check = QCheckBox(adj[0])
            check.setChecked(False)
            check.path = adj[1]
            self.adj_checkboxes.append(check)
            adj_box_layout.addWidget(check)
        adj_box_layout.addStretch()
        toggle_adj_checkbox = QCheckBox("Set/Clear All")
        toggle_adj_checkbox.setChecked(True)
        toggle_adj_checkbox.stateChanged.connect(self.set_clear_adjectives)
        adj_box_layout.addWidget(toggle_adj_checkbox)
        adj_box = QGroupBox("Adjectives")
        adj_box.setLayout(adj_box_layout)
        options_layout.addWidget(adj_box, 0, 1, -1, 1)

        # Form, Tense and Polarity
        form_box_layout = QVBoxLayout()
        self.form_checkboxes = []
        for form in conjugation_forms_global:
            checkbox = QCheckBox(globals()[form].formName())
            checkbox.setToolTip(globals()[form].toolTip())
            checkbox.name = form  # Might break things
            self.form_checkboxes.append(checkbox)
            form_box_layout.addWidget(checkbox)
        form_box = QGroupBox("Form")
        form_box.setLayout(form_box_layout)
        options_layout.addWidget(form_box, 0, 2)

        tense_box_layout = QVBoxLayout()
        self.tense_checkboxes = []
        for tense in ["Past", "Present"]:
            checkbox = QCheckBox(tense)
            checkbox.name = tense  # Might break things
            self.tense_checkboxes.append(checkbox)
            tense_box_layout.addWidget(checkbox)
        tense_box = QGroupBox("Tense")
        tense_box.setLayout(tense_box_layout)
        options_layout.addWidget(tense_box, 1, 2)

        polarity_box_layout = QVBoxLayout()
        self.polarity_checkboxes = []
        for polarity in ["Affirmative", "Negative"]:
            checkbox = QCheckBox(polarity)
            checkbox.name = polarity  # Might break things
            self.polarity_checkboxes.append(checkbox)
            polarity_box_layout.addWidget(checkbox)
        polarity_box = QGroupBox("Polarity")
        polarity_box.setLayout(polarity_box_layout)
        options_layout.addWidget(polarity_box, 2, 2)

        options_box = QGroupBox()
        options_box.setLayout(options_layout)

        ##########################
        ## Other Options Layout ##
        ##########################

        other_layout = QVBoxLayout()
        self.easy_mode_checkbox = QCheckBox("Show Japanese word with English definition in questions")
        self.kanji_mode_checkbox = QCheckBox("Use Kanji where possible in questions")
        other_layout.addWidget(self.easy_mode_checkbox)
        other_layout.addWidget(self.kanji_mode_checkbox)

        other_box = QGroupBox()
        other_box.setLayout(other_layout)

        ##########################
        ## Accept/Cancel Layout ##
        ##########################
        button_layout = QHBoxLayout()
        accept = QPushButton('Accept', self)
        accept.clicked.connect(self.verifySettings)
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
        main_layout.addWidget(other_box)
        main_layout.addWidget(button_box)

        self.setLayout(main_layout)

    def set_clear_verbs(self, state):
        if state == 0:
            state = False
        else:
            state = True

        for checkbox in self.verb_checkboxes:
            checkbox.setChecked(state)

    def set_clear_adjectives(self, state):
        if state == 0:
            state = False
        else:
            state = True

        for checkbox in self.adj_checkboxes:
            checkbox.setChecked(state)

    def initSettings(self):
        # If there isn't a settings_state object available, create a new one.
        # Need to consider verbs, adjectives, forms, tenses and polarities.
        settings_valid = True
        if self.settings_state is None:
            settings_valid = False
        elif len(self.verb_checkboxes) != len(self.settings_state.verb_state) or \
            len(self.adj_checkboxes) != len(self.settings_state.adj_state):
            # Only need to check verbs and adjectives, as the other lists would
            # require the program to be rerun for them to change.
            settings_valid = False

        if settings_valid == False:
            verb_state = [True] * len(self.verb_checkboxes)
            adj_state = [True] * len(self.adj_checkboxes)
            form_state = [True] * len(self.form_checkboxes)
            tense_state = [True] * len(self.tense_checkboxes)
            polarity_state = [True] * len(self.polarity_checkboxes)
            easy_mode = False
            kanji_mode = False
            self.settings_state = SettingsState(verb_state, adj_state,
                                                form_state, tense_state,
                                                polarity_state, easy_mode,
                                                kanji_mode)

        self.applySettingsFromState()

    def applySettingsFromState(self):
        for i in range(len(self.verb_checkboxes)):
            self.verb_checkboxes[i].setChecked(self.settings_state.verb_state[i])
        for i in range(len(self.adj_checkboxes)):
            self.adj_checkboxes[i].setChecked(self.settings_state.adj_state[i])
        for i in range(len(self.form_checkboxes)):
            self.form_checkboxes[i].setChecked(self.settings_state.form_state[i])
        for i in range(len(self.tense_checkboxes)):
            self.tense_checkboxes[i].setChecked(self.settings_state.tense_state[i])
        for i in range(len(self.polarity_checkboxes)):
            self.polarity_checkboxes[i].setChecked(self.settings_state.polarity_state[i])
        self.easy_mode_checkbox.setChecked(self.settings_state.easy_mode)
        self.kanji_mode_checkbox.setChecked(self.settings_state.kanji_mode)

    def updateSettingsState(self):
        for i in range(len(self.verb_checkboxes)):
            self.settings_state.verb_state[i] = self.verb_checkboxes[i].isChecked()
        for i in range(len(self.adj_checkboxes)):
            self.settings_state.adj_state[i] = self.adj_checkboxes[i].isChecked()
        for i in range(len(self.form_checkboxes)):
            self.settings_state.form_state[i] = self.form_checkboxes[i].isChecked()
        for i in range(len(self.tense_checkboxes)):
            self.settings_state.tense_state[i] = self.tense_checkboxes[i].isChecked()
        for i in range(len(self.polarity_checkboxes)):
            self.settings_state.polarity_state[i] = self.polarity_checkboxes[i].isChecked()
        self.settings_state.easy_mode = self.easy_mode_checkbox.isChecked()
        self.settings_state.kanji_mode = self.kanji_mode_checkbox.isChecked()

    def verifySettings(self):
        # Check whether or not the currently selected settings make sense.

        verb_selected = False
        adj_selected = False
        verb_required = False
        adj_required = False
        for checkbox in self.verb_checkboxes:
            verb_selected = verb_selected or checkbox.isChecked()
        for checkbox in self.adj_checkboxes:
            adj_selected = adj_selected or checkbox.isChecked()

        tense_required = False
        polarity_required = False
        form_selected = False
        for checkbox in self.form_checkboxes:
            form_selected = form_selected or checkbox.isChecked()
            if checkbox.isChecked() and globals()[checkbox.name].isTensed():
                tense_required = True
            if checkbox.isChecked() and globals()[checkbox.name].isPolarised():
                polarity_required = True

            # Here we are testing whether or not the form managed by this checkbox
            # only addresses a single word group (for example, the potential form
            # only applies to verbs).
            required_groups = globals()[checkbox.name].wordGroups()
            if checkbox.isChecked() and ("verb" in required_groups) ^ ("adjective" in required_groups):
                verb_required = verb_required or ("verb" in required_groups)
                adj_required = adj_required or ("adjective" in required_groups)

        tense_selected = False
        polarity_selected = False
        if tense_required:
            for checkbox in self.tense_checkboxes:
                tense_selected = checkbox.isChecked() or tense_selected
        if polarity_required:
            for checkbox in self.polarity_checkboxes:
                polarity_selected = checkbox.isChecked() or polarity_selected

        if not form_selected:
            warning = QMessageBox(self)
            warning.setText("Invalid options selected")
            warning.setInformativeText("No conjugation forms have been selected.")
            warning.exec_()
        elif not (verb_selected or adj_selected):
            warning = QMessageBox(self)
            warning.setText("Invalid options selected")
            warning.setInformativeText("No word lists have been selected.")
            warning.exec_()
        elif verb_required and not verb_selected:
            warning = QMessageBox(self)
            warning.setText("Verb List not Selected")
            warning.setInformativeText("One of the forms selected only applies to verbs, but no verb lists have been selected.")
            warning.exec_()
        elif adj_required and not adj_selected:
            warning = QMessageBox(self)
            warning.setText("Adjective list not selected")
            warning.setInformativeText("One of the forms selected only applies to adjectives, but no adjective lists have been selected.")
            warning.exec_()
        elif (verb_selected or adj_selected) and (not (tense_required ^ tense_selected)) and (not (polarity_required ^ polarity_selected)):
            # Logical negated exclusive or: not (A ^ B)
            self.updateSettingsState()
            self.accept()
        else:
            # If the settings aren't valid, then raise a warning message.
            warning = QMessageBox(self)
            warning.setText("Invalid options selected")
            warning.setInformativeText("Some of the forms selected require at least one tense or polarity to be selected.")
            warning.exec_()

    def getQuizData(self):
        verb_path_list = []
        adj_path_list = []
        for checkbox in self.verb_checkboxes:
            if checkbox.isChecked():
                verb_path_list.append(checkbox.path)
        for checkbox in self.adj_checkboxes:
            if checkbox.isChecked():
                adj_path_list.append(checkbox.path)

        verb_list = load_word_lists(verb_path_list, return_verb=True)
        adj_list = load_word_lists(adj_path_list, return_adj=True)

        form_list = []
        tense_list = []
        polarity_list = []
        for checkbox in self.form_checkboxes:
            if checkbox.isChecked():
                form_list.append(checkbox.name)
        for checkbox in self.tense_checkboxes:
            if checkbox.isChecked():
                tense_list.append(checkbox.name)
        for checkbox in self.polarity_checkboxes:
            if checkbox.isChecked():
                polarity_list.append(checkbox.name)

        return QuizData(verb_list, adj_list, form_list, tense_list, polarity_list,
                        self.settings_state.easy_mode, self.settings_state.kanji_mode)


class QuizWidget(QWidget):
    # This widget runs inside the QuizWindow main window.
    # It handles the general running of the quiz after receiving the
    # quiz settings from the QuizWindow?

    def __init__(self, parent, quiz_data=None):
        super().__init__(parent)

        self.initUI()
        self.quiz_data = quiz_data

    def initUI(self):
        # Determine the font size for the two systems.
        if platform.system().lower() == "windows":
            question_font = QFont("Yu Gothic UI", 16)
            response_font = QFont("Yu Gothic UI", 11)
        else:
            question_font = QFont("Yu Gothic", 20)
            response_font = QFont("Yu Gothic", 16)

        # Initialise the GUI objects
        self.question = QLabel("Question")
        self.question.setFont(question_font)
        self.question.setAlignment(Qt.AlignHCenter)

        self.answer = QLineEdit()
        self.answer.setFont(response_font)
        self.answer.returnPressed.connect(self.submitAnswer)
        if ROMAJI:
            self.answer.textEdited.connect(self.__convertToKana)

        self.response = QLabel("")
        self.response.setFont(response_font)
        self.response.setAlignment(Qt.AlignHCenter)

        submit = QPushButton("Submit", self)
        submit.clicked.connect(self.submitAnswer)

        grid = QGridLayout()
        grid.setColumnStretch(0, 1)
        grid.setColumnMinimumWidth(1, 700)
        grid.setColumnStretch(3, 1)
        grid.setRowStretch(0, 1)
        grid.setRowStretch(4, 1)
        grid.setSpacing(10)

        grid.addWidget(self.question, 1, 1, 1, 2)  # row, column, rowspan, columnspan
        grid.addWidget(self.answer, 2, 1)
        grid.addWidget(self.response, 3, 1, 1, 2)
        grid.addWidget(submit, 2, 2)

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

    def randomQuestion(self):
        form = self.quiz_data.forms[random.randint(0, len(self.quiz_data.forms) - 1)]

        # Some forms cannot conjugate all word groups, so make sure we're only
        # considering a valid form for conjugation.
        word_list = []
        if "verb" in globals()[form].wordGroups():
            word_list += self.quiz_data.verb_list
        if "adjective" in globals()[form].wordGroups():
            word_list += self.quiz_data.adj_list

        word = word_list[random.randint(0, len(word_list) - 1)]

        if len(self.quiz_data.tenses) != 0:
            tense = self.quiz_data.tenses[random.randint(0, len(self.quiz_data.tenses) - 1)].lower()
        else:
            tense = ""
        if len(self.quiz_data.polarities) != 0:
            polarity = self.quiz_data.polarities[random.randint(0, len(self.quiz_data.polarities) - 1)].lower()
        else:
            polarity = ""

        # Dirty hack to get the answer with and without Kanji.
        # Having answer_string0 as the inverse of "using_kanji" means that the
        # final state of the "question_string" variable is always correct.
        question_string, answer_string0 = globals()[form].question(word, form.lower(), tense.lower(), polarity.lower(), self.quiz_data.easy_mode, not self.quiz_data.kanji_mode)
        question_string, answer_string1 = globals()[form].question(word, form.lower(), tense.lower(), polarity.lower(), self.quiz_data.easy_mode, self.quiz_data.kanji_mode)
        answer_string = [answer_string0, answer_string1]

        return question_string, answer_string

    def displayQuestion(self):
        question_string, self.answer_string = self.randomQuestion()
        self.question.setText(question_string)

    def submitAnswer(self):
        if isinstance(self.answer_string, str) and self.answer.text() == self.answer_string:
            self.response.setText("Correct")
        elif isinstance(self.answer_string, list) and self.answer.text() in self.answer_string:
            self.response.setText("Correct")
        else:
            # Because of the hack in randomQuestion(), the correct answer string
            # is always in the 1st index of the array.
            answer_string = self.answer_string[1]
            self.response.setText("Incorrect. The answer was \"{}\", you answered \"{}\"".format(answer_string, self.answer.text()))

        self.answer.setText("")
        self.displayQuestion()

    def updateQuizData(self, quiz_data):
        self.quiz_data = quiz_data
        self.displayQuestion()


class QuizWindow(QMainWindow):
    # The main window for the application.
    # The QuizWidget will run inside this window.
    def __init__(self):
        super().__init__()

        self.settings_state = None

        self.initUI()

    def initUI(self):
        self.setCentralWidget(QuizWidget(self))

        settings_action = QAction(QIcon(""), "Settings", self)
        settings_action.setShortcut("Ctrl+S")
        settings_action.setStatusTip("Settings")
        settings_action.triggered.connect(self.showSettingsDialog)
        # Load all the questions with all possible forms, tenses and polarities
        # so we have a question to ask at startup.
        settingsDialog = SettingsDialog()
        initial_quiz_data = settingsDialog.getQuizData()
        self.centralWidget().updateQuizData(initial_quiz_data)

        exit_action = QAction(QIcon(""), "Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip("Exit Application")
        exit_action.triggered.connect(qApp.exit)

        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(settings_action)
        file_menu.addAction(exit_action)

        self.setGeometry(300, 300, 600, -1)
        self.setWindowTitle("Japanese Flash Cards")
        self.show()

    def showSettingsDialog(self):
        settingsDialog = SettingsDialog(self.settings_state)
        if settingsDialog.exec_():
            self.settings_state = settingsDialog.settings_state
            quiz_data = settingsDialog.getQuizData()
            self.centralWidget().updateQuizData(quiz_data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # quiz = QuizWindow()
    # sys.exit(app.exec_())

    if (os.path.isdir(WORD_LIST_DIRECTORY) and len([f for f in os.listdir(WORD_LIST_DIRECTORY) if os.path.isfile(os.path.join(WORD_LIST_DIRECTORY, f)) and f[-5:] == '.json']) > 0):
        # Word list directories exist and have have word lists present.
        ex = QuizWindow()
        sys.exit(app.exec_())
    elif not os.path.isdir(WORD_LIST_DIRECTORY):
        # Neither of the word list directories exist.
        warning = QMessageBox(None)
        warning.setText("Word List Directories Missing")
        warning.setInformativeText("Please create the \"lists\" directory in the same directory as the application.")
        warning.exec_()
    else:
        # At least one of the directories exist but there are no word lists present.
        warning = QMessageBox(None)
        warning.setText("Word Lists Missing")
        warning.setInformativeText("Please place at least one word list in either of the \"lists\" directory.")
        warning.exec_()
