from GameBoard import GameBoard


class Main:
    def takeMove(ptag):
        return list(map(int, input("Player " + str(ptag) + " make a move").split()))

    def takeMove2(ptag, board):
        return list(map(int, (board, input("Player " + str(ptag) + " make a move for board " + str(board)))))


def main():
    test = GameBoard()
    win = False
    counter = 0
    test.printboard()
    position = Main.takeMove(counter % 2 + 1)
    print(position)
    test.playmove(position[0], position[1], counter % 2 + 1)
    test.printboard()
    counter += 1
    while not win:
        position = Main.takeMove2(counter % 2 + 1, position[1])
        test.playmove(position[0], position[1], counter % 2 + 1)
        test.printboard()
        counter+=1
        position = Main.takeMove2(counter % 2 + 1, position[1])
        test.playmove(position[0], position[1], counter % 2 + 1)
        test.printboard()


if __name__ == '__main__':
    main()
