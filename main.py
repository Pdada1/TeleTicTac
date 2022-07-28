import GameBoard
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
