class GameBoard:
    boardA = []

    def __init__(self, ):
        for x in range(0, 9):
            y = MiniBoard()
            self.boardA.append(y)

    def printboard(self):
        for x in range(0, 9):
            print(self.boardA[x].geta())

    def checklegal(self, bcellnum, scellnum):
        if 9 > bcellnum > -1 and self.boardA[bcellnum].checklegal(scellnum):
            return True
        else:
            return False

    def playmove(self, bcellnum, scellnum, ptag):

        c = self.checklegal(bcellnum, scellnum)
        if c:
            self.boardA[bcellnum].setv(scellnum, ptag)
            print(self.boardA[bcellnum].getv(scellnum))
            return True
        else:
            return False

    def checkwin(self):
        if (self.checkDiagonal() == 1 or self.checkVertical() == 1 or self.checkHorizontal() == 1):
            print("The first player has won")
            return True
        if (self.checkDiagonal() == 2 or self.checkVertical() == 2 or self.checkHorizontal() == 2):
            print("The second player has won")
            return True

    def checkDiagonal(self):
        if str(self.boardA[0]) + str(self.boardA[4]) + str(self.boardA[8]) == ("FFF") or str(self.boardA[2]) + str(self.boardA[4]) + str(self.boardA[
            6]) == ("FFF"):
            return 1
        if str(self.boardA[0]) + str(self.boardA[4]) + str(self.boardA[8]) == ("SSS") or str(self.boardA[2]) + str(self.boardA[4]) + str(self.boardA[
            6]) == ("SSS"):
            return 2
        else:
            return False

    def checkVertical(self):
        for x in range(0, 3):
            if str(self.boardA[x]) + str(self.boardA[x + 3]) + str(self.boardA[x + 6]) == ("FFF"):
                return 1
            if str(self.boardA[x]) + str(self.boardA[x + 3]) + str(self.boardA[x + 6]) == ("SSS"):
                return 2
            else:
                return False

    def checkHorizontal(self):
        for x in range(0, 3):
            if str(self.boardA[3 * x]) + str(self.boardA[3 * + 1]) + str(self.boardA[3 * x + 2]) == ("FFF"):
                return 1
            if str(self.boardA[3 * x]) + str(self.boardA[3 * x + 1]) + str(self.boardA[3 * x + 2]) == ("SSS"):
                return 2
            else:
                return False


class MiniBoard:
    mboardA = []

    def __init__(self):
        self.mboardA = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def geta(self):
        return self.mboardA

    def getv(self, cellnum):
        return self.mboardA[cellnum]

    def setv(self, cellnum, ptag):
        self.mboardA[cellnum] = ptag

    def checklegal(self, cellnum):
        if 9 > cellnum > -1 and self.mboardA[cellnum] == 0:
            return True
        else:
            return False

    def checkwin(self):
        if (self.checkDiagonal() == 1 or self.checkHorizontal() == 1 or self.checkVertical() == 1):
            self.mboard = ["F"]
            return True
        if (self.checkDiagonal() == 2 or self.checkHorizontal() == 2 or self.checkVertical() == 2):
            self.mboard = ["S"]
            return True
        return False

    def checkDiagonal(self):
        if self.mboardA[0] + self.mboardA[4] + self.mboardA[8] == 3 or self.mboardA[2] + self.mboardA[4] + self.mboardA[
            6] == 3:
            return 1
        if self.mboardA[0] + self.mboardA[4] + self.mboardA[8] == 6 or self.mboardA[2] + self.mboardA[4] + self.mboardA[
            6] == 6:
            return 2
        return False

    def checkVertical(self):
        for x in range(0, 3):
            if self.mboardA[x] + self.mboardA[x + 3] + self.mboardA[x + 6] == 3:
                return 1
            if self.mboardA[x] + self.mboardA[x + 3] + self.mboardA[x + 6] == 6:
                return 2
            return False

    def checkHorizontal(self):
        for x in range(0, 3):
            if self.mboardA[3 * x] + self.mboardA[3 * + 1] + self.mboardA[3 * x + 2] == 3:
                return 1
            if self.mboardA[3 * x] + self.mboardA[3 * x + 1] + self.mboardA[3 * x + 2] == 6:
                return 2
            return False


def takeMove(ptag):
    return list(map(int, input("Player " + str(ptag) + " make a move").split()))


def takeMove2(ptag, board):
    return int(input("Player " + str(ptag) + " make a move for board "+str(board)))


def main():
    test = GameBoard()
    win = False
    counter = 1
    test.printboard()
    position = takeMove(counter)
    print(position)
    move = test.playmove(position[0], position[1], counter)
    while not move:
        position = list(map(int, input("Please enter a valid move, that move is illegal").split()))
        move = test.playmove(position[0], position[1], counter)
    counter = 2
    while not win:
        test.printboard()
        if test.boardA[position[0]] == ("F" or "S"):
            position = takeMove(counter)
            print(position)
            move = test.playmove(position[0], position[1], counter)
            while not move:
                position = input("Please enter a valid move, that move is illegal").split()
                move = test.playmove(position[0], position[1], counter)
            test.boardA[position].checkwin()
            win = test.checkwin()
        else:
            position2 = takeMove2(counter, position[1])
            move = test.playmove(position[1], position2, counter)
            while not move:
                position2 = input("Please enter a valid move, that move is illegal").split()
                move = test.playmove(position[1], position2, counter)
            test.boardA[position2].checkwin()
            win = test.checkwin()


if __name__ == '__main__':
    main()
