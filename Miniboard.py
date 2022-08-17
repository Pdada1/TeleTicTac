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
            self.mboardA = ['F','F','F','F','F','F','F','F','F']
            return True
        if (self.checkDiagonal() == 2 or self.checkHorizontal() == 2 or self.checkVertical() == 2):
            self.mboardA = ['S','S','S','S','S','S','S','S','S']
            return True
        return False

    def checkDiagonal(self):
        if str(self.mboardA[0]) + str(self.mboardA[4]) + str(self.mboardA[8]) == "111" or str(self.mboardA[2]) + str(self.mboardA[4]) + str(self.mboardA[6]) == "111":
            return 1
        if str(self.mboardA[0]) + str(self.mboardA[4]) + str(self.mboardA[8]) == "222" or str(self.mboardA[2]) + str(self.mboardA[4]) + str(self.mboardA[6]) == "222":
            return 2
        return False

    def checkVertical(self):
        for x in range(0, 3):
            if str(self.mboardA[x]) + str(self.mboardA[x + 3]) + str(self.mboardA[x + 6]) == "111":
                return 1
            if str(self.mboardA[x]) + str(self.mboardA[x + 3]) + str(self.mboardA[x + 6]) == "222":
                return 2
        return False

    def checkHorizontal(self):
        for x in range(0, 3):
            if str(self.mboardA[3 * x]) + str(self.mboardA[3 * + 1]) + str(self.mboardA[3 * x + 2]) == "111":
                return 1
            if str(self.mboardA[3 * x]) + str(self.mboardA[3 * + 1]) + str(self.mboardA[3 * x + 2]) == "222":
                return 2
        return False
