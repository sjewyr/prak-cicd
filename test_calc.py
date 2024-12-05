import pytestqt
import pytestqt.qtbot
from main import CalculatorWindow
from PyQt6.QtCore import Qt

def test_plus(qtbot:pytestqt.qtbot.QtBot):
    window = CalculatorWindow()
    qtbot.keyPress(window, '1')
    qtbot.keyPress(window, '+')
    qtbot.keyPress(window, '1')
    qtbot.mouseClick(window.equals_button, Qt.MouseButton.LeftButton)
    assert window.monitor.text() == "2.0"


def test_minus(qtbot:pytestqt.qtbot.QtBot):
    window = CalculatorWindow()
    qtbot.keyPress(window, '1')
    qtbot.keyPress(window, '-')
    qtbot.keyPress(window, '1')
    qtbot.mouseClick(window.equals_button, Qt.MouseButton.LeftButton)
    assert window.monitor.text() == "0.0"

def test_mult(qtbot:pytestqt.qtbot.QtBot):
    window = CalculatorWindow()
    qtbot.keyPress(window, '2')
    qtbot.keyPress(window, '*')
    qtbot.keyPress(window, '5')
    qtbot.mouseClick(window.equals_button, Qt.MouseButton.LeftButton)
    assert window.monitor.text() == "10.0"

def test_div(qtbot:pytestqt.qtbot.QtBot):
    window = CalculatorWindow()
    qtbot.keyPress(window, '9')
    qtbot.keyPress(window, '/')
    qtbot.keyPress(window, '4')
    qtbot.mouseClick(window.equals_button, Qt.MouseButton.LeftButton)
    assert window.monitor.text() == "2.25"

def test_mem(qtbot:pytestqt.qtbot.QtBot):
    window = CalculatorWindow()
    qtbot.keyPress(window, '1')
    qtbot.mouseClick(window.memadd_button, Qt.MouseButton.LeftButton)
    qtbot.keyPress(window, '1')
    qtbot.mouseClick(window.memadd_button, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(window.memrc_button, Qt.MouseButton.LeftButton)
    assert window.monitor.text() == "12", "MemAdd is not memadd'ing"

    qtbot.mouseClick(window.memclear_button, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(window.memrc_button, Qt.MouseButton.LeftButton)

    assert window.monitor.text() == "0", "MemReset is not memreset'ing"