"""

Kevin
Propose; OOP design aft verified
"""

from collections import namedtuple
from enum import Enum
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


################Type
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
    STATION = 2
    CHANCE = 3
    JAIL = 4

Ground = namedtuple('Ground',['name', 'value', 'owner'])
Role = namedtuple('Role',['cash', 'property'])
Size = namedtuple('Size', ['x_len', 'y_len'])
Point = namedtuple('Point', ['x', 'y'])
Rectangle = namedtuple('namedtuple', ['x_ul', 'y_ul', 'x_len', 'y_len'])
WinSize = Size._make([800, 480])
CellSize = Size._make([80, 80])

################Global Variables




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
    def 

if __name__ == '__main__':
    lay_out = clayout(WinSize, CellSize)
    lay_out_lst = lay_out.create_layout(0)
    lay_out.print_layout_lst()

