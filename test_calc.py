import pytestqt
import pytestqt.qtbot
from main import CalculatorWindow
from PyQt6.QtCore import Qt

def test_plus(qtbot:pytestqt.qtbot.QtBot):
    window = CalculatorWindow()
    qtbot.keyPress(window, '6')
    qtbot.keyPress(window, '+')
    qtbot.keyPress(window, '3')
    qtbot.mouseClick(window.invert_button, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(window.equals_button, Qt.MouseButton.LeftButton)
    assert window.monitor.text() == "3.0"


def test_minus(qtbot:pytestqt.qtbot.QtBot):
    window = CalculatorWindow()
    qtbot.keyPress(window, '9')
    qtbot.mouseClick(window.invert_button, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(window.sqrt_button, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(window.equals_button, Qt.MouseButton.LeftButton)
    assert window.monitor.text() == "Error"

def test_mult(qtbot:pytestqt.qtbot.QtBot):
    window = CalculatorWindow()
    qtbot.keyPress(window, '2')
    qtbot.mouseClick(window.point_button, Qt.MouseButton.LeftButton)
    qtbot.keyPress(window, '8')
    qtbot.mouseClick(window.invert_button, Qt.MouseButton.LeftButton)
    qtbot.keyPress(window, '*')
    qtbot.keyPress(window, '5')
    qtbot.mouseClick(window.equals_button, Qt.MouseButton.LeftButton)
    assert window.monitor.text() == "-14.0"

def test_div(qtbot:pytestqt.qtbot.QtBot):
    window = CalculatorWindow()
    qtbot.keyPress(window, '9')
    qtbot.keyPress(window, '/')
    qtbot.keyPress(window, '4')
    qtbot.mouseClick(window.equals_button, Qt.MouseButton.LeftButton)
    assert window.monitor.text() == "2.25"

def test_trygonometr(qtbot:pytestqt.qtbot.QtBot):
    window = CalculatorWindow()
    qtbot.keyPress(window, '3')
    qtbot.mouseClick(window.point_button, Qt.MouseButton.LeftButton)
    qtbot.keyPress(window, '1')
    qtbot.keyPress(window, '4')
    qtbot.mouseClick(window.cos_button, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(window.equals_button, Qt.MouseButton.LeftButton)
    assert round(float(window.monitor.text()),1) == -1.0

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
