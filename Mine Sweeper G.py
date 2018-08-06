# from tkinter import *
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter.ttk import *
from tkinter import font as tkFont
from PIL import Image
from random import randint

class Tile(object):
    bomb = False
    clicked = False
    numb = 0

    def __init__(self):
        self.bomb = False
        self.clicked = False

    def is_bomb(self):
        return self.bomb

    def set_bomb(self, bomb):
        self.bomb = bomb
        if bomb:
            self.numb = 9

    def click(self):
        self.clicked = True

    def is_clicked(self):
        return self.clicked

    def set_numb(self, numb):
        self.numb = numb

    def get_numb(self):
        return self.numb


class Game(object):
    board = []
    rows = 0
    cols = 0
    bombs = 0
    dead = None

    def __init__(self, rows, cols, bombs):
        if bombs > rows*cols:
            exit()
        self.dead = False
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        self.makeBoard()

    def startGame(self):
        self.printBoard()
        print("Enter \'X Y\' to click a tile...\n")
        while not self.dead:
            if len(self.board)-self.bombs == self.count_clicked():
                print("You Win!!!")
                exit()

            input_xy = [int(x) for x in input().split(" ")]
            if input_xy[0] >= self.cols or input_xy[1] >= self.rows:
                print("A given input is out of bounds, try again... ")
            else:
                bomb_numb = self.guess(input_xy)
                # if bomb_numb == None:
                #     self.dead = True
                # else:
                #     self.board[input_xy[1]*self.cols + input_xy[0]].set_numb(bomb_numb)

                self.printBoard()
        print("Game Over")

    def guess(self, xy):
        if self.board[xy[1]*self.cols + xy[0]].is_bomb():
            self.board[xy[1]*self.cols + xy[0]].click()
            self.dead = True
            return None
        self.board[xy[1]*self.cols + xy[0]].click()

        bomb_numb = 0
        if (xy[1]+1) < self.rows and self.board[(xy[1]+1)*self.cols + xy[0]].is_bomb():
            bomb_numb += 1
        if (xy[1]-1) >= 0 and self.board[(xy[1]-1)*self.cols + xy[0]].is_bomb():
            bomb_numb += 1
        if (xy[0]+1) < self.cols and self.board[xy[1]*self.cols + (xy[0]+1)].is_bomb():
            bomb_numb += 1
        if (xy[0]-1) >= 0 and self.board[xy[1]*self.cols + (xy[0]-1)].is_bomb():
            bomb_numb += 1
        if (xy[0]+1) < self.cols and (xy[1]+1) < self.rows and self.board[(xy[1]+1)*self.cols + (xy[0]+1)].is_bomb():
            bomb_numb += 1
        if (xy[1]-1) >= 0 and (xy[0]-1) >= 0 and self.board[(xy[1]-1)*self.cols + (xy[0]-1)].is_bomb():
            bomb_numb += 1
        if (xy[1]+1) < self.rows and (xy[0]-1) >= 0 and self.board[(xy[1]+1)*self.cols + (xy[0]-1)].is_bomb():
            bomb_numb += 1
        if (xy[1]-1) >= 0 and (xy[0]+1) < self.cols and self.board[(xy[1]-1)*self.cols + (xy[0]+1)].is_bomb():
            bomb_numb += 1
        # self.board[xy[1]*self.cols + xy[0]].set_numb(bomb_numb)

        if bomb_numb == 0:
            x = xy[0]
            y = xy[1]+1
            if x >= 0 and x < self.cols and y >= 0 and y < self.rows and not self.board[y*self.cols + x].is_clicked():
                    numb = self.guess([x, y])
                    if numb != None:
                        self.board[y*self.cols + x].set_numb(numb)

            x = xy[0]
            y = xy[1]-1
            if x >= 0 and x < self.cols and y >= 0 and y < self.rows and not self.board[y*self.cols + x].is_clicked():
                    numb = self.guess([x, y])
                    if numb != None:
                        self.board[y*self.cols + x].set_numb(numb)

            x = xy[0]+1
            y = xy[1]
            if x >= 0 and x < self.cols and y >= 0 and y < self.rows and not self.board[y*self.cols + x].is_clicked():
                    numb = self.guess([x, y])
                    if numb != None:
                        self.board[y*self.cols + x].set_numb(numb)

            x = xy[0]-1
            y = xy[1]
            if x >= 0 and x < self.cols and y >= 0 and y < self.rows and not self.board[y*self.cols + x].is_clicked():
                    numb = self.guess([x, y])
                    if numb != None:
                        self.board[y*self.cols + x].set_numb(numb)

            x = xy[0]+1
            y = xy[1]+1
            if x >= 0 and x < self.cols and y >= 0 and y < self.rows and not self.board[y*self.cols + x].is_clicked():
                    numb = self.guess([x, y])
                    if numb != None:
                        self.board[y*self.cols + x].set_numb(numb)

            x = xy[0]-1
            y = xy[1]-1
            if x >= 0 and x < self.cols and y >= 0 and y < self.rows and not self.board[y*self.cols + x].is_clicked():
                    numb = self.guess([x, y])
                    if numb != None:
                        self.board[y*self.cols + x].set_numb(numb)

            x = xy[0]+1
            y = xy[1]-1
            if x >= 0 and x < self.cols and y >= 0 and y < self.rows and not self.board[y*self.cols + x].is_clicked():
                    numb = self.guess([x, y])
                    if numb != None:
                        self.board[y*self.cols + x].set_numb(numb)

            x = xy[0]-1
            y = xy[1]+1
            if x >= 0 and x < self.cols and y >= 0 and y < self.rows and not self.board[y*self.cols + x].is_clicked():
                    numb = self.guess([x, y])
                    if numb != None:
                        self.board[y*self.cols + x].set_numb(numb)

        # return bomb_numb
        self.board[xy[1]*self.cols + xy[0]].set_numb(bomb_numb)

    def makeBoard(self):
        for i in range(0, self.rows*self.cols):
            self.board.append(Tile())

        bombPos = []
        while len(bombPos) < self.bombs:
            bi = randint(0, len(self.board)-1)
            if bi not in bombPos:
                bombPos.append(bi)

        for i in bombPos:
            self.board[i].set_bomb(True)

    def printBoardBombs(self):
        for y in range(0, self.rows):
            string = "["
            for x in range(0, self.cols):
                string += str(int(self.board[y*self.cols + x].is_bomb()))
                if x < self.cols - 1:
                    string = string + ", "
            print(string + "]")

    def printBoard(self):
        string = "   X "
        for x in range(0, self.cols):
            string += str(x) + " "
        print(string)
        string = "Y    "
        for x in range(0, self.cols):
            string += "| "
        print(string)
        for y in range(0, self.rows):
            string = str(y) + " -- "
            for x in range(0, self.cols):
                if self.board[y*self.cols + x].is_clicked():
                    if self.board[y*self.cols + x].is_bomb():
                        string += "X"
                    else:
                        string += str(self.board[y*self.cols + x].get_numb())
                else:
                    string += "@"
                if x < self.cols - 1:
                    string = string + " "
            print(string)

    def count_clicked(self):
        numb = 0
        for tile in self.board:
            if tile.is_clicked():
                numb += 1
        # print(numb)
        return numb

class Window(Frame):
    startColor = "Grey"
    LCColor = "White"
    RCColor = "Red"

    # Change size of grid and number of bombs here
    rows = 10
    cols = 10
    bombs = 10

    grid = {}

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Mine Sweeper")

        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        self.game = Game(self.rows, self.cols, self.bombs)
        # game.startGame()

        for x in range(self.cols):
            self.columnconfigure(x, pad=1)

        for x in range(self.rows):
            self.rowconfigure(x, pad=1)

        # cls = Button(self, text="")
        for y in range(self.rows):
            for x in range(self.cols):
                btn = tk.Button(self, width="3", height="1", bg=self.startColor)
                btn.bind("<Button-1>", self.leftClick)
                btn.bind("<Button-3>", self.rightClick)
                btn.grid(row=y, column=x)
                self.grid[(x,y)] = btn

        self.pack()
        self.colorGrid()

    def gameStatus(self):
        if self.game.dead:
            for coor, btn in self.grid.items():
                btn.configure(bg="Black", state=DISABLED)
            top = Toplevel()
            top.title("Game Over")

            msg = Message(top, text="You Lose: You hit a bomb, better luck next time!")
            msg.pack()

            button = tk.Button(top, text="Okay", command=self.master.destroy)
            button.pack()
        elif len(self.game.board)-self.game.bombs == self.game.count_clicked():
            for coor, btn in self.grid.items():
                btn.configure(bg="Black", state=DISABLED)
            top = Toplevel()
            top.title("You Win")

            msg = Message(top, text="You Win: Nice Job!")
            msg.pack()

            button = tk.Button(top, text="Okay", command=self.master.destroy)
            button.pack()

    # Clicking the button means that you don't think there is a bomb there, if there isn't a bomb
    # then it will open the space and show you how many bombs are near. If it was a bomb then you
    # will lose the game!
    def leftClick(self, event):
        # print("leftClick")
        caller = event.widget
        bcolor = caller.cget("bg")
        if bcolor == self.startColor:
            # self.game.guess([x,y])
            # caller.configure(bg=self.LCColor, text="", state=DISABLED)
            for coor, btn in self.grid.items():
                if btn == caller:
                    self.game.guess(coor)
                    self.gameStatus()
                    break
            self.colorGrid()

    # Marks which spots you think are bombs and makes that button untargetable by a left click
    # until you right click it again, making it targetable.
    def rightClick(self, event):
        # print("rightClick")
        caller = event.widget
        bcolor = caller.cget("bg")
        if bcolor == self.LCColor:
            return
        elif bcolor == self.RCColor:
            caller.configure(bg=self.startColor)
        else:
            caller.configure(bg=self.RCColor)

    def colorGrid(self):
        for index in range(len(self.game.board)):
            if self.game.board[index].is_clicked():
                self.grid[(index%self.cols,int(index/self.cols))].configure(bg=self.LCColor, text=self.game.board[index].numb, state=DISABLED)


        # frame=Frame(self.master)
        # Grid.rowconfigure(self.master, 0, weight=1)
        # Grid.columnconfigure(self.master, 0, weight=1)
        # frame.grid(row=0, column=0, sticky=N+S+E+W)
        # grid=Frame(frame)
        # grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
        # Grid.rowconfigure(frame, 7, weight=1)
        # Grid.columnconfigure(frame, 0, weight=1)
        #
        # #example values
        # for x in range(10):
        #     for y in range(5):
        #         btn = Button(frame)
        #         btn.grid(column=x, row=y, sticky=N+S+E+W)
        #
        # for x in range(10):
        #   Grid.columnconfigure(frame, x, weight=1)
        #
        # for y in range(5):
        #   Grid.rowconfigure(frame, y, weight=1)

root = Tk()
app = Window(root)
root.mainloop()
