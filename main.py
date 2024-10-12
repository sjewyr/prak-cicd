from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
    QPushButton,
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QVBoxLayout,
    QLineEdit,
)
from PyQt6.QtCore import Qt


class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mem = 0
        self.monitor_layout = QHBoxLayout()
        self.setCentralWidget(QWidget(self))
        self.monitor = QLineEdit(self)
        self.monitor.setEnabled(False)
        self.centralWidget().setLayout(QVBoxLayout())
        self.centralWidget().layout().addLayout(self.monitor_layout)
        self.monitor_layout.addWidget(self.monitor)
        self.numbers_layout = QGridLayout()
        self.centralWidget().layout().addLayout(self.numbers_layout)

        self.buttons = [QPushButton(str(i), self) for i in range(1, 10)]
        for idx, but in enumerate(self.buttons):
            but.clicked.connect(lambda _, x=str(idx + 1): self.number_pressed(num=x))
            self.numbers_layout.addWidget(but, idx // 3 + 1, idx % 3)
        self.buttons.append(QPushButton("0", self))
        self.numbers_layout.addWidget(self.buttons[-1], 4, 1)
        self.buttons[-1].clicked.connect(lambda _, x="0": self.number_pressed(num=x))

        self.plus_button = QPushButton("+", self)
        self.numbers_layout.addWidget(self.plus_button, 0, 3)
        self.plus_button.clicked.connect(lambda _, x="+": self.process_operator(operator=x))  

        self.minus_button = QPushButton("-", self)
        self.numbers_layout.addWidget(self.minus_button, 1, 3)
        self.minus_button.clicked.connect(lambda _, x="-": self.process_operator(operator=x))  

        self.divide_button = QPushButton("/", self)
        self.numbers_layout.addWidget(self.divide_button, 2, 3)
        self.divide_button.clicked.connect(lambda _, x="/": self.process_operator(operator=x))  

        self.multiply_button = QPushButton("*", self)
        self.numbers_layout.addWidget(self.multiply_button, 3, 3)
        self.multiply_button.clicked.connect(lambda _, x="*": self.process_operator(operator=x))  

        self.memrc_button = QPushButton("M", self)
        self.numbers_layout.addWidget(self.memrc_button, 0, 2)
        self.memrc_button.clicked.connect(self.memrecall)

        self.memadd_button = QPushButton("M+", self)
        self.numbers_layout.addWidget(self.memadd_button, 0, 1)
        self.memadd_button.clicked.connect(self.memplus)

        self.memsubtract_button = QPushButton("M-", self)
        self.numbers_layout.addWidget(self.memsubtract_button, 0, 0)
        self.memsubtract_button.clicked.connect(self.memminus)

        self.memclear_button = QPushButton("MC", self)
        self.numbers_layout.addWidget(self.memclear_button, 4, 3)
        self.memclear_button.clicked.connect(self.memreset)

        self.point_button = QPushButton(".", self)
        self.numbers_layout.addWidget(self.point_button, 4, 0)
        self.point_button.clicked.connect(lambda _: _)  # TODO

        self.equals_button = QPushButton("=", self)
        self.numbers_layout.addWidget(self.equals_button, 4, 2)
        self.equals_button.clicked.connect(self.equals)

        self.backspace_button = QPushButton("⌫", self)
        self.monitor_layout.addWidget(self.backspace_button)
        self.backspace_button.clicked.connect(self.backspace)

        self.clear_entry_button = QPushButton("CE", self)
        self.numbers_layout.addWidget(self.clear_entry_button, 0, 4)
        self.clear_entry_button.clicked.connect(self.clear)

        self.sin_button = QPushButton("sin", self)
        self.numbers_layout.addWidget(self.sin_button, 1, 4)
        self.sin_button.clicked.connect(lambda _: _)  # TODO

        self.cos_button = QPushButton("cos", self)
        self.numbers_layout.addWidget(self.cos_button, 2, 4)
        self.cos_button.clicked.connect(lambda _: _)  # TODO

        self.tan_button = QPushButton("tan", self)
        self.numbers_layout.addWidget(self.tan_button, 3, 4)
        self.tan_button.clicked.connect(lambda _: _)  # TODO

        self.sqrt_button = QPushButton("sqrt", self)
        self.numbers_layout.addWidget(self.sqrt_button, 4, 4)
        self.sqrt_button.clicked.connect(
            lambda _: _
        )  # TODO (Refer to Dmitry's self.proccess_operator and self.equals for consistency)

        self.current_value = ""
        self.pending_operator = None
        self.last_value = 0

    def keyPressEvent(self, a0):
        key = a0.key()
        if Qt.Key.Key_0 <= key <= Qt.Key.Key_9:
            self.number_pressed(num=str(key - Qt.Key.Key_0))
        elif key == Qt.Key.Key_Plus:
            self.process_operator("+")
        elif key == Qt.Key.Key_Minus:
            self.process_operator("-")
        elif key == Qt.Key.Key_Asterisk:
            self.process_operator("*")
        elif key == Qt.Key.Key_Slash:
            self.process_operator("/")
        elif key == Qt.Key.Key_Equal:
            self.equals
        elif key == Qt.Key.Key_Backspace:
            self.backspace
        elif key == Qt.Key.Key_Enter or key == Qt.Key.Key_Return:
            self.equals()
        # TODO: add more key bindings for sin, cos, tan, sqrt, etc.
        else:
            super().keyPressEvent(a0)

    def equals(self):
        if self.pending_operator is not None:
            try:
                current_value = float(self.monitor.text())
                if self.pending_operator == "+":
                    self.last_value += current_value
                elif self.pending_operator == "-":
                    self.last_value -= current_value
                elif self.pending_operator == "*":
                    self.last_value *= current_value
                elif self.pending_operator == "/":
                    if current_value == 0:
                        raise ZeroDivisionError("Ошибка: Деление на 0")
                    self.last_value /= current_value
                self.monitor.setText(str(self.last_value))
                self.pending_operator = None
            except ZeroDivisionError as e:
                self.monitor.setText("Ошибка: Деление на 0")
            except Exception as e:
                self.monitor.setText("Ошибка")

    def clear(self):
        self.monitor.clear()
        self.current_value = ""
        self.last_value = 0
        self.pending_operator = None

    def backspace(self):
        current_text = self.monitor.text()
        if current_text:
            self.monitor.setText(current_text[:-1])

    def number_pressed(self, num):
        if self.monitor.text() == "0" or not self.monitor.text().isnumeric():
            self.monitor.setText("")
        self.monitor.setText(self.monitor.text() + num)

    def process_operator(self, operator):
        try:
            if self.pending_operator is None:
                self.last_value = float(self.monitor.text())
            else:
                self.equals()
            self.pending_operator = operator
            self.monitor.clear()
        except Exception as e:
            self.monitor.setText("Ошибка")

    def memplus(self):
        try:
            self.mem += int(self.monitor.text())
        except ValueError:
            self.monitor.setText("Ошибка: NaN")

    def memminus(self):
        try:
            self.mem -= int(self.monitor.text())
        except ValueError:
            self.monitor.setText("Ошибка: NaN")

    def memreset(self):
        self.mem = 0

    def memrecall(self):
        self.monitor.setText(str(self.mem))


def main():
    import sys

    app = QApplication(sys.argv)
    calculator = CalculatorWindow()
    calculator.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
