import os
import csv
import random

# init - defining the puzzle to solve
sudoku_predetermined = [
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

solved_predetermined = [
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




def color_print(cp): # prints the predefined numbers in red, the others in black
    a="\033[1;31m" # prints in bold and red color
    b="\033[;m" # end of printing in red color
    c="\033[1m" # prints in bold 
    d="\033[0;0m" # end of print in bold
    '''
    predefined = [] # creates a list thet has the index of the predefined numbers
    for i in range(len(sudoku)):
        if sudoku[i] != 0:
            predefined.append(i)
    # print(predefined)
    '''
    if cp in predefined:
        print(a+str(sudoku[cp])+b, end='')
    elif sudoku[cp] == 0:
        print('-', end='')
    elif sudoku.count(sudoku[cp]) == 9:
        print(c+str(sudoku[cp])+d, end='')
    else:
        print(sudoku[cp], end='')



# printing
def print_sudoku():
    os.system('clear')
    print("   \033[1;32mA B C   D E F   G H I\033[;m") # columns
    for i in range(3):
        for row in range(0, 3):
                print("\033[1;32m"+str((i*3)+(row+1))+"\033[;m", ' ', end='') # rows
                color_print(i*27+row*9) 
                print(' ', end='')
                color_print(i*27+row*9+1)
                print(' ', end='')
                color_print(i*27+row*9+2)
                print(' ', end='  ')
                color_print(i*27+row*9+3)
                print(' ', end='')
                color_print(i*27+row*9+4)
                print(' ', end='')
                color_print(i*27+row*9+5)
                print(' ', end='  ')
                color_print(i*27+row*9+6)
                print(' ', end='')
                color_print(i*27+row*9+7)
                print(' ', end='')
                color_print(i*27+row*9+8)
                print()
        print()

def instructions():
    print('''
    column row number - e.g. 'A 1 1' or 'a 1 1’     return to menu press: m or M
    to delete - e.g. 'a 1 0' or 'a 1 -'             to save and exit press: s or S
    for help - e.g. 'a 1 h'                         return to menu and save press: ms or MS

                                     to quit press: x
    ''')
    get_input()

def get_input(): # process the user input
    '''
    predefined = []  # creates a list thet has the index of the predefined numbers
    for i in range(len(sudoku)):
        if sudoku[i] != 0:
            predefined.append(i)
    '''
    try:
        sudoku_input = input("Next number (For instruction type ins): ").split()
        slot = 0 # the place of the number
        if sudoku_input[0] != 'a' and sudoku_input[0] != 'A' and sudoku_input[0] != 'b' and sudoku_input[0] != 'B' and sudoku_input[0] != 'c' and sudoku_input[0] != 'C' and sudoku_input[0] != 'd' and sudoku_input[0] != 'D' and sudoku_input[0] != 'e' and sudoku_input[0] != 'E' and sudoku_input[0] != 'f' and sudoku_input[0] != 'F' and sudoku_input[0] != 'g' and sudoku_input[0] != 'G' and sudoku_input[0] != 'h' and sudoku_input[0] != 'H' and sudoku_input[0] != 'i' and sudoku_input[0] != 'I' and sudoku_input[0] != 'x' and sudoku_input[0] != 'X' and sudoku_input[0] != 's' and sudoku_input[0] != 'S' and sudoku_input[0] != 'm' and sudoku_input[0] != 'M' and sudoku_input[0] != 'ms' and sudoku_input[0] != 'MS' and sudoku_input[0] != 'mS' and sudoku_input[0] != 'Ms' and sudoku_input[0] != 'ins' and sudoku_input[0] != 'INS':
            print_sudoku()
            print('Wrong column, try again!')
            return
        elif sudoku_input[0] == 'a' or sudoku_input[0] == 'A':
            slot = 1
        elif sudoku_input[0] == 'b' or sudoku_input[0] == 'B':
            slot = 2
        elif sudoku_input[0] == 'c' or sudoku_input[0] == 'C':
            slot = 3
        elif sudoku_input[0] == 'd' or sudoku_input[0] == 'D':
            slot = 4
        elif sudoku_input[0] == 'e' or sudoku_input[0] == 'E':
            slot = 5
        elif sudoku_input[0] == 'f' or sudoku_input[0] == 'F':
            slot = 6
        elif sudoku_input[0] == 'g' or sudoku_input[0] == 'G':
            slot = 7
        elif sudoku_input[0] == 'h' or sudoku_input[0] == 'H':
            slot = 8         
        elif sudoku_input[0] == 'i' or sudoku_input[0] == 'I':
            slot = 9         
        elif sudoku_input[0] == 'x' or sudoku_input[0] == 'X': # exit game
            quit()
        elif sudoku_input[0] == 's' or sudoku_input[0] == 'S': # to save game
            save_sudoku()
            print('Good bye, see you next time!')
            quit()
        elif sudoku_input[0] == 'm' or sudoku_input[0] == 'M': # return to main menu
            main()
        elif sudoku_input[0] == 'ms' or sudoku_input[0] == 'MS' or sudoku_input[0] == 'mS' or sudoku_input[0] == 'Ms': # return to main menu and save
            save_sudoku()
            main()
        elif sudoku_input[0] == 'ins' or sudoku_input[0] == 'INS':
            instructions()
            return

        if int(sudoku_input[1]) not in range(1,10): 
            print_sudoku()
            print('Wrong row, try again!')
            return
        else:
            slot += (int(sudoku_input[1])-1)*9-1
            if slot in predefined:
                print_sudoku()
                print('Predefined number, try again!')
                return
            elif sudoku[slot] != 0:
                if sudoku_input[2] == '0' or sudoku_input[2] == '-':
                    sudoku[slot] = 0
                    print_sudoku()
                    return
                else:    
                    print_sudoku()
                    print('Occupied place, try again!')
                    return
            elif sudoku_input[2] == 'h' or sudoku_input[2] == 'H': # help
                    sudoku[slot] = solved[slot]
                    print_sudoku()
                    return
            elif int(sudoku_input[2]) not in range(1, 10): 
                    print_sudoku()
                    print('Wrong number, try again!')
                    return
            else:
                sudoku[slot] = int(sudoku_input[2])
                print_sudoku()
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        #raise
        print_sudoku()
        print('Wrong input, try again')


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
    
    global solved
    solved = sudoku_filled[:]
    


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
    
    predefined_numbers = []  # creates a list thet has the index of the predefined numbers
    for i in range(len(sudoku_to_solve)):
        if sudoku_to_solve[i] != 0:
            predefined_numbers.append(i)
    
    sudoku_possible = []
    for i in range(0, 81):
        if i not in predefined_numbers:
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
            while n in predefined_numbers:
                n += 1
                # print('n ', n, 'lehet ', sudoku_possible[n])
            if n > 80:
                if test_for_set(sudoku_to_solve) == 1:
                    # printsudoku(sudoku_to_solve)
                    # print('Solved to solve')
                    # input()
                    global solved
                    solved = sudoku_to_solve[:]
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
        while sudoku_to_solve[n] == [] or sudoku_possible[n] == [] or n in predefined_numbers:
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
    return slots

 
def test(list): # checks if the given 9 member list (row, column or block) is valid
    # print(list)
    # input()
    all_numbers_once = [] # a list that has the numbers of 1 to 9
    for i in range(1,10):
        all_numbers_once.append(i)
    list.sort()
    if set(all_numbers_once) != set(list):
        return 0

def check_filled(): # testing the filled sudoku
    testlist = []
    result = 1
    
    # test rows
    for i in range(9):
        testlist= []
        for j in range(9):
            testlist.append(sudoku[j+i*9])
        if test(testlist) == 0:
            result = 0
            break
    # print('row result ', result)
    
    testlist = []
    # test columns
    if result == 1:
        for i in range(9):
            testlist= []
            for j in range(9):
                testlist.append(sudoku[i+j*9])
            if test(testlist) == 0:
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
                        testlist.append(sudoku[i+j])
                        testlist.append(sudoku[i+j+1])
                        testlist.append(sudoku[i+j+2])
                        testlist.append(sudoku[i+j+9])
                        testlist.append(sudoku[i+j+10])
                        testlist.append(sudoku[i+j+11])
                        testlist.append(sudoku[i+j+18])
                        testlist.append(sudoku[i+j+19])
                        testlist.append(sudoku[i+j+20])
                        if test(testlist) == 0:
                            result = 0
                            # print(result)
                            break
                        testlist = []
                
        # print('cube result ', result)
        
    return result


def save_sudoku(filename="sudoku.csv"):
    with open(filename, 'w', newline='') as csvfile:
        sudoku_writer = csv.writer(csvfile)
        sudoku_writer.writerow(sudoku)
        sudoku_writer.writerow(solved)
        sudoku_writer.writerow(predefined)


def load_sudoku(filename="sudoku.csv"):
    try:
      with open(filename, newline='') as csvfile:
        sudoku_reader = csv.reader(csvfile)
        load_sudoku = []
        for row in sudoku_reader:
            for i in row:
                load_sudoku.append(int(i))
      return load_sudoku
    except FileNotFoundError:
      print("You have no previous saved file")
      menu()



def title():
    print('''
                                                                                                               
                                                 dddddddd                                                      
   SSSSSSSSSSSSSSS                               d::::::d                 kkkkkkkk                             
 SS:::::::::::::::S                              d::::::d                 k::::::k                             
S:::::SSSSSS::::::S                              d::::::d                 k::::::k                             
S:::::S     SSSSSSS                              d:::::d                  k::::::k                             
S:::::S            uuuuuu    uuuuuu      ddddddddd:::::d    ooooooooooo    k:::::k    kkkkkkkuuuuuu    uuuuuu  
S:::::S            u::::u    u::::u    dd::::::::::::::d  oo:::::::::::oo  k:::::k   k:::::k u::::u    u::::u  
 S::::SSSS         u::::u    u::::u   d::::::::::::::::d o:::::::::::::::o k:::::k  k:::::k  u::::u    u::::u  
  SS::::::SSSSS    u::::u    u::::u  d:::::::ddddd:::::d o:::::ooooo:::::o k:::::k k:::::k   u::::u    u::::u  
    SSS::::::::SS  u::::u    u::::u  d::::::d    d:::::d o::::o     o::::o k::::::k:::::k    u::::u    u::::u  
       SSSSSS::::S u::::u    u::::u  d:::::d     d:::::d o::::o     o::::o k:::::::::::k     u::::u    u::::u  
            S:::::Su::::u    u::::u  d:::::d     d:::::d o::::o     o::::o k:::::::::::k     u::::u    u::::u  
            S:::::Su:::::uuuu:::::u  d:::::d     d:::::d o::::o     o::::o k::::::k:::::k    u:::::uuuu:::::u  
SSSSSSS     S:::::Su:::::::::::::::uud::::::ddddd::::::ddo:::::ooooo:::::ok::::::k k:::::k   u:::::::::::::::uu
S::::::SSSSSS:::::S u:::::::::::::::u d:::::::::::::::::do:::::::::::::::ok::::::k  k:::::k   u:::::::::::::::u
S:::::::::::::::SS   uu::::::::uu:::u  d:::::::::ddd::::d oo:::::::::::oo k::::::k   k:::::k   uu::::::::uu:::u
 SSSSSSSSSSSSSSS       uuuuuuuu  uuuu   ddddddddd   ddddd   ooooooooooo   kkkkkkkk    kkkkkkk    uuuuuuuu  uuuu
                                                                                                               
                  Welcome to the most awesome sudoku game ever, choose one from the menus below                                                                                        
    ''')

def menu():
  print('{:^112}'.format("1 - Load saved game"))
  print('{:^112}'.format("2 - Use predetermined table (for the weak)"))
  print('{:^112}'.format("3 - Random generate sudoku"))
  print('{:^112}'.format("4 - eXit - But mom, bedtime already?.. :("))
  print('{:^112}'.format("5 - Random generate sudoku with difficulty levels"))
  choose = 1
  while choose > 0 and choose < 5:
    try:
        choose = int(input())
    except:
        print("Wrong Input")
        menu()
    if choose == 1:
        loaded = load_sudoku()
        global sudoku
        sudoku = []
        global solved
        solved = []
        global predefined
        predefined = []
        for i in range(81):
            sudoku.append(int(loaded[i]))
        for i in range(81, 162):
            solved.append(int(loaded[i]))
        for i in range(162, len(loaded)):
            predefined.append(int(loaded[i]))
        return

    elif choose == 2:
        global sudoku
        sudoku = sudoku_predetermined[:]
        
        global solved
        solved = solved_predetermined[:]
        
        global predefined
        predefined = [] # creates a list thet has the index of the predefined numbers
        for i in range(len(sudoku)):
            if sudoku[i] != 0:
                predefined.append(i)

        return
    elif choose == 3:
        global sudoku
        sudoku = create_filled_sudoku()
        dig_holes(sudoku)
        global predefined
        predefined = [] # creates a list thet has the index of the predefined numbers
        for i in range(len(sudoku)):
            if sudoku[i] != 0:
                predefined.append(i)
        return
    elif choose == 4:
        quit()
    elif choose == 5:
        submenu()
        return


def submenu():
    print('{:^112}'.format("1 - Easy"))
    print('{:^112}'.format("2 - Medium"))
    print('{:^112}'.format("3 - Hard"))
    print('{:^112}'.format("4 - NIGHTMARE"))
    choose = 0
    while choose not in range(1, 4):
        try:
            choose = int(input())
        except:
            print("Wrong Input")
            menu()
        if choose == 1:
            global sudoku
            sudoku = create_filled_sudoku()
            number_of_holes = 0
            while number_of_holes not in range(32, 42):
                number_of_holes = dig_holes(sudoku)
            global predefined
            predefined = [] # creates a list thet has the index of the predefined numbers
            for i in range(len(sudoku)):
                if sudoku[i] != 0:
                    predefined.append(i)
            return

        if choose == 2:
            global sudoku
            sudoku = create_filled_sudoku()
            number_of_holes = 0
            while number_of_holes not in range(42, 56):
                number_of_holes = dig_holes(sudoku)
            global predefined
            predefined = [] # creates a list thet has the index of the predefined numbers
            for i in range(len(sudoku)):
                if sudoku[i] != 0:
                    predefined.append(i)
            return

        if choose == 3:
            global sudoku
            sudoku = create_filled_sudoku()
            number_of_holes = 0
            while number_of_holes not in range(56, 59):
                number_of_holes = dig_holes(sudoku)
            global predefined
            predefined = [] # creates a list thet has the index of the predefined numbers
            for i in range(len(sudoku)):
                if sudoku[i] != 0:
                    predefined.append(i)
            return
        if choose == 4:
            global sudoku
            sudoku = create_filled_sudoku()
            number_of_holes = 0
            while number_of_holes not in range(60, 64):
                number_of_holes = dig_holes(sudoku)
            global predefined
            predefined = [] # creates a list thet has the index of the predefined numbers
            for i in range(len(sudoku)):
                if sudoku[i] != 0:
                    predefined.append(i)
            return

# main
def main():
    os.system('clear')
    title()
    menu()
    '''
    global predefined
    predefined = [] # creates a list thet has the index of the predefined numbers
    for i in range(len(sudoku)):
        if sudoku[i] != 0:
            predefined.append(i)
    # print(predefined)
    '''
    # sudoku_solver(sudoku)

    print_sudoku()
    while 0 in sudoku:
        get_input()
    check_filled()
    if check_filled() == 0:
        print('Wrong solution, try again!')
    else:
        print('Congratulations, you solved the sudoku!')

main()