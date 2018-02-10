"""

Kevin
Propose; OOP design aft verified
"""

from collections import namedtuple
from enum import Enum
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


################Type
class RoleType(Enum):
    BANKER = 0
    PLAYER1 = 1
    PLAYER2 = 2
    NON = 3

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
    STATION = 2
    CHANCE = 3
    JAIL = 4

Ground = namedtuple('Ground',['name', 'value', 'owner'])
SpecialGround = namedtuple('SpecialGround', ['name', 'type', 'Bonus', 'value', 'owner' ])
Role = namedtuple('Role',['name', 'cash', 'property'])
Size = namedtuple('Size', ['x_len', 'y_len'])
Point = namedtuple('Point', ['x', 'y'])
Bank = namedtuple('Bank',['name', 'cash', 'property'])
Rectangle = namedtuple('namedtuple', ['x_ul', 'y_ul', 'x_len', 'y_len'])


################Global Variables
WinSize = Size._make([800, 480])
CellSize = Size._make([80, 80])
PlayerNum = 2



###############Class
# type limit



class clayout:
    def __init__(self, winsize, cellsize, scheme=0):
        self.win_size = winsize
        self.cell_size = cellsize
        self.create_layout(scheme)

    def create_layout(self, scheme):
        win_p_ul = Point._make([0, 0])
        win_p_ur = Point._make([self.win_size.x_len, 0])
        win_p_dl = Point._make([0, self.win_size.y_len])
        win_p_dr = Point._make([self.win_size.x_len, self.win_size.y_len])
        p = win_p_ul
        dir = DirectionType.RIGHT
        i = 0
        layout_lst = []

        if scheme != 0:
            return layout_lst

        # if self.cell_size.x_len/self.win_size.x_len != 0 or self.cell_size.y_len/self.win_size.y_len != 0:
        #     return layout_lst

        while (1):
            layout_lst.append(Rectangle._make([p.x, p.y, self.cell_size.x_len, self.cell_size.y_len]))
            i = i + 1

            if p == win_p_ur and dir == DirectionType.RIGHT:
                dir = DirectionType.DOWN
            elif p == win_p_dr and dir == DirectionType.DOWN:
                dir = DirectionType.LEFT
            elif p == win_p_dl and dir == DirectionType.LEFT:
                dir = DirectionType.UP

            if dir == DirectionType.RIGHT:
                tmp = p.x + self.cell_size.x_len
                p = p._replace(x=tmp)
            elif dir == DirectionType.DOWN:
                tmp = p.y + self.cell_size.y_len
                p = p._replace(y=tmp)
            elif dir == DirectionType.LEFT:
                tmp = p.x - self.cell_size.x_len
                p = p._replace(x=tmp)
            else:
                tmp = p.y - self.cell_size.y_len
                p = p._replace(y=tmp)


            if p == win_p_ul and dir == DirectionType.UP:
                break

        self.lay_out = layout_lst
        return layout_lst

    def print_layout_lst(self):
        i = 0
        for p in self.lay_out:
            print('item ', i, ' pos: ', p.x_ul, p.y_ul)

class cinfo:
    def __init__(self):
        self.init_layout()
        self.init_ground()
        self.init_role()

    def init_layout(self):
        lay_out = clayout(WinSize, CellSize)
        self.layout_info = lay_out.create_layout(0)
        lay_out.print_layout_lst()

    def init_ground(self):
        pos_go = [0]
        pos_chance = [5,12]
        pos_jail = [17]
        pos_station = [2, 9, 15]
        self.grd_info = []

        i_street = 1
        i_chanece = 1
        i_station = 1
        item_num = (len(self.layout_info))
        i = 0
        while(i<item_num):

            if i in pos_go:
                self.grd_info.append(SpecialGround._make(['Go', GroundType.GO, 'add cash $300', 0, RoleType.NON]))
                i = i + 1
                continue

            if i in pos_chance:
                self.grd_info.append(SpecialGround._make(['Chance' + str(i_chanece), GroundType.CHANCE, 'random bouns', 0, RoleType.NON]))
                i_chanece = i_chanece + 1
                i = i + 1
                continue

            if i in pos_jail:
                self.grd_info.append(SpecialGround._make(['Jail', GroundType.CHANCE, 'hang up for a run', 0, RoleType.NON]))
                i = i + 1
                continue

            if i in pos_station:
                self.grd_info.append(Ground._make(['Station'+str(i_station), 300+i, RoleType.BANKER]))
                i_station = i_station + 1
                i = i + 1
                continue

            self.grd_info.append(Ground._make(['Station' + str(i_street), 300 + i, RoleType.BANKER]))
            i_street = i_street + 1
            i = i + 1



        # for g in self.grd_info:
        #     print(g.name)

    def init_role(self):
        self.player1 = Role._make(['Player1',200, []])
        self.player2 = Role._make(['Player2',200, []])
        self.bank = Bank._make(['theBank', 50000, []])

# Ground = namedtuple('Ground',['name', 'value', 'owner'])
# SpecialGround = namedtuple('SpecialGround', ['name', 'type', 'Bonus', ])
# Role = namedtuple('Role',['name', 'cash', 'property'])
# Size = namedtuple('Size', ['x_len', 'y_len'])
# Point = namedtuple('Point', ['x', 'y'])
# Bank = namedtuple('Bank',['name', 'cash', 'property'])
# Rectangle = namedtuple('namedtuple', ['x_ul', 'y_ul', 'x_len', 'y_len'])
import numpy.random as random
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

        #create_layout(WinSize, CellSize, layout_lst)
        info = cinfo()
        self.layout = info.layout_info
        self.ground_info = info.grd_info
        #print('size of ground_list', len(self.layout))
        i = 0
        for p in self.layout:

            info = ''

            if self.ground_info[i].value < 1:
                info = self.ground_info[i].name + '\n'
            else:
                info = self.ground_info[i].name + '\n' + '$' + str(self.ground_info[i].value)

            button = QPushButton(info, self)
            if self.ground_info[i].owner != RoleType.NON:
                tip = self.get_role_str(self.ground_info[i].owner)
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


        #create die roll
        self.die_btn = QPushButton('Roll', self)
        self.die_btn.move(200,240)
        self.die_btn.clicked.connect(self.on_die_click)
        self.die_label = QLabel('Die '+ str(self.roll_die(1)),self)
        self.die_label.move(200,200)

        self.show()
        print(self.roll_die(3))

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

    @pyqtSlot()
    def on_die_click(self):
        self.update_roll()

    def get_role_str(self, en_role):
        if en_role == RoleType.BANKER:
            return "Bank"
        elif en_role == RoleType.PLAYER1:
            return "Player1"
        elif en_role == RoleType.PLAYER2:
            return "Player2"

    def roll_die(self, die_num):
        res = 0
        for i in range(die_num):
            res = res + random.randint(1,6,1)
        return res

    def update_roll(self):
        self.die_label.setWindowTitle("23")
        print('roll update')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

