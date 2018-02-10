"""
Author: Kevin
Propose: verify design
window size
"""
from collections import namedtuple
from enum import Enum
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class RoleType(Enum):
    BANKER = 0
    PLAYER1 = 1
    PLAYER2 = 2

class CornerType(Enum):
    UL = 0
    UR = 1
    DL = 2
    DR = 3

class DirectionType(Enum):
    RIGHT = 0
    LEFT = 1
    UP  = 2
    DOWN = 3

class GroundType(Enum):
    GO = 0
    STREET = 1
    SPECIAL = 2

Ground = namedtuple('Ground',['name', 'value', 'owner'])
Role = namedtuple('Role',['cash', 'property'])
Size = namedtuple('Size', ['x_len', 'y_len'])
Point = namedtuple('Point', ['x', 'y'])
Rectangle = namedtuple('namedtuple', ['x_ul', 'y_ul', 'x_len', 'y_len'])

Ground1 = Ground._make(['a', 30, RoleType.BANKER])
WinSize = Size._make([800, 480])
CellSize = Size._make([80, 80])
layout_lst = []
ground_list = []
all_role_list = []

def get_role_type_name(ROLE):
    if ROLE == RoleType.BANKER:
        return "bank"
    elif ROLE == RoleType.PLAYER1:
        return "player 1"
    elif ROLE == RoleType.PLAYER2:
        return "player 2"

def init_info():
    tot_cash = 50000
    player_cash = 200
    player_num = 2
    player_grd_lst = []

    grd_list = []
    layout_lst_tmp = []
    create_layout(WinSize, CellSize, layout_lst_tmp)
    grd_num = len(layout_lst_tmp)
    for i in range(grd_num):
        if i == 0:
            grd = Ground._make(['GO', 200, RoleType.BANKER])
            ground_list.append(grd)
            continue
        elif i%8 == 0:
            grd = Ground._make(['Special', 0, RoleType.BANKER])
            ground_list.append(grd)
            continue

        grd = Ground._make(['Street'+str(i), 100+i, RoleType.BANKER])
        ground_list.append(grd)


    for g in ground_list:
        print(g.name)


    banker = Role._make([tot_cash-player_num*player_cash, grd_list])
    all_role_list.append(banker)
    player1 = Role._make([player_cash, player_grd_lst])
    all_role_list.append(player1)
    player2 = Role._make([player_cash, player_grd_lst])
    all_role_list.append(player2)




def create_layout(winsize, cellsize, layout_lst):

    win_p_ul = Point._make([0,0])
    p = win_p_ul
    win_p_ur = Point._make([winsize.x_len,0])
    win_p_dl = Point._make([0, winsize.y_len])
    win_p_dr = Point._make([winsize.x_len, winsize.y_len])
    dir = DirectionType.RIGHT
    i = 0

    print('start loop')
    while(1):
        layout_lst.append(Rectangle._make([p.x, p.y, cellsize.x_len, cellsize.y_len]))
        #print("the ", i, " time:", p.x, p.y)
        i = i + 1

        if p == win_p_ur and dir == DirectionType.RIGHT:
            dir = DirectionType.DOWN
        elif p == win_p_dr and dir == DirectionType.DOWN:
            dir = DirectionType.LEFT
        elif p == win_p_dl and dir == DirectionType.LEFT:
            dir = DirectionType.UP

        if dir == DirectionType.RIGHT:
            tmp = p.x + cellsize.x_len
            #print('tmp', tmp)
            p = p._replace(x=tmp)#p.x = p.x + cellsize.x_len
        elif dir == DirectionType.DOWN:
            tmp = p.y + cellsize.y_len
            p = p._replace(y=tmp)
        elif dir == DirectionType.LEFT:
            tmp = p.x - cellsize.x_len
            p = p._replace(x=tmp)
        else:
            tmp = p.y - cellsize.y_len
            p = p._replace(y=tmp)

        if i > 500:
            break

        if p == win_p_ul and dir == DirectionType.UP :
            break


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Monpoly Game'
        self.left = 10
        self.top = 10
        self.width = 1368
        self.height = 720
        self.initUi()

    def initUi(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        create_layout(WinSize, CellSize, layout_lst)

        print('size of ground_list', len(ground_list))
        i = 0
        for p in layout_lst:
            info = ground_list[i].name + '\n' + get_role_type_name(ground_list[i].owner) + '\n' + '$' + str(ground_list[i].value)
            tip = ground_list[i].owner
            button = QPushButton(info, self)
            button.setToolTip(str(tip))
            x = p.x_ul
            y = p.y_ul
            x_size = p.x_len
            y_size = p.y_len
            button.move(x,y)
            button.setFixedHeight(y_size)
            button.setFixedWidth(x_size)
            if i == 2:
                button.setIcon(QIcon("red.png"))

            if i == 5:
                button.setIcon(QIcon("blue.jpeg"))


            button.clicked.connect(self.on_click)
            i = i + 1

        self.show()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

if __name__ == '__main__':
    init_info()
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())



    # i = 0
    # for p in layout_lst:
    #     print("item ", i, p.x_ul, p.y_ul)
    #     i = i + 1





