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

            input_check = input().split(" ")
            if len(input_check) != 2 or not input_check[0].isdigit() or not input_check[1].isdigit():
                print("Enter \'X Y\' to click a tile...")
                continue
            input_xy = [int(x) for x in input_check]
            if input_xy[0] >= self.cols or input_xy[1] >= self.rows:
                print("A given input is out of bounds, try again... ")
            else:
                bomb_numb = self.guess(input_xy)
                if bomb_numb == None:
                    self.dead = True
                else:
                    self.board[input_xy[1]*self.cols + input_xy[0]].set_numb(bomb_numb)

                self.printBoard()
        print("Game Over")

    def guess(self, xy):
        if self.board[xy[1]*self.cols + xy[0]].is_bomb():
            self.board[xy[1]*self.cols + xy[0]].click()
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

        return bomb_numb

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
        print("Tiles opened: " + str(numb))
        return numb

# Change size of grid and number of bombs here
rows = 10
cols = 10
bombs = 10

game = Game(rows, cols, bombs)
game.startGame()
