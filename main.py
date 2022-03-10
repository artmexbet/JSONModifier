import json

from design.main_window import Ui_MainWindow as MainDesign
from design.read import Ui_Dialog as ReadDesign
from design.write import Ui_Dialog as WriteDesign
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog
import sys

from copy import deepcopy


def to_norm(obj):
    return json.dumps(obj, indent=4)


class MainWindow(QMainWindow, MainDesign):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.setWindowTitle("Главная")
        self.create_btn.clicked.connect(self.create_file)
        self.open_btn.clicked.connect(self.open_read_window)
        self.exit_btn.clicked.connect(self.close)

        self.filename = ""

    def create_file(self):
        filename = QFileDialog.getSaveFileName(self, "Создать файл", "", "JSON (*.json)")
        if filename[0]:
            with open(filename[0], "w") as f:
                f.write("{}")
            self.filename = filename[0]
            self.open_write_window()

    def open_write_window(self):
        if not self.filename:
            self.filename = QFileDialog.getOpenFileName(self, "Открыть файл", "", "JSON (*.json)")[0]
        if self.filename != "":
            window = WriteWindow(self.filename)
            self.hide()
            window.exec_()
            self.show()

    def open_read_window(self):
        if not self.filename:
            self.filename = QFileDialog.getOpenFileName(self, "Открыть файл", "", "JSON (*.json)")[0]
        if self.filename != "":
            window = ReadWindow(self.filename)
            self.hide()
            window.exec_()
            self.show()


class Dialog(QDialog):
    def __init__(self, filename):
        super().__init__()

        self.filename = filename
        with open(self.filename, encoding="utf8") as f:
            self.json = json.load(f)

        self.current_query = to_norm(self.json)


class WriteWindow(Dialog, WriteDesign):
    def __init__(self, filename):
        super().__init__(filename)

        self.setupUi(self)

        self.setWindowTitle("Запись")
        self.to_read_btn.clicked.connect(self.to_read)
        self.execute.clicked.connect(self.execute_action)

        self.refresh()

    def refresh(self):
        self.output.setText(self.current_query)

    def execute_action(self):
        keys = self.expression.text().strip().split(">")
        value = self.value.text()
        # Проверка, является ли value словарём или числом
        try:
            value = json.loads(value)
        except:
            pass
        try:
            value = int(value)
        except:
            pass
        # Изменение и запись
        try:
            temp = self.json
            for key in keys[:-1]:
                temp = temp[key]
            if value:
                temp[keys[-1]] = value
            else:
                del temp[keys[-1]]
            self.current_query = to_norm(self.json)
            with open(self.filename, "w", encoding="utf8") as f:
                json.dump(self.json, f)
            self.refresh()
        except KeyError:
            print("atata")

    def to_read(self):
        window = ReadWindow(self.filename)
        self.close()
        window.exec_()


class ReadWindow(Dialog, ReadDesign):
    def __init__(self, filename):
        super().__init__(filename)

        self.setupUi(self)

        self.setWindowTitle("Чтение")
        self.to_write_btn.clicked.connect(self.to_write)
        self.execute.clicked.connect(self.execute_action)

        self.refresh()

    def refresh(self):
        self.output.setText(self.current_query)

    def execute_action(self):
        exp = self.expression.text().strip().split(">")
        try:
            if exp[0] != "":
                temp = deepcopy(self.json)
                for key in exp:
                    temp = temp[key]
                self.current_query = to_norm(temp)
            else:
                self.current_query = to_norm(self.json)
            self.refresh()
        except KeyError:
            print("atata")

    def to_write(self):
        window = WriteWindow(self.filename)
        self.close()
        window.exec_()


def excepthook(type, value, traceback):
    print(type, value, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.excepthook = excepthook
    sys.exit(app.exec_())
