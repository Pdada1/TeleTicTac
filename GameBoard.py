from Miniboard import MiniBoard
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
