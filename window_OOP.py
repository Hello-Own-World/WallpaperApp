import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

path_to_icon = "C:\\Users\\yushc\\PycharmProjects\\works\\PyQt5projects\\circle.png"


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Window_OOP")
        self.setWindowIcon(QIcon(path_to_icon))
        
        self.show()


def main():
        app = QApplication(sys.argv)
        window = App()
        sys.exit(app.exec_())


if __name__ == "__main__":
    main()
