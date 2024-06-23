# src/main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel, QRadioButton, QButtonGroup, QGridLayout, QCheckBox, QComboBox, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from Predictor import predict_cgpa_class
from re_run import get_recommendations
from db_operations import insert_enrolled_student, insert_prospective_student

personality_questions = [
    ("Openness", "Is original, comes up with new ideas", False),
    ("Openness", "Is curious about many different things", False),
    ("Openness", "Is ingenious, a deep thinker", False),
    ("Openness", "Has an active imagination", False),
    ("Openness", "Is inventive", False),
    ("Openness", "Values artistic, aesthetic experiences", False),
    ("Openness", "Prefers work that is routine", True),
    ("Openness", "Likes to reflect, play with ideas", False),
    ("Openness", "Has few artistic interests", True),
    ("Openness", "Is sophisticated in art, music, or literature", False),
    ("Conscientiousness", "Does a thorough job", False),
    ("Conscientiousness", "Can be somewhat careless", True),
    ("Conscientiousness", "Is a reliable worker", False),
    ("Conscientiousness", "Tends to be disorganized", True),
    ("Conscientiousness", "Tends to be lazy", True),
    ("Conscientiousness", "Perseveres until the task is finished", False),
    ("Conscientiousness", "Does things efficiently", False),
    ("Conscientiousness", "Makes plans and follows through with them", False),
    ("Conscientiousness", "Is easily distracted", True)
]

class CUEduHelp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CUEduHelp")
        self.setGeometry(100, 100, 800, 600)
        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)
        self.init_ui()

    def init_ui(self):
        self.home_page = QWidget()
        layout = QVBoxLayout()
        enrolled_btn = QPushButton("Enrolled Student")
        prospective_btn = QPushButton("Prospective Student")
        enrolled_btn.clicked.connect(self.show_enrolled_student_page)
        prospective_btn.clicked.connect(self.show_prospective_student_page)
        layout.addWidget(enrolled_btn)
        layout.addWidget(prospective_btn)
        self.home_page.setLayout(layout)
        self.stack.addWidget(self.home_page)

        self.init_enrolled_student_pages()
        self.init_prospective_student_pages()

    def init_enrolled_student_pages(self):
        # Page 1: Enrolled Student Information
        self.enrolled_page1 = QWidget()
        layout = QVBoxLayout()
        form_layout = QFormLayout()
        self.enrolled_id = QLineEdit()
        self.enrolled_name = QLineEdit()
        form_layout.addRow("Student ID", self.enrolled_id)
        form_layout.addRow("Name", self.enrolled_name)
        next_btn = QPushButton("Next")
        next_btn.clicked.connect(self.goto_enrolled_page2)
        layout.addLayout(form_layout)
        layout.addWidget(next_btn)
        self.enrolled_page1.setLayout(layout)
        self.stack.addWidget(self.enrolled_page1)

        # Page 2: Academic Info
        self.enrolled_page2 = QWidget()
        layout = QVBoxLayout()
        form_layout = QFormLayout()
        self.gender_group = QButtonGroup(self)
        self.gender_group.setExclusive(True)
        male_rb = QRadioButton("Male")
        female_rb = QRadioButton("Female")
        self.gender_group.addButton(male_rb)
        self.gender_group.addButton(female_rb)
        gender_layout = QVBoxLayout()
        gender_layout.addWidget(QLabel("Gender"))
        gender_layout.addWidget(male_rb)
        gender_layout.addWidget(female_rb)
        layout.addLayout(gender_layout)

        self.level_group = QButtonGroup(self)
        self.level_group.setExclusive(True)
        level_200_rb = QRadioButton("200")
        level_300_rb = QRadioButton("300")
        level_400_rb = QRadioButton("400")
        level_500_rb = QRadioButton("500")
        self.level_group.addButton(level_200_rb)
        self.level_group.addButton(level_300_rb)
        self.level_group.addButton(level_400_rb)
        self.level_group.addButton(level_500_rb)
        level_layout = QVBoxLayout()
        level_layout.addWidget(QLabel("Level"))
        level_layout.addWidget(level_200_rb)
        level_layout.addWidget(level_300_rb)
        level_layout.addWidget(level_400_rb)
        level_layout.addWidget(level_500_rb)
        layout.addLayout(level_layout)

        self.college_group = QButtonGroup(self)
        self.college_group.setExclusive(True)
        cst_rb = QRadioButton("CST")
        coe_rb = QRadioButton("COE")
        self.college_group.addButton(cst_rb)
        self.college_group.addButton(coe_rb)
        college_layout = QVBoxLayout()
        college_layout.addWidget(QLabel("College"))
        college_layout.addWidget(cst_rb)
        college_layout.addWidget(coe_rb)
        layout.addLayout(college_layout)

        next_btn = QPushButton("Next")
        next_btn.clicked.connect(self.goto_enrolled_page3)
        layout.addWidget(next_btn)
        self.enrolled_page2.setLayout(layout)
        self.stack.addWidget(self.enrolled_page2)

        # Page 3: Personality Test
        self.enrolled_page3 = QWidget()
        layout = QVBoxLayout()
        form_layout = QFormLayout()
        self.personality_responses = {}
        grid_layout = QGridLayout()
        for idx, question_data in enumerate(personality_questions):
            trait, question, reverse = question_data
            label = QLabel(question)
            button_group = QButtonGroup(self)
            for i in range(1, 6):
                radio_button = QRadioButton(str(i))
                button_group.addButton(radio_button, 6 - i if reverse else i)
                grid_layout.addWidget(radio_button, idx, i + 1)
            self.personality_responses[question] = (button_group, trait)
            grid_layout.addWidget(label, idx, 0)

        submit_btn = QPushButton("Submit Personality Test")
        submit_btn.clicked.connect(self.calculate_personality_scores)
        next_btn = QPushButton("Next")
        next_btn.clicked.connect(self.goto_enrolled_page4)
        layout.addLayout(grid_layout)
        layout.addWidget(submit_btn)
        layout.addWidget(next_btn)
        self.enrolled_page3.setLayout(layout)
        self.stack.addWidget(self.enrolled_page3)

        # Page 4: Final Review and Submission
        self.enrolled_page4 = QWidget()
        layout = QVBoxLayout()
        form_layout = QFormLayout()
        self.openness_score = QLineEdit()
        self.openness_score.setReadOnly(True)
        self.conscientiousness_score = QLineEdit()
        self.conscientiousness_score.setReadOnly(True)
        self.gender_display = QLineEdit()
        self.gender_display.setReadOnly(True)
        self.level_display = QLineEdit()
        self.level_display.setReadOnly(True)
        self.college_display = QLineEdit()
        self.college_display.setReadOnly(True)

        form_layout.addRow("Openness Score", self.openness_score)
        form_layout.addRow("Conscientiousness Score", self.conscientiousness_score)
        form_layout.addRow("Gender", self.gender_display)
        form_layout.addRow("Level", self.level_display)
        form_layout.addRow("College", self.college_display)
        submit_btn = QPushButton("Submit Student Record")
        submit_btn.clicked.connect(self.calculate_cgpa)
        layout.addLayout(form_layout)
        layout.addWidget(submit_btn)
        self.enrolled_page4.setLayout(layout)
        self.stack.addWidget(self.enrolled_page4)

        # Page 5: CGPA Prediction
        self.enrolled_page5 = QWidget()
        layout = QVBoxLayout()
        self.cgpa_prediction_result = QLabel("")
        home_btn = QPushButton("Back to Home")
        home_btn.clicked.connect(self.show_home_page)
        layout.addWidget(self.cgpa_prediction_result)
        layout.addWidget(home_btn)
        self.enrolled_page5.setLayout(layout)
        self.stack.addWidget(self.enrolled_page5)

    def init_prospective_student_pages(self):
        # Page 1: Prospective Student Information
        self.prospective_page1 = QWidget()
        layout = QVBoxLayout()
        form_layout = QFormLayout()
        self.prospective_id = QLineEdit()
        self.prospective_name = QLineEdit()
        form_layout.addRow("Student ID", self.prospective_id)
        form_layout.addRow("Name", self.prospective_name)
        next_btn = QPushButton("Next")
        next_btn.clicked.connect(self.goto_prospective_page2)
        layout.addLayout(form_layout)
        layout.addWidget(next_btn)
        self.prospective_page1.setLayout(layout)
        self.stack.addWidget(self.prospective_page1)

        # Page 2: WAEC Subjects Selection
        self.prospective_page2 = QWidget()
        layout = QVBoxLayout()
        form_layout = QFormLayout()
        self.waec_subject_checkboxes = {}
        self.waec_subject_comboboxes = {}
        subjects = ["English", "Maths", "Civic Education", "Trade", "Chemistry", "Physics", "Biology", "Geography", "Agricultural Science", "Technical Drawing", "Further Mathematics", "Computer Studies", "Economics"]
        for subject in subjects:
            checkbox = QCheckBox(subject)
            combobox = QComboBox()
            combobox.addItems(["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"])
            combobox.setEnabled(False)
            checkbox.toggled.connect(lambda state, cb=combobox: cb.setEnabled(state))
            self.waec_subject_checkboxes[subject] = checkbox
            self.waec_subject_comboboxes[subject] = combobox
            form_layout.addRow(checkbox, combobox)
        submit_btn = QPushButton("Submit WAEC")
        submit_btn.clicked.connect(self.submit_waec_results)
        next_btn = QPushButton("Next")
        next_btn.clicked.connect(self.goto_prospective_page3)
        layout.addLayout(form_layout)
        layout.addWidget(submit_btn)
        layout.addWidget(next_btn)
        self.prospective_page2.setLayout(layout)
        self.stack.addWidget(self.prospective_page2)

        # Page 3: JAMB Subjects Selection
        self.prospective_page3 = QWidget()
        layout = QVBoxLayout()
        form_layout = QFormLayout()
        self.jamb_subject_checkboxes = {}
        self.jamb_subject_textboxes = {}
        subjects = ["English", "Maths", "Physics", "Chemistry", "Biology", "Geography", "Economics"]
        for subject in subjects:
            checkbox = QCheckBox(subject)
            textbox = QLineEdit()
            textbox.setEnabled(False)
            checkbox.toggled.connect(lambda state, tb=textbox: tb.setEnabled(state))
            self.jamb_subject_checkboxes[subject] = checkbox
            self.jamb_subject_textboxes[subject] = textbox
            form_layout.addRow(checkbox, textbox)
        submit_btn = QPushButton("Submit JAMB")
        submit_btn.clicked.connect(self.submit_jamb_results)
        next_btn = QPushButton("Next")
        next_btn.clicked.connect(self.goto_prospective_page4)
        layout.addLayout(form_layout)
        layout.addWidget(submit_btn)
        layout.addWidget(next_btn)
        self.prospective_page3.setLayout(layout)
        self.stack.addWidget(self.prospective_page3)

        # Page 4: Personality Test
        self.prospective_page4 = QWidget()
        layout = QVBoxLayout()
        grid_layout = QGridLayout()
        self.personality_responses_prospective = {}
        for idx, question_data in enumerate(personality_questions):
            trait, question, reverse = question_data
            label = QLabel(question)
            button_group = QButtonGroup(self)
            for i in range(1, 6):
                radio_button = QRadioButton(str(i))
                button_group.addButton(radio_button, 6 - i if reverse else i)
                grid_layout.addWidget(radio_button, idx, i + 1)
            self.personality_responses_prospective[question] = (button_group, trait)
            grid_layout.addWidget(label, idx, 0)

        submit_btn = QPushButton("Submit Personality Test")
        submit_btn.clicked.connect(self.calculate_personality_scores_prospective)
        next_btn = QPushButton("Next")
        next_btn.clicked.connect(self.goto_prospective_page5)
        layout.addLayout(grid_layout)
        layout.addWidget(submit_btn)
        layout.addWidget(next_btn)
        self.prospective_page4.setLayout(layout)
        self.stack.addWidget(self.prospective_page4)

        # Page 5: Final Review and Submission
        self.prospective_page5 = QWidget()
        layout = QVBoxLayout()
        form_layout = QFormLayout()
        self.openness_score_prospective = QLineEdit()
        self.openness_score_prospective.setReadOnly(True)
        self.conscientiousness_score_prospective = QLineEdit()
        self.conscientiousness_score_prospective.setReadOnly(True)
        self.waec_summary_display = QLabel("")
        self.jamb_score_display = QLineEdit()
        self.jamb_score_display.setReadOnly(True)
        self.preferred_course = QComboBox()
        self.preferred_course.addItems(["Chemical Engineering", "Civil Engineering", "Computer Engineering", "Electrical and Electronics Engineering", "Information and Communication Engineering", "Mechanical Engineering", "Petroleum Engineering", "Architecture", "Biochemistry", "Biology (Applied Biology and Biotechnology)", "Building Technology", "Computer Science", "Estate Management", "Industrial Chemistry", "Industrial Mathematics", "Industrial Physics", "Management Information Systems", "Microbiology"])
        form_layout.addRow("Openness Score", self.openness_score_prospective)
        form_layout.addRow("Conscientiousness Score", self.conscientiousness_score_prospective)
        form_layout.addRow("WAEC Summary", self.waec_summary_display)
        form_layout.addRow("JAMB Score", self.jamb_score_display)
        form_layout.addRow("Preferred Course", self.preferred_course)
        submit_btn = QPushButton("Submit Student Record")
        submit_btn.clicked.connect(self.submit_prospective_student_record)
        layout.addLayout(form_layout)
        layout.addWidget(submit_btn)
        self.prospective_page5.setLayout(layout)
        self.stack.addWidget(self.prospective_page5)

        # Page 6: Recommended Courses
        self.prospective_page6 = QWidget()
        layout = QVBoxLayout()
        self.recommended_courses = QLabel("")
        home_btn = QPushButton("Back to Home")
        home_btn.clicked.connect(self.show_home_page)
        layout.addWidget(self.recommended_courses)
        layout.addWidget(home_btn)
        self.prospective_page6.setLayout(layout)
        self.stack.addWidget(self.prospective_page6)

    def show_home_page(self):
        self.stack.setCurrentWidget(self.home_page)

    def show_enrolled_student_page(self):
        self.stack.setCurrentWidget(self.enrolled_page1)

    def show_prospective_student_page(self):
        self.stack.setCurrentWidget(self.prospective_page1)

    def goto_enrolled_page2(self):
        self.stack.setCurrentWidget(self.enrolled_page2)

    def goto_enrolled_page3(self):
        self.stack.setCurrentWidget(self.enrolled_page3)

    def goto_enrolled_page4(self):
        self.gender_display.setText("Male" if self.gender_group.checkedButton().text() == "Male" else "Female")
        self.level_display.setText(self.level_group.checkedButton().text())
        self.college_display.setText(self.college_group.checkedButton().text())
        self.stack.setCurrentWidget(self.enrolled_page4)

    def calculate_personality_scores(self):
        openness_score = 0
        conscientiousness_score = 0
        for question, (button_group, trait) in self.personality_responses.items():
            response = button_group.checkedId()
            if "Openness" in trait:
                openness_score += response
            else:
                conscientiousness_score += response

        self.openness_score.setText(str(openness_score))
        self.conscientiousness_score.setText(str(conscientiousness_score))
        
        QMessageBox.information(self, "Personality Test Scores", f"Openness Score: {openness_score}, Conscientiousness Score: {conscientiousness_score}")

    def calculate_cgpa(self):
        student_data = {
            'id': self.enrolled_id.text(),
            'name': self.enrolled_name.text(),
            'gender': "Male" if self.gender_group.checkedButton().text() == "Male" else "Female",
            'college': self.college_display.text(),
            'level': self.level_display.text(),
            'openness': int(self.openness_score.text()),
            'conscientiousness': int(self.conscientiousness_score.text())
        }
        prediction = predict_cgpa_class(student_data['gender'], student_data['college'], student_data['level'], student_data['openness'], student_data['conscientiousness'])
        student_data['prediction'] = prediction
        try:
            insert_enrolled_student(student_data)
            self.cgpa_prediction_result.setText(f"Predicted CGPA Class: {prediction}")
            self.stack.setCurrentWidget(self.enrolled_page5)
        except ValueError as e:
            QMessageBox.warning(self, "Database Error", str(e))

    def goto_prospective_page2(self):
        self.stack.setCurrentWidget(self.prospective_page2)

    def goto_prospective_page3(self):
        self.stack.setCurrentWidget(self.prospective_page3)

    def goto_prospective_page4(self):
        self.stack.setCurrentWidget(self.prospective_page4)

    def goto_prospective_page5(self):
        self.stack.setCurrentWidget(self.prospective_page5)

    def goto_prospective_page6(self):
        self.stack.setCurrentWidget(self.prospective_page6)

    def submit_waec_results(self):
        waec_results = {subject: combobox.currentText() for subject, combobox in self.waec_subject_comboboxes.items() if self.waec_subject_checkboxes[subject].isChecked()}
        if len(waec_results) != 9:
            QMessageBox.warning(self, "Invalid Selection", "Please select exactly 9 WAEC subjects.")
            return
        summary = ", ".join(f"{subject}: {grade}" for subject, grade in waec_results.items())
        self.waec_summary_display.setText(summary)
        QMessageBox.information(self, "WAEC Summary", f"WAEC Results: {summary}")

    def submit_jamb_results(self):
        jamb_results = {subject: int(textbox.text()) for subject, textbox in self.jamb_subject_textboxes.items() if self.jamb_subject_checkboxes[subject].isChecked()}
        if len(jamb_results) != 4:
            QMessageBox.warning(self, "Invalid Selection", "Please select exactly 4 JAMB subjects.")
            return
        total_score = sum(jamb_results.values())
        self.jamb_score_display.setText(str(total_score))
        QMessageBox.information(self, "JAMB Total Score", f"JAMB Total Score: {total_score}")

    def calculate_personality_scores_prospective(self):
        openness_score = 0
        conscientiousness_score = 0
        for question, (button_group, trait) in self.personality_responses_prospective.items():
            response = button_group.checkedId()
            if "Openness" in trait:
                openness_score += response
            else:
                conscientiousness_score += response

        self.openness_score_prospective.setText(str(openness_score))
        self.conscientiousness_score_prospective.setText(str(conscientiousness_score))
        QMessageBox.information(self, "Personality Test Scores", f"Openness Score: {openness_score}, Conscientiousness Score: {conscientiousness_score}")

    def submit_prospective_student_record(self):
        waec_results = {subject: combobox.currentText() for subject, combobox in self.waec_subject_comboboxes.items() if self.waec_subject_checkboxes[subject].isChecked()}
        jamb_results = {subject: int(textbox.text()) for subject, textbox in self.jamb_subject_textboxes.items() if self.jamb_subject_checkboxes[subject].isChecked()}
        total_score = sum(jamb_results.values())
        student_data = {
            'id': self.prospective_id.text(),
            'name': self.prospective_name.text(),
            'openness': int(self.openness_score_prospective.text()),
            'conscientiousness': int(self.conscientiousness_score_prospective.text()),
            'waec_subject_picked': len(waec_results),
            'waec_subject_selected_1': list(waec_results.keys())[0],
            'waec_subject_selected_2': list(waec_results.keys())[1],
            'waec_subject_selected_3': list(waec_results.keys())[2],
            'waec_subject_selected_4': list(waec_results.keys())[3],
            'waec_subject_selected_5': list(waec_results.keys())[4],
            'waec_subject_selected_6': list(waec_results.keys())[5],
            'waec_subject_selected_7': list(waec_results.keys())[6],
            'waec_subject_selected_8': list(waec_results.keys())[7],
            'waec_subject_selected_9': list(waec_results.keys())[8],
            'jamb_subject_selected_1': list(jamb_results.keys())[0],
            'jamb_subject_selected_2': list(jamb_results.keys())[1],
            'jamb_subject_selected_3': list(jamb_results.keys())[2],
            'jamb_subject_selected_4': list(jamb_results.keys())[3],
            'jamb_score': total_score,
            'preferred_course': self.preferred_course.currentText(),
            'waec_data': waec_results,
            'jamb_subjects': list(jamb_results.keys())
        }
        recommendations = get_recommendations(
            student_data['preferred_course'],
            student_data['waec_data'],
            student_data['jamb_score'],
            student_data['jamb_subjects'],
            student_data['openness'],
            student_data['conscientiousness']
        )
        student_data['recommendation_1'] = recommendations[1][0] if len(recommendations[1]) > 0 else ""
        student_data['recommendation_2'] = recommendations[1][1] if len(recommendations[1]) > 1 else ""
        student_data['recommendation_3'] = recommendations[1][2] if len(recommendations[1]) > 2 else ""
        try:
            insert_prospective_student(student_data)
            self.recommended_courses.setText(f"Recommended Courses: {', '.join(recommendations[1])}")
            self.goto_prospective_page6()
        except ValueError as e:
            QMessageBox.warning(self, "Database Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = CUEduHelp()
    main_window.show()
    sys.exit(app.exec_())
