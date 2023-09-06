import sys
import time as ptime

from PyQt6.QtTest import QTest
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication, QListWidget, QGridLayout, QLabel
from PyQt6.QtCore import QTimer, QDateTime, QSize, Qt, QCoreApplication
from PyQt6.QtGui import QFont


app=QApplication(sys.argv)

screen_size = app.primaryScreen().availableGeometry()

class Smudge_Timer(QWidget):
    def __init__(self,parent=None):
        super(Smudge_Timer, self).__init__(parent)
        self.setWindowTitle('Smudge Stick Timer')

        self.listFile=QListWidget()
        self.label=QLabel('')
        self.label.setFont(QFont('Arial', 15))
        self.label.setObjectName('timer_label')
        self.label.setStyleSheet('QLabel#timer_label {color: white}')
        self.startBtn=QPushButton('Start')
        self.endBtn=QPushButton('Stop')

        self.end_time= ptime.time() + 90

        layout=QGridLayout()
        

        self.timer=QTimer()
        self.timer.timeout.connect(self.showTime)

        layout.addWidget(self.label,0,0,1,2)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)
        self.setMinimumSize(QSize(screen_size.width()//10, screen_size.height()//20))

        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setLayout(layout)

    def showTime(self):
        self.end_time = self.end_time - 1
        timeDisplay=f"{self.end_time} seconds"

        if self.end_time < 0:
            self.endTimer()
            timeDisplay="Благовоние закончилось!"
            self.label.setText(f"{timeDisplay}")
            QTest.qWait(3000)
            self.endTimer()
        self.label.setText(f"{timeDisplay}")

    def startTimer(self):
        self.label.setText("90 seconds")
        self.end_time =  90
        self.timer.start(1000)

    def endTimer(self):
        self.timer.stop()
        self.label.setText(" ")

    def location_on_the_screen(self):
        ag = app.primaryScreen().availableGeometry()
        sg = app.primaryScreen().size()

        widget = self.geometry()
        x = sg.width() // 2 + widget.width() // 2
        y = sg.height() // 2 - widget.height() // 2
        self.move(x, y)

class Attack_timer(QWidget):
    def __init__(self,parent=None):
        super(Attack_timer, self).__init__(parent)
        self.setWindowTitle('Smudge Stick Timer')

        self.__times = 33

        self.listFile=QListWidget()
        self.label=QLabel('')
        self.label.setFont(QFont('Arial', 15))
        self.label.setObjectName('timer_label')
        self.label.setStyleSheet('QLabel#timer_label {color: red}')
        self.startBtn=QPushButton('Start')
        self.endBtn=QPushButton('Stop')

        self.end_time= ptime.time() + 90

        layout=QGridLayout()
        
        self.timer=QTimer()
        self.timer.timeout.connect(self.showTime)

        layout.addWidget(self.label,0,0,1,2)

        self.setMinimumSize(QSize(screen_size.width()//10, screen_size.height()//20))

        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setLayout(layout)

    @property
    def times(self):
        return self.__times

    @times.setter
    def times(self, times):
        self.__times = times

    def showTime(self):
        self.end_time = self.end_time - 1
        timeDisplay=f"{self.end_time} seconds"

        if self.end_time < 0:
            self.endTimer()
            timeDisplay="Благовоние закончилось!"
            self.label.setText(f"{timeDisplay}")
            QTest.qWait(3000)
            self.endTimer()
        self.label.setText(f"{timeDisplay}")

    def startTimer(self):
        self.label.setText(f"{self.__times} seconds")
        self.end_time = self.__times
        self.timer.start(1000)

    def endTimer(self):
        self.timer.stop()
        self.label.setText(" ")

    def location_on_the_screen(self):
        ag = app.primaryScreen().availableGeometry()
        sg = app.primaryScreen().size()

        widget = self.geometry()
        x = sg.width() // 2 + widget.width() // 2
        y = sg.height() // 2 - widget.height()
        self.move(x, y)

if __name__ == '__main__':
    form=Smudge_Timer()
    form.show()
    sys.exit(app.exec())