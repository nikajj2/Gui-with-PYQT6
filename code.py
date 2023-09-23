import sys
import csv

x=list(csv.reader(open(sys.argv[1],'r')))
A=[]
for i in range(len(x)):
    for j in range(len(x[i])):
        z=[1,1,1,1]#z[0]->counts repetition on the left,z[1]->counts repetitions up
        #z[2]->up-left diagonal, z[3]->up-right diagonal
        if((j>0) and x[i][j]==x[i][j-1]):
            z[0]=A[len(A)-1][0]+1
        if((i>0) and x[i][j]==x[i-1][j]):
            z[1]=A[len(A)-len(x[1])][1]+1
        if((i>0)and(j>0) and x[i][j]==x[i-1][j-1]):
            z[2]=A[len(A)-len(x[1])-1][2]+1
        if((i>0)and(j<len(x[1])-1) and x[i][j]==x[i-1][j+1]):
            z[3]=A[len(A)-len(x[1])+1][3]+1
        #print(i,j, z)
        A.append(z);
#print(A)
max=1
row=0
col=0
for i in range(len(A)):
    for j in range(4):
        if A[i][j]>max:
            max=A[i][j]
            col=j
            row=i


#max_repetition=max
#max_i=row//len(x[1])
#max_j=row%len(x)
#max_direction=col

from PyQt6.QtCore import Qt, QPoint, QRect, QSize
from PyQt6.QtGui import QAction,QColor, QPalette
from PyQt6.QtWidgets import \
    (QApplication, QHBoxLayout, QLabel, QLayout, QMainWindow, QMenu,
     QVBoxLayout, QSizePolicy,QMenuBar, QPushButton, QWidget,QGridLayout)


class MainWindow(QMainWindow):

        def __init__(self):
            super().__init__()
            self.setWindowTitle('CSC 221 - HW 4')
            self.resize(50*len(x), 50*len(x[1]))
            self.max_repetition=max
            self.max_i=row//len(x[1])
            self.max_j=row%len(x)
            self.max_direction=col

        ## Setup the central widget
            self.widget = QWidget()
            self.central = QVBoxLayout()
            self.central.setSpacing(1)
            self.central.setContentsMargins(10,10,10,10)
            self.widget.setLayout(self.central)
            self.setCentralWidget(self.widget)
        
            self.layout_i = QGridLayout()
            self.layout_i.setSpacing(1)
            self.central.addLayout(self.layout_i)
            for i in range(len(x)):
                for j in range(len(x[1])):
                    self.layout_i.addWidget(Square(x[i][j],True),i,j)
            self.button = QPushButton('Solve')
            self.button.clicked.connect(self.buttonClicked)
            end=QVBoxLayout()
            end.addWidget(self.button)
            layout_button = QHBoxLayout()
            layout_button.setSpacing(0)
            self.central.addLayout(layout_button)
            layout_button.addLayout(end)
        def buttonClicked(self):
            if(self.max_direction==0):
                for i in range(self.max_repetition):
                    self.layout_i.addWidget(Square(x[self.max_i][self.max_j],False),self.max_i,self.max_j)
                    self.max_j-=1#move to the left
            elif(self.max_direction==1):
                for i in range(self.max_repetition):
                    self.layout_i.addWidget(Square(x[self.max_i][self.max_j],False),self.max_i,self.max_j)
                    self.max_i-=1#move up
            elif(self.max_direction==2):
                for i in range(self.max_repetition):
                    self.layout_i.addWidget(Square(x[self.max_i][self.max_j],False),self.max_i,self.max_j)
                    self.max_i-=1#move up-left diagonal
                    self.max_j-=1
            else :
                for i in range(self.max_repetition):
                    self.layout_i.addWidget(Square(x[self.max_i][self.max_j],False),self.max_i,self.max_j)
                    self.max_i-=1#move up-right diagonal
                    self.max_j+=1
                    
                    
            
class Square(QWidget):
    def __init__(self, title, active=True):
        super().__init__()
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor('white'))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        if active:
            palette.setColor(QPalette.ColorRole.Window, QColor('white'))
        else:
            palette.setColor(QPalette.ColorRole.Window, QColor('yellow'))
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        
        label=QLabel(title)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        layout = QHBoxLayout(self)
        layout.addWidget(label)
        layout.addStretch()



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()




 
