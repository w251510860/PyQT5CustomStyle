import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QFrame
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个 Figure 和一个 FigureCanvas 对象
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # 创建一个 Frame 并将 FigureCanvas 放入其中
        self.frame = QFrame()
        self.frame.setFrameStyle(QFrame.Panel | QFrame.Plain)
        self.frame.setLayout(QVBoxLayout())
        self.frame.layout().addWidget(self.canvas)

        # 设置窗口的中心小部件
        self.setCentralWidget(self.frame)

        # 绘制一个简单的图形
        self.ax = self.figure.add_subplot(111)
        self.ax.plot([1, 2, 3], [1, 4, 9])

    def show(self):
        super().show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
