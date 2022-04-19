import sys
from PyQt5 import QtWidgets
class window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.write_area=QtWidgets.QLabel("not click yet...")
        self.buton =QtWidgets.QPushButton("!~ Push me ~!")
        self.count=0


        #vetical
        v_box =QtWidgets.QVBoxLayout()

        v_box.addWidget(self.buton)
        v_box.addWidget(self.write_area)
        v_box.addStretch()

        #horizontal
        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.buton.clicked.connect(self.click)

        self.show()
    def click(self):
        self.count +=1
        self.write_area.setText(str(self.count)+" time click me")

app = QtWidgets.QApplication(sys.argv)
window =window()
sys.exit(app.exec())
