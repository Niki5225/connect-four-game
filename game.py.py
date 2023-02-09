class Value(Exception):
    pass


class Index(Exception):
    pass


def reset_matrix():
    new_matrix = []
    for _ in range(rows):
        new_matrix.append([0] * cols)
    return new_matrix


def value_error():
    counter = 0
    choice = None

    while counter < 4:
        new_choice = input()
        if new_choice.isdigit():
            choice = int(new_choice)
            break
        else:
            counter += 1

    if counter > 3:
        return True
    else:
        return choice


def index_error():
    counter = 0
    choice = None

    while counter < 4:
        new_choice = input()
        if new_choice.isdigit() < cols - 1:
            choice = int(new_choice)
            break
        else:
            counter += 1

    if counter > 3:
        print("You gave coordinates, which are out of the matrix too many times. Restart and try again.")
        return True
    else:
        return choice


def move(matrix, choice, player):
    found_the_first_upper_row = False

    for row in range(len(matrix) - 1, -1, -1):
        if matrix[row][choice - 1] == 0:
            matrix[row][choice - 1] = player
            break
        elif matrix[row][choice - 1] == 1 or matrix[row][choice - 1] == 2:
            for r in range(len(matrix) - 1, -1, -1):
                if matrix[r][choice - 1] == 0:
                    matrix[r][choice - 1] = player
                    found_the_first_upper_row = True
                    break
        if found_the_first_upper_row:
            break
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(*row)


def check_if_won(matrix):
    for row in range(len(matrix) - 1, -1, -1):
        for col in range(0, len(matrix[row]) - 4):
            if matrix[row][col] == 1:
                if matrix[row][col + 1] == 1 and matrix[row][col + 2] == 1 and matrix[row][col + 3] == 1:
                    print("The winner is player 1\n")
                    return True
            elif matrix[row][col] == 2:
                if matrix[row][col + 1] == 2 and matrix[row][col + 2] == 2 and matrix[row][col + 3] == 2:
                    print("The winner is player 2\n")
                    return True

    for row in range(len(matrix) - 1, 2, -1):
        for col in range(0, len(matrix[row]) - 1):
            if matrix[row][col] == 1:
                if matrix[row - 1][col] == 1 and matrix[row - 2][col] == 1 and matrix[row - 3][col] == 1:
                    print("The winner is player 1\n")
                    return True
            elif matrix[row][col] == 2:
                if matrix[row - 1][col] == 2 and matrix[row - 2][col] == 2 and matrix[row - 3][col] == 2:
                    print("The winner is player 2\n")
                    return True

    for row in range(len(matrix) - 1, 2, -1):
        for col in range(0, len(matrix[row]) - 3):
            if matrix[row][col] == 1:
                if matrix[row - 1][col + 1] == 1 and matrix[row - 2][col + 2] == 1 and matrix[row - 3][col + 3] == 1:
                    print("The winner is player 1\n")
                    return True
            elif matrix[row][col] == 2:
                if matrix[row - 1][col + 1] == 2 and matrix[row - 2][col + 2] == 2 and matrix[row - 3][col + 3] == 2:
                    print("The winner is player 2\n")
                    return True

    for row in range(len(matrix) - 1, 2, -1):
        for col in range(len(matrix[row]) - 1, 2, -1):
            if matrix[row][col] == 1:
                if matrix[row - 1][col - 1] == 1 and matrix[row - 2][col - 2] == 1 and matrix[row - 3][col - 3] == 1:
                    print("The winner is player 1\n")
                    return True
            elif matrix[row][col] == 2:
                if matrix[row - 1][col - 1] == 2 and matrix[row - 2][col - 2] == 2 and matrix[row - 3][col - 3] == 2:
                    print("The winner is player 2\n")
                    return True


rows, cols = 6, 7
matrix = []

for _ in range(rows):
    matrix.append([0] * cols)

winner1 = False
winner2 = False
won_games1 = 0
won_games2 = 0

while True:
    start_or_end_command = input()
    if start_or_end_command == "Exit":
        print("\nHave a nice day!")
        exit()
    elif start_or_end_command != "Start":
        print("Invalid command!")
        continue
    else:
        print("Welcome to my game!\n")
        break

while won_games1 < 5 and won_games2 < 5:
    choice1 = input("Player 1, choose a column\n")
    if choice1 == "Exit":
        print("Have a nice day!")
        exit()
    if choice1.isalpha():
        choice1 = value_error()
        if type(choice1) == bool or choice1 > cols - 1:
            print("You gave coordinates, which are out of the matrix too many times. Restart and try again.")
            raise Value
    elif int(choice1) > cols:
        choice1 = index_error()
        if type(choice1) == bool or choice1 > cols - 1:
            print("You gave coordinates which are outside of the matrix too many times. Restart and try again")
            raise Index

    matrix = move(matrix, int(choice1), 1)
    print_matrix(matrix)
    winner1 = check_if_won(matrix)

    if winner1:
        winner1 = False
        won_games1 += 1
        matrix = reset_matrix()
        continue

    choice2 = input("Player 1, choose a column\n")
    if choice2 == "Exit":
        print("Have a nice day!")
        exit()

    if choice2.isalpha():
        choice2 = value_error()
        if type(choice2) == bool or choice2 > cols - 1:
            print("You gave coordinates, which are out of the matrix too many times. Restart and try again.")
            raise Value

    if int(choice2) > cols:
        choice2 = index_error()
        if type(choice1) == bool or choice2 > cols - 1:
            print("You gave coordinates which are outside of the matrix too many times. Restart and try again")
            raise Index

    matrix = move(matrix, int(choice2), 2)
    print_matrix(matrix)
    winner2 = check_if_won(matrix)

    if winner2:
        winner2 = False
        won_games2 += 1
        matrix = reset_matrix()
