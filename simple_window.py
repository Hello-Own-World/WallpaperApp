import sys
from PyQt5 import QtWidgets


def main():
    app = QtWidgets.QApplication(sys.argv)  # Necessary QAplication object

    w = QtWidgets.QWidget()
    w.resize(250, 250)
    w.move(300, 300)
    w.setWindowTitle("WallpaperApp")
    w.show()
    
    sys.exit(app.exec_())   # Mainloop starts


if __name__ == '__main__':
    main()