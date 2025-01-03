from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
    QPushButton,
    QApplication,
    QHBoxLayout,
    QTextEdit,
    QMainWindow,
    QVBoxLayout,
    QLineEdit,
)
import math as m
from PyQt6.QtCore import Qt


class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(QWidget(self))
        self.monitor = QLineEdit(self)
        self.monitor.setEnabled(False)
        self.centralWidget().setLayout(QVBoxLayout())
        self.centralWidget().layout().addWidget(self.monitor)
        self.numbers_layout = QGridLayout()
        self.centralWidget().layout().addLayout(self.numbers_layout)

        self.buttons = [QPushButton(str(i), self) for i in range(1, 10)]
        for idx, but in enumerate(self.buttons):
            but.clicked.connect(lambda _, x=str(idx + 1): self.number_pressed(num=x))
            self.numbers_layout.addWidget(but, idx // 3, idx % 3)

        self.buttons.append(QPushButton("0", self))
        self.numbers_layout.addWidget(self.buttons[-1], 3, 1)
        self.buttons[-1].clicked.connect(lambda _, x="0": self.number_pressed(num=x))

        self.plus_button = QPushButton("+", self)
        self.numbers_layout.addWidget(self.plus_button, 0, 3)
        self.plus_button.clicked.connect(self.plus)

        self.point_button = QPushButton(".", self)
        self.numbers_layout.addWidget(self.point_button, 0, 4)
        self.point_button.clicked.connect(self.point)

        self.minus_button = QPushButton("-", self)
        self.numbers_layout.addWidget(self.minus_button, 1, 3)
        self.minus_button.clicked.connect(self.minus)

        self.divide_button = QPushButton("/", self)
        self.numbers_layout.addWidget(self.divide_button, 2, 3)
        self.divide_button.clicked.connect(self.divide)

        self.multiply_button = QPushButton("*", self)
        self.numbers_layout.addWidget(self.multiply_button, 3, 3)
        self.multiply_button.clicked.connect(self.multiply)

        self.invert_button = QPushButton("inv", self)
        self.numbers_layout.addWidget(self.invert_button, 0, 5)
        self.invert_button.clicked.connect(self.inv)

        self.equals_button = QPushButton("=", self)
        self.numbers_layout.addWidget(self.equals_button, 2, 5)
        self.equals_button.clicked.connect(self.equals)

        self.backspace_button = QPushButton("⌫", self)
        self.numbers_layout.addWidget(self.backspace_button, 3, 5)
        self.backspace_button.clicked.connect(self.backspace)

        self.clear_entry_button = QPushButton("CE", self)
        self.numbers_layout.addWidget(self.clear_entry_button, 1, 5)
        self.clear_entry_button.clicked.connect(self.clear)

        self.sqrt_button = QPushButton("√", self)
        self.numbers_layout.addWidget(self.sqrt_button, 1, 4)
        self.sqrt_button.clicked.connect(self.sqrt)

        self.smaller_button = QPushButton("<-", self)
        self.numbers_layout.addWidget(self.smaller_button, 2, 4)
        self.smaller_button.clicked.connect(self.floor)

        self.bigger_button = QPushButton("->", self)
        self.numbers_layout.addWidget(self.bigger_button, 3, 4)
        self.bigger_button.clicked.connect(self.ceil)

        self.sin_button = QPushButton("sin", self)
        self.numbers_layout.addWidget(self.sin_button, 3, 0)
        self.sin_button.clicked.connect(self.sin)

        self.cos_button = QPushButton("cos", self)
        self.numbers_layout.addWidget(self.cos_button, 3, 2)
        self.cos_button.clicked.connect(self.cos)

        self.mem = 0

        self.memrc_button = QPushButton("M", self)
        self.numbers_layout.addWidget(self.memrc_button, 4, 2)
        self.memrc_button.clicked.connect(self.memrecall)

        self.memadd_button = QPushButton("M+", self)
        self.numbers_layout.addWidget(self.memadd_button, 4, 1)
        self.memadd_button.clicked.connect(self.memplus)

        self.memsubtract_button = QPushButton("M-", self)
        self.numbers_layout.addWidget(self.memsubtract_button, 4, 0)
        self.memsubtract_button.clicked.connect(self.memminus)

        self.memclear_button = QPushButton("MC", self)
        self.numbers_layout.addWidget(self.memclear_button, 4, 3)
        self.memclear_button.clicked.connect(self.memreset)

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
            self.equals()
        elif key == Qt.Key.Key_Backspace:
            self.backspace()
        elif key == Qt.Key.Key_Enter or key == Qt.Key.Key_Return:
            self.equals()
        # TODO: add more key bindings for sin, cos, tan, sqrt, etc.
        else:
            super().keyPressEvent(a0)

    def plus(self):
        self.process_operator("+")

    def minus(self):

        self.process_operator("-")

    def divide(self):
        self.process_operator("/")

    def multiply(self):
        self.process_operator("*")

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
                        raise ZeroDivisionError("Нельзя делить на ноль")
                    self.last_value /= current_value
                self.monitor.setText(str(self.last_value))
                self.pending_operator = None
            except ZeroDivisionError as e:
                self.monitor.setText("Error: Деление на 0")
            except Exception as e:
                self.monitor.setText("Error")

    def clear(self):
        self.monitor.clear()
        self.current_value = ""
        self.last_value = 0
        self.pending_operator = None

    def backspace(self):
        current_text = self.monitor.text()
        if "error" in current_text.lower():
            self.monitor.setText("")
            return

        if current_text:
            self.monitor.setText(current_text[:-1])

    def inv(self):
        try:
            num = float(self.monitor.text())
            if num:
                self.monitor.setText(str(-1*(num)))
        except Exception as e:
            self.monitor.setText("Error")

    def sin(self):
        try:
            num = float(self.monitor.text())
            if num:
                self.monitor.setText(str(m.sin(num)))
        except Exception as e:
            self.monitor.setText("Error")

    def sqrt(self):
        try:
            num = float(self.monitor.text())
            if num:
                self.monitor.setText(str(m.sqrt(num)))
        except Exception as e:
            self.monitor.setText("Error")

    def point(self):
        try:
            num = self.monitor.text()
            if not num:
                self.monitor.setText("0")
            if not "." in num:
                self.monitor.setText(self.monitor.text() + ".")
        except Exception as e:
            self.monitor.setText("Error")

    def floor(self):
        try:
            num = float(self.monitor.text())
            if num:
                self.monitor.setText(str(m.floor(num)))
        except Exception as e:
            self.monitor.setText("Error")

    def ceil(self):
        try:
            num = float(self.monitor.text())
            if num:
                self.monitor.setText(str(m.ceil(num)))
        except Exception as e:
            self.monitor.setText("Error")

    def cos(self):
        try:
            num = float(self.monitor.text())
            if num:
                self.monitor.setText(str(m.cos(num)))
        except Exception as e:
            self.monitor.setText("Error")

    def number_pressed(self, num):
        if self.monitor.text() == "0":
            self.monitor.setText(num)
            return
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
            self.monitor.setText("Error")

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
