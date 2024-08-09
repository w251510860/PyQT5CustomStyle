from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QLCDNumber,QFormLayout,QLineEdit,QLabel,QGridLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt,QTimer,QDateTime,QDate,QTime,QSize
import sys

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,330,310)
        self.setWindowTitle("数字键盘输入")
        gridLayout = QGridLayout()
        self.display = QLineEdit("0")
        self.display.setFixedSize(QSize(287,40))
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFont(QFont("微软雅黑",14,QFont.Bold))
        gridLayout.addWidget(self.display,0,0,1,4)
        self.showNum = ""

        keys = ['Clear', '/', '*', '-',
                '7', '8', '9', '+',
                '4', '5', '6', '',
                '1', '2', '3', 'Enter',
                '0', '', '.', '']
        position = [(0, 0), (0, 1), (0, 2), (0, 3),
                    (1, 0), (1, 1), (1, 2), (1, 3),
                    (2, 0), (2, 1), (2, 2), (2, 2),
                    (3, 0), (3, 1), (3, 2), (3, 3),
                    (4, 0), (4, 1), (4, 2), (4, 3), ]
        for item in range(len(keys)):
            btn = QPushButton(keys[item])
            btn.setFixedSize(QSize(60, 40))
            btn.setFont(QFont("微软雅黑",12,QFont.Bold))
            btn.clicked.connect(self.btnClicked)
            if keys[item] == "+":
                gridLayout.addWidget(btn, 2, 3, 2, 1)
                btn.setFixedSize(QSize(60, 90))
            elif keys[item] == "Enter":
                gridLayout.addWidget(btn, 4, 3, 2, 1)
                btn.setFixedSize(QSize(60, 90))
            elif keys[item] == "0":
                gridLayout.addWidget(btn, 5, 0, 1, 2)
                btn.setFixedSize(QSize(142, 40))
            elif keys[item] == "":
                continue
            else:
                gridLayout.addWidget(btn, position[item][0]+1, position[item][1], 1, 1)
        self.setLayout(gridLayout)

    def btnClicked(self):
        sender = self.sender()
        symbols = ["Clear","/","*","-","+","Enter"]
        if ' ' in self.showNum and sender.text() not in ["/","*","-","+"]:
            self.showNum = ''
        else:
            self.showNum.strip()
        if sender.text() not in symbols:
            self.showNum += sender.text()
        elif sender.text() == "Clear":
            self.showNum = ""
        elif sender.text() in ["/","*","-","+"]:
            self.showNum += sender.text()

        else:
            self.showNum = ' ' + self.showNum
            self.showNum = str(eval(self.showNum))
        self.display.setText(self.showNum)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())