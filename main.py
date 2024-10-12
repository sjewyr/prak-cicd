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
from PyQt6.QtCore import Qt


class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mem = 0
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
            self.numbers_layout.addWidget(but, idx // 3 + 1, idx % 3)
        self.buttons.append(QPushButton("0", self))
        self.numbers_layout.addWidget(self.buttons[-1], 4, 1)
        self.buttons[-1].clicked.connect(lambda _, x="0": self.number_pressed(num=x))

        self.plus_button = QPushButton("+", self)
        self.numbers_layout.addWidget(self.plus_button, 0, 3)
        self.plus_button.clicked.connect(self.plus)

        self.minus_button = QPushButton("-", self)
        self.numbers_layout.addWidget(self.minus_button, 1, 3)
        self.minus_button.clicked.connect(self.minus)

        self.divide_button = QPushButton("/", self)
        self.numbers_layout.addWidget(self.divide_button, 2, 3)
        self.divide_button.clicked.connect(self.divide)

        self.multiply_button = QPushButton("*", self)
        self.numbers_layout.addWidget(self.multiply_button, 3, 3)
        self.multiply_button.clicked.connect(self.multiply)

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
        self.numbers_layout.addWidget(self.memclear_button, 4, 0)
        self.memclear_button.clicked.connect(self.memreset)

        self.point_button = QPushButton(".", self)
        self.numbers_layout.addWidget(self.point_button, 4, 2)
        self.point_button.clicked.connect(lambda _: _) # TODO
        
        self.equal_button = QPushButton("=", self)
        self.numbers_layout.addWidget(self.equal_button, 4, 3)
        self.equal_button.clicked.connect(lambda _: _) # TODO


    def keyPressEvent(self, a0):
        nums = {
            Qt.Key.Key_0: 0,
            Qt.Key.Key_1: 1,
            Qt.Key.Key_2: 2,
            Qt.Key.Key_3: 3,
            Qt.Key.Key_4: 4,
            Qt.Key.Key_5: 5,
            Qt.Key.Key_6: 6,
            Qt.Key.Key_7: 7,
            Qt.Key.Key_8: 8,
            Qt.Key.Key_9: 9,
        }
        if a0.key() in nums:
            self.number_pressed(num=str(nums[a0.key()]))
        return super().keyPressEvent(a0)

    def plus(self, _):
        # TODO: Dima Sdelai
        pass

    def minus(self, _):
        # TODO: Dima blin nu sdelai
        pass

    def divide(self, _):
        # TODO: NUUUU DIMAA BLIN
        pass

    def multiply(self, _):
        # TODO: dima... ya shas драться nachnu blin
        pass

    def number_pressed(self, num): 
        if self.monitor.text() == "0" or not self.monitor.text().isnumeric():
            self.monitor.setText("")
        self.monitor.setText(self.monitor.text() + num)


    def memplus(self):
        try:
            self.mem+= int(self.monitor.text())
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
