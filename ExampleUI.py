import sys, os
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic, QtWidgets


class  UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("C:\\Users\\yushc\\PycharmProjects\\works\\PyQt5projects\\example.ui", self)

        self.button = self.findChild(QtWidgets.QPushButton, 'BtnBrowse')  # Find the button
        self.button.clicked.connect(self.BtnPressed)  # Remember to pass the definition/method, not the return value!

        self.show()

    def BtnPressed(self):
        self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose folder")

        if directory:
            for file_name in os.listdir(directory):
                self.listWidget.addItem(file_name)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
