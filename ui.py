from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout,
    QHBoxLayout, QSlider, QPushButton
)
from PySide6.QtCore import Qt
from logic import calculate_scores
import sys

CRITERIA = [
    "Κόπος",
    "Χρησιμότητα",
    "Προσωπικό Νόημα",
    "Δύναμη Ιδέας",
    "Motivation",
    "Συναισθηματικό Βάρος",
    "Πιθανότητα Επιτυχίας",
    "Χρόνος"
]

class OptionWidget(QWidget):
    def __init__(self, title):
        super().__init__()
        self.layout = QVBoxLayout()
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText(title)
        self.layout.addWidget(self.title_input)

        self.sliders = []
        for criterion in CRITERIA:
            row = QHBoxLayout()

            label = QLabel(criterion)
            label.setFixedWidth(150)  # σταθερό πλάτος για label

            slider = QSlider(Qt.Horizontal)
            slider.setRange(1, 10)
            slider.setValue(5)
            slider.setFixedWidth(200)  # ίδιου μήκους όλα

            value_label = QLabel("5")  # δείχνει την τρέχουσα τιμή

            def make_updater(lbl, sldr):
                return lambda value: lbl.setText(str(value))

            slider.valueChanged.connect(make_updater(value_label, slider))

            row.addWidget(label)
            row.addWidget(slider)
            row.addWidget(value_label)

            self.sliders.append(slider)
            self.layout.addLayout(row)
            self.setLayout(self.layout)


    def get_scores(self):
        return {
            criterion: slider.value()
            for criterion, slider in zip(CRITERIA, self.sliders)
        }

    def get_title(self):
        return self.title_input.text()

def launch_app():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("MindWeigh")
    window.resize(800, 600)

    layout = QVBoxLayout()

    options_layout = QHBoxLayout()
    option1 = OptionWidget("Επιλογή 1")
    option2 = OptionWidget("Επιλογή 2")
    options_layout.addWidget(option1)
    options_layout.addWidget(option2)

    result_label = QLabel("Αποτελέσματα:")

    def on_calculate():
        title1 = option1.get_title()
        title2 = option2.get_title()
        scores1 = option1.get_scores()
        scores2 = option2.get_scores()
        result = calculate_scores(title1, scores1, title2, scores2)
        result_label.setText(result)

    calc_button = QPushButton("Υπολόγισε")
    calc_button.clicked.connect(on_calculate)

    layout.addLayout(options_layout)
    layout.addWidget(calc_button)
    layout.addWidget(result_label)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec())