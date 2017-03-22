import random

# empty
sudoku_empty = [
1,2,3,4,5,6,7,8,9,
0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,
8,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0
]

# multiple
sudoku_multiple = [
0,8,0,0,0,9,7,4,3,
0,5,0,0,0,8,0,1,0,
0,1,0,0,3,0,0,0,0,
8,0,0,0,0,5,0,0,0,
0,0,0,8,0,4,0,0,0,
0,0,0,3,0,0,0,0,6,
0,0,0,0,0,0,0,7,0,
0,3,0,5,0,0,0,8,0,
9,7,2,4,0,0,0,5,0
]

#unsolvable
sudoku_unsolvable = [
4,6,1,2,9,5,8,7,3,
2,7,9,3,1,8,6,4,5,
8,3,5,6,4,7,9,2,1,
6,9,4,7,8,1,5,3,2,
7,5,2,4,3,6,1,8,9,
3,1,8,5,2,9,7,6,4,
1,4,7,9,6,3,2,5,8,
9,2,6,8,5,4,3,1,7,
5,8,3,1,7,2,9,9,0
]

sudoku_solved = [
4,6,1,2,9,5,8,7,3,
2,7,9,3,1,8,6,4,5,
8,3,5,6,4,7,9,2,1,
6,9,4,7,8,1,5,3,2,
7,5,2,4,3,6,1,8,9,
3,1,8,5,2,9,7,6,4,
1,4,7,9,6,3,2,5,8,
9,2,6,8,5,4,3,1,7,
5,8,3,1,7,2,4,9,6
]

sudoku_sample = [
0,6,0,2,0,0,8,0,0,
0,0,0,3,1,8,6,4,0,
0,0,5,0,0,0,0,0,0,
0,9,0,7,8,0,0,3,0,
7,0,0,0,3,0,0,0,9,
0,1,0,0,2,9,0,6,0,
0,0,0,0,0,0,2,0,0,
0,2,6,8,5,4,0,0,0,
0,0,3,0,0,2,0,9,0
]

'''
def test(list, sudoku_for_listcheck):  # checks if the given 9 member list (row, column or block) is valid
    if set(range(10)) != set(list):
        print(list, ' test failed')
        return 0
    if list.count(sudoku_for_listcheck[n]) > 1:
        return 0
'''


def create_filled_sudoku():
    clean_list = []
    for i in range(1, 10):
        clean_list.append(i)

    sudoku_filled = []

    for i in range(1, 83):
        sudoku_filled.append(0)
    # print(sudoku)

    sudoku_possible = []

    for i in range(1, 83):
        sudoku_possible.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # print(sudoku_possible)

    n = 0
    while n <= 80:
        while sudoku_possible[n] != []:
            printsudoku(sudoku_filled)
            print('n ', n, 'lehet ', sudoku_possible[n])
            sudoku_filled[n] = sudoku_possible[n][random.randint(0, len(sudoku_possible[n])-1)]
            print('n ', n, sudoku_filled[n])
            # input()
            if check(sudoku_filled, n) == 1:
                n += 1
                print(n)
                if n > 81:
                    printsudoku(sudoku_filled)
                    return(sudoku_filled)
                # input()
            else:
                sudoku_possible[n].remove(sudoku_filled[n])
                printsudoku(sudoku_filled)
                print(n, sudoku_possible[n])
                # input()
                sudoku_filled[n] = 0
        sudoku_possible[n] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(sudoku_possible)
        sudoku_filled[n] = 0
        n -= 1
        sudoku_possible[n].remove(sudoku_filled[n])
        print('n ', n, 'lehet ', sudoku_possible[n])
    printsudoku(sudoku_filled)


def check(sudoku_to_check, slot):  # testing the filled sudoku
    testlist = []
    result = 1

    # test rows
    for i in range(9):
        testlist = []
        for j in range(9):
            testlist.append(sudoku_to_check[j+i*9])
        if testlist.count(sudoku_to_check[slot]) > 1:
            result = 0
            break
    # print('row result ', result)

    testlist = []
    # test columns
    if result == 1:
        for i in range(9):
            testlist = []
            for j in range(9):
                testlist.append(sudoku_to_check[i+j*9])
            if testlist.count(sudoku_to_check[slot]) > 1:
                result = 0
                # print(result)
                break
    # print('column result', result)

    if result == 1:
        testlist = []
        # test cubes
        for i in range(0, 81, 27):
            if result == 1:
                for j in range(0, 9, 3):
                        testlist = []
                        testlist.append(sudoku_to_check[i+j])
                        testlist.append(sudoku_to_check[i+j+1])
                        testlist.append(sudoku_to_check[i+j+2])
                        testlist.append(sudoku_to_check[i+j+9])
                        testlist.append(sudoku_to_check[i+j+10])
                        testlist.append(sudoku_to_check[i+j+11])
                        testlist.append(sudoku_to_check[i+j+18])
                        testlist.append(sudoku_to_check[i+j+19])
                        testlist.append(sudoku_to_check[i+j+20])
                        if testlist.count(sudoku_to_check[slot]) > 1:
                            result = 0
                            # print(result)
                            break
                        testlist = []

        # print('cube result ', result)

    return result


def printsudoku(sudoku_to_print):
    print("   \033[1;32mA B C   D E F   G H I\033[;m")  # columns
    for i in range(3):
        for row in range(0, 3):
                print("\033[1;32m"+str((i*3)+(row+1))+"\033[;m", ' ', end='')  # rows
                print(sudoku_to_print[i*27+row*9], end='')
                print(' ', end='')
                print(sudoku_to_print[i*27+row*9+1], end='')
                print(' ', end='')
                print(sudoku_to_print[i*27+row*9+2], end='')
                print(' ', end='  ')
                print(sudoku_to_print[i*27+row*9+3], end='')
                print(' ', end='')
                print(sudoku_to_print[i*27+row*9+4], end='')
                print(' ', end='')
                print(sudoku_to_print[i*27+row*9+5], end='')
                print(' ', end='  ')
                print(sudoku_to_print[i*27+row*9+6], end='')
                print(' ', end='')
                print(sudoku_to_print[i*27+row*9+7], end='')
                print(' ', end='')
                print(sudoku_to_print[i*27+row*9+8], end='')
                print()
        print()


def test_for_set(sudoku_sets):
    testlist = []
    result = 1

    # test rows
    for i in range(9):
        testlist = []
        for j in range(9):
            testlist.append(sudoku_sets[j+i*9])
        # print(set(testlist), set(range(1, 10)))
        if set(testlist) != set(range(1, 10)):
            result = 0
            # print('set test row result ', result)
            return result
    # print('set row result ', result)

    testlist = []
    # test columns
    if result == 1:
        for i in range(9):
            testlist = []
            for j in range(9):
                testlist.append(sudoku_sets[i+j*9])
            if set(testlist) != set(range(1, 10)):
                result = 0
                # print('set test column result ', result)
                return result
    # print('set column result', result)

    if result == 1:
        testlist = []
        # test cubes
        for i in range(0, 81, 27):
            if result == 1:
                for j in range(0, 9, 3):
                        testlist = []
                        testlist.append(sudoku_sets[i+j])
                        testlist.append(sudoku_sets[i+j+1])
                        testlist.append(sudoku_sets[i+j+2])
                        testlist.append(sudoku_sets[i+j+9])
                        testlist.append(sudoku_sets[i+j+10])
                        testlist.append(sudoku_sets[i+j+11])
                        testlist.append(sudoku_sets[i+j+18])
                        testlist.append(sudoku_sets[i+j+19])
                        testlist.append(sudoku_sets[i+j+20])
                        if set(testlist) != set(range(1, 10)):
                            result = 0
                            # print('set test cube result ', result)
                            return result
                        testlist = []

        # print('set test cube result ', result)

    return result


def sudoku_solver(sudoku_to_solve):
    predefined = []  # creates a list thet has the index of the predefined numbers
    for i in range(len(sudoku_to_solve)):
        if sudoku_to_solve[i] != 0:
            predefined.append(i)

    sudoku_possible = []
    for i in range(0, 81):
        if i not in predefined:
            sudoku_possible.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
        else:
            list = []
            list.append(sudoku_to_solve[i])
            sudoku_possible.append(list)
            list = []

    n = 0
    while n <= 80:
        while sudoku_possible[n] != []:
            # printsudoku(sudoku_to_solve)
            while n in predefined:
                n += 1
                # print('n ', n, 'lehet ', sudoku_possible[n])
            if n > 80:
                if test_for_set(sudoku_to_solve) == 1:
                    # printsudoku(sudoku_to_solve)
                    # print('Solved to solve')
                    # input()
                    return 'Solved'   # raise SystemExit()

                else:
                    return 'Unsolvable1'    # raise SystemExit()
            sudoku_to_solve[n] = sudoku_possible[n][0]
            # print('n ', n, sudoku_to_solve[n])
            if check(sudoku_to_solve, n) == 1:
                if n >= 80:
                    if test_for_set(sudoku_to_solve) == 1:
                        # printsudoku(sudoku_to_solve)
                        # print('Solved to solve')
                        # input()
                        return 'Solved'   # raise SystemExit()

                    else:
                        return 'Unsolvable2'    # raise SystemExit()
                n += 1
                '''
                while n in predefined:
                    n += 1
                '''
            else:
                sudoku_possible[n].remove(sudoku_to_solve[n])

        sudoku_possible[n] = [1, 2, 3, 4, 5, 6, 7, 8, 9]    # print(sudoku_possible)
        sudoku_to_solve[n] = 0
        n -= 1
        if n < 0:
            return 'Unsolvable3'
        while sudoku_to_solve[n] == [] or sudoku_possible[n] == [] or n in predefined:
            n -= 1
        if n < 0:
            return 'unsolvable4'    # raise SystemExit()

        sudoku_possible[n].remove(sudoku_to_solve[n])
        # print('n ', n, 'lehet ', sudoku_possible[n])


def dig(dig):
    hole = random.randint(0, 80)
    while dig[hole] == 0:
        hole = random.randint(0, 80)
    # print('hole: ', hole)
    return hole


def dig_holes(sudoku_to_dig):
    sudoku_to_dig[dig(sudoku_to_dig)] = 0   # first hole
    slots = 1
    solutions = 0
    while solutions < 2:
        slot = dig(sudoku_to_dig)   # print(slot)
        slots = sudoku_to_dig.count(0)
        sudoku_to_try = []
        for i in sudoku_to_dig:
            sudoku_to_try.append(i)
        # printsudoku(sudoku_to_try)
        print('to try')
        solutions = 0
        for i in range(1, 10):
            sudoku_to_try[slot] = i
            # printsudoku(sudoku_to_try)    # print('i ', i, sudoku_solver(sudoku_to_try))
            # print('to try')
            # input()
            print('to try ', i)
            if sudoku_solver(sudoku_to_try) == 'Solved':
                solutions += 1
                # printsudoku(sudoku_to_try)
                print('solved ', slots, slot, i, sudoku_to_dig[slot], sudoku_to_try[slot], solutions)
                sudoku_to_try = []
                for i in sudoku_to_dig:
                    sudoku_to_try.append(i)
                # printsudoku(sudoku_to_dig)
                # print('to dig ', slots)
                # input()
            # printsudoku(sudoku_to_try)
            # print(slots, solutions)
            # input()
        if solutions == 1:
            sudoku_to_dig[slot] = 0
            sudoku_generated = []
            for i in sudoku_to_dig:
                sudoku_generated.append(i)
            # printsudoku(sudoku_to_dig)
            # print('to dig')
            # input()
    printsudoku(sudoku_generated)
    print(slots)


# main()
sudoku = create_filled_sudoku()
dig_holes(sudoku)