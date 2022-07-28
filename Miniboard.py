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
