import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton, QMessageBox, QErrorMessage
from PyQt5.QtCore import QSize


class Field():
    def __init__(self, window, name: str, position, size, method):
        self.nameLabel = QLabel(window)
        self.nameLabel.setText(name)
        self.line = QLineEdit(window)

        self.line.move(*position)
        self.line.resize(*size)
        self.line.returnPressed.connect(method)
        self.nameLabel.move(position[0] - 60, position[1])


class Button:
    def __init__(self, window, name, size, position, function, isDefault=False):
        pybutton = QPushButton(name, window)
        pybutton.clicked.connect(function)
        pybutton.setDefault(isDefault)
        pybutton.resize(*size)
        pybutton.move(*position)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 180))
        self.setWindowTitle("Trading Helper")

        self.field_up = Field(self, "Вход:", (80, 20), (200, 30), self.clickMethod)
        self.field_middle = Field(self, "Стоп:", (80, 60), (200, 30), self.clickMethod)
        self.field_down = Field(self, "Выход:", (80, 140), (200, 30), self.clickMethod)

        calculate = Button(self, "Рассчитать", (100, 32), (180, 100), self.clickMethod, True)
        clear_button = Button(self, "Очистить", (100, 32), (80, 100), self.clear_fields)

    def clear_fields(self):
        self.field_up.line.setText("")
        self.field_middle.line.setText("")
        self.field_down.line.setText("")

    def clickMethod(self):
        def get_z(a_, b_):
            if a_ <= b_:
                raise ArithmeticError
            assert a_ > b_, "Unfortunately, the first argument must be bigger than the second one"
            res = (3 * a_ - 2 * b_) * 1.002
            res = round(res, 4)
            return res
        try:
            a = float(self.field_up.line.text().replace(',', '.'))
            b = float(self.field_middle.line.text().replace(',', '.'))

            self.field_down.line.setText(f"{get_z(a, b)}")
        except ValueError:
            QMessageBox.question(self, 'Message - Trading Utility',
                                 "Пожалуйста, вводите только цифры!\n"
                                 "Используйте точки, вместо запятых!",
                                 QMessageBox.Ok,
                                 QMessageBox.Ok)
        except ArithmeticError:
            QMessageBox.question(self, 'Message - Trading Utility',
                                 "Значение \"Вход\" должно быть больше, чем значение \"Стоп\"!\n",
                                 QMessageBox.Ok,
                                 QMessageBox.Ok)
        except:
            QMessageBox.question(self, 'Message - Trading Utility', "Unforeseen Error!",
                                 QMessageBox.Ok,
                                 QMessageBox.Ok)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
