import os

# init - defining the puzzle to solve
sudoku = [
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

solved = [
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

predefined = [] # creates a list thet has the index of the predefined numbers
for i in range(len(sudoku)):
    if sudoku[i] != 0:
        predefined.append(i)
# print(predefined)

a="\033[1;31m" # prints in baéd and red color
b="\033[;m" # end of printing in red color
def color_print(cp): # prints the predefined numbers in red, the others in black
    if cp in predefined:
        print(a+str(sudoku[cp])+b, end='')
    elif sudoku[cp] == 0:
        print('-', end='')
    else:
        print(sudoku[cp], end='')

all_numbers_once = [] # a list that has the numbers of 1 to 9
for i in range(1,10):
    all_numbers_once.append(i)

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

def get_input(): # process the user input
    try:
        sudoku_input = input("Next number (column row number - e.g. 'A 1 1' or 'a 1 1', to delete 'a 1 0' or 'a 1 -', for help 'a 1 h', to  quit 'x', to save press s or S: ").split()
        slot = 0 # the place of the number
        if sudoku_input[0] != 'a' and sudoku_input[0] != 'A' and sudoku_input[0] != 'b' and sudoku_input[0] != 'B' and sudoku_input[0] != 'c' and sudoku_input[0] != 'C' and sudoku_input[0] != 'd' and sudoku_input[0] != 'D' and sudoku_input[0] != 'e' and sudoku_input[0] != 'E' and sudoku_input[0] != 'f' and sudoku_input[0] != 'F' and sudoku_input[0] != 'g' and sudoku_input[0] != 'G' and sudoku_input[0] != 'h' and sudoku_input[0] != 'H' and sudoku_input[0] != 'i' and sudoku_input[0] != 'I' and sudoku_input[0] != 'x' and sudoku_input[0] != 'X' and sudoku_input[0] != 's' and sudoku_input[0] != 'S':
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
            save()

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
        print_sudoku()
        print('Wrong input, try again')

def test(list): # checks if the given 9 member list (row, column or block) is valid
    # print(list)
    # input()
    list.sort()
    if set(all_numbers_once) != set(list):
        return 0

def check(): # testing the filled sudoku
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

def title():
    print('''
        _        _                  _            _            _         _               
       / /\     /\_\               /\ \         /\ \         /\_\      /\_\             
      / /  \   / / /         _    /  \ \____   /  \ \       / / /  _  / / /         _   
     / / /\ \__\ \ \__      /\_\ / /\ \_____\ / /\ \ \     / / /  /\_\\ \ \__      /\_\ 
    / / /\ \___\\ \___\    / / // / /\/___  // / /\ \ \   / / /__/ / / \ \___\    / / / 
    \ \ \ \/___/ \__  /   / / // / /   / / // / /  \ \_\ / /\_____/ /   \__  /   / / /  
     \ \ \       / / /   / / // / /   / / // / /   / / // /\_______/    / / /   / / /   
 _    \ \ \     / / /   / / // / /   / / // / /   / / // / /\ \ \      / / /   / / /    
/_/\__/ / /    / / /___/ / / \ \ \__/ / // / /___/ / // / /  \ \ \    / / /___/ / /     
\ \/___/ /    / / /____\/ /   \ \___\/ // / /____\/ // / /    \ \ \  / / /____\/ /      
 \_____\/     \/_________/     \/_____/ \/_________/ \/_/      \_\_\ \/_________/       
    ''')


# main
def main():
    os.system('clear')
    title()
    print_sudoku()
    while 0 in sudoku:
        get_input()
    check()
    if check() == 0:
        print('Wrong solution, try again!')
    else:
        print('Congratulations, you solved the sudoku!')

main()