"""
ui core of monpoly

&1 2018-2-4 Kevin
   create monpoly place display
&2 2018-2-4 Kevin
   create a list to display a group of places
&2 2018-2-4 Kevin
   organize layout of display

Author: Kevin
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QLabel, QApplication,QVBoxLayout, QWidget, QPushButton, QHBoxLayout,QGroupBox, QGridLayout
from PyQt5.QtGui import QIcon
from enum import Enum
from numpy import ndarray

nUiLocationX = 300
nUiLocationY = 300
nUiSizeX = 1200
nUiSizeY = 800
szUiTiele = "Monpoly"
szUiIcoPath = 'web.png'


class Color(Enum):
    R = 1
    Y = 2
    G = 3
class PlaceType(Enum):
    PLACE = 0
    STREET = 1
    STATION = 2


class UI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(nUiLocationX, nUiLocationY, nUiSizeX, nUiSizeY)
        self.setWindowTitle(szUiTiele)
        self.setWindowIcon(QIcon(szUiIcoPath))

        self.place = []
        self.place_info = []

        self.createLayout2()
        # windowLayout = QVBoxLayout()
        # windowLayout.addWidget(self.horizontalGroupBox)
        # self.setLayout(windowLayout)


        print("size of place list is ", len(self.place))

        self.show()

    def createLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
        self.place_info = createDefPlaceList(9)

        nIdx = 0
        for i in range(0, 2):
            for j in range(0, 2):
                layout.addWidget(QPushButton(self.place_info[nIdx].getInfo()), i,j) #self.place_info[nIdx].getInfo()
                nIdx = nIdx + 1

        self.horizontalGroupBox.setLayout(layout)

    def createLayout2(self):
        grid = QGridLayout()
        self.setLayout(grid)
        nLayoutRow = 4
        nLayoutCol = 5
        szLayout = ['0', '1', '2', '3', '4',
                    '13', '', '', '',   '5',
                    '12', '', '', '',    '6',
                    '11', '10', '9', '8', '7']
        lstPlaceInfo = []
        for i in range(0, 14):
            p_info = PlaceInfo('place', Color.R, '300', '120', 'banker')
            lstPlaceInfo.append(p_info)

        layoutMap = self.createLayoutMap(nLayoutRow,nLayoutCol, [nUiSizeX, nUiSizeY])
        i = 0
        j = 0
        btn = QPushButton(lstPlaceInfo[10].getInfo(), self)
        btn.resize(30,30)

    def createLayout3(self):


    def createLayoutMap(self, nRow, nCol, nWindowSize):
        [nTotSizeX,nTotSizeY] = nWindowSize
        nStepX = nTotSizeX/nCol
        nStepY = nTotSizeY/nRow

        tdPosMap = ndarray((nRow, nCol))
        for i in range(nRow):
            for j in range(nCol):
                tdPosMap[i][j] = 1#[i*nStepX, j*nStepY]

        print(len(tdPosMap))
        return tdPosMap





class PlaceInfo:
    def __init__(self, szType, enColGrp, szSaleVal, szMorVal, szOwner):
        self.type = szType
        self.col = enColGrp
        self.svalue = szSaleVal
        self.mvalue = szMorVal
        self.owner = szOwner

    def getInfo(self):
        szInfo =  self.type + '\n' + self.svalue + '\n' + self.owner
        return  szInfo

    def getColor(self):
        return self.col

def createPlace(obj, szTit, nLocx, nLocy, nSizex, nSizey):
    btn = QPushButton(szTit, obj)
    btn.setGeometry(nLocx, nLocy, nSizex, nSizey)
    return btn

def createDefPlaceList(nNum):
    lstPlaceInfo = []
    for i in range(0, nNum):
        p_info = PlaceInfo('place', Color.R, '300', '120', 'banker')
        lstPlaceInfo.append(p_info)
        #print('new records')

    return lstPlaceInfo



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())
