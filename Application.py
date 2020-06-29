import sys
import time
import ctypes
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *


class App(QMainWindow):

    def __init__(self):
        super(App, self).__init__()

        self.path_to_icon = "C:\\Users\\yushc\\PycharmProjects\\works\\PyQt5projects\\WallpaperApp\\circle.png"
        self.title = "WallpaperApp"

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        uic.loadUi("C:\\Users\\yushc\\PycharmProjects\\works\\PyQt5projects\\WallpaperApp\\untitled.ui", self)

        self.button1 = self.findChild(QtWidgets.QPushButton, "pushButton_3")
        self.button1.clicked.connect(self.mainloop)

        self.init_ui()
        self.show()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.path_to_icon))

    def mainloop(self):
        worker = Worker()
        self.threadpool.start(worker)


class Worker(QRunnable):            #Окремий потік

    def __init__(self):
        super(Worker, self).__init__()
        """Default settings"""
        self.SPI_SETDESKWALLPAPER = 20
        self.ph_amount = 6
        self.time_period3 = [0, 7, 9, 14, 18, 20, 24]

        """Path to img"""
        self.path = ["C:\\Users\\yushc\\OneDrive\\Робочий стіл\\photo\\2\\1.png",
                     "C:\\Users\\yushc\\OneDrive\\Робочий стіл\\photo\\  2\\2.png",
                     "C:\\Users\\yushc\\OneDrive\\Робочий стіл\\photo\\2\\3.png",
                     "C:\\Users\\yushc\\OneDrive\\Робочий стіл\\photo\\2\\4.png",
                     "C:\\Users\\yushc\\OneDrive\\Робочий стіл\\photo\\2\\5.png",
                     "C:\\Users\\yushc\\OneDrive\\Робочий стіл\\photo\\2\\6.png"]

    def change_BG(self, i):
        ctypes.windll.user32.SystemParametersInfoW(self.SPI_SETDESKWALLPAPER, 0, self.path[i], 3)

    def run(self):
        '''
        Your code goes in this function
        '''
        print("Thread start")
        while True:
            hour = time.localtime()
            for i in range(0, self.ph_amount):
                if self.time_period3[i] <= hour[3] < self.time_period3[i + 1]:
                    self.change_BG(i)
                    print(hour, i)  # Marker
                    time.sleep(((self.time_period3[i + 1] - hour[3]) * 60 - hour[4]) * 60)


def main():
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()