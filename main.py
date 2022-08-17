from GameBoard import GameBoard


class Main:
    position = " "
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
    while not test.checklegal(position[0], position[1]):  # error checking for legal moves
        position = Main.takeMove(counter % 2 + 1)
    test.playmove(position[0], position[1], counter % 2 + 1)
    test.printboard()
    counter += 1
    # first move sequence above
    while not win:
        # second player move repeating sequence
        if test.boardA[position[1]].geta() == ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'] or test.boardA[position[1]].geta() == [
            'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']:
            position = Main.takeMove(counter % 2 + 1)
            while not test.checklegal(position[0], position[1]):
                position = Main.takeMove(counter % 2 + 1)
        else:
            position = Main.takeMove2(counter % 2 + 1, position[1])
            while not test.checklegal(position[0], position[1]):
                position = Main.takeMove2(counter % 2 + 1, position[0])
        test.playmove(position[0], position[1], counter % 2 + 1)
        if test.boardA[position[0]].checkwin():
            win = test.checkwin()
        test.printboard()
            # first player move repeating sequence
        counter += 1
        print("bposition",test.boardA[position[1]].geta())
        print("position:", position[1])
        if test.boardA[position[1]].geta() == ['F','F','F','F','F','F','F','F','F'] or test.boardA[position[1]].geta() == ['S','S','S','S','S','S','S','S','S']:
            position = Main.takeMove(counter % 2 + 1)
            while not test.checklegal(position[0], position[1]):
                position = Main.takeMove(counter % 2 + 1)
        else:
            position = Main.takeMove2(counter % 2 + 1, position[1])
            while not test.checklegal(position[0], position[1]):
                position = Main.takeMove2(counter % 2 + 1, position[0])
        test.playmove(position[0], position[1], counter % 2 + 1)
        if test.boardA[position[0]].checkwin():
            win = test.checkwin()
        test.printboard()
        counter += 1


if __name__ == '__main__':
    main()
