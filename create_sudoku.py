import random

clean_list=[]
for i in range(1,10):
    clean_list.append(i)

sudoku = []

for i in range(1,83):
   sudoku.append(0)
# print(sudoku)

sudoku_not = []

for i in range(1,83):
   sudoku_not.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(sudoku_not)

def test(list): # checks if the given 9 member list (row, column or block) is valid
    # print(list, n)
    # input()
    if list.count(sudoku[n]) > 1:
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
    print('row result ', result)
    
    testlist = []
    # test columns
    if result == 1:
        for i in range(9):
            testlist= []
            for j in range(9):
                testlist.append(sudoku[i+j*9])
            if test(testlist) == 0:
                result = 0
                print(result)
                break
    print('column result', result)
    
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
                            print(result)
                            break
                        testlist = []
                
        print('cube result ', result)
        
    return result

def printsudoku():
    print("   \033[1;32mA B C   D E F   G H I\033[;m") # columns
    for i in range(3):
        for row in range(0, 3):
                print("\033[1;32m"+str((i*3)+(row+1))+"\033[;m", ' ', end='') # rows
                print(sudoku[i*27+row*9], end='') 
                print(' ', end='')
                print(sudoku[i*27+row*9+1], end='')
                print(' ', end='')
                print(sudoku[i*27+row*9+2], end='')
                print(' ', end='  ')
                print(sudoku[i*27+row*9+3], end='')
                print(' ', end='')
                print(sudoku[i*27+row*9+4], end='')
                print(' ', end='')
                print(sudoku[i*27+row*9+5], end='')
                print(' ', end='  ')
                print(sudoku[i*27+row*9+6], end='')
                print(' ', end='')
                print(sudoku[i*27+row*9+7], end='')
                print(' ', end='')
                print(sudoku[i*27+row*9+8], end='')
                print()
        print()


n = 0
while n <= 80:
    while sudoku_not[n] != []:
        printsudoku()
        print('n ', n, 'lehet ', sudoku_not[n])
        sudoku[n] = sudoku_not[n][random.randint(0,len(sudoku_not[n])-1)] 
        print('n ', n, sudoku[n])
        # input()
        if check() == 1:
            n += 1
            print(n)
            if n > 81:
                printsudoku()
                quit()            
            # input()
        else:
            sudoku_not[n].remove(sudoku[n])
            printsudoku()
            print(n, sudoku_not[n])
            # input()
            sudoku[n] = 0
    sudoku_not[n] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sudoku_not)
    sudoku[n] = 0
    n -= 1
    sudoku_not[n].remove(sudoku[n])
    print('n ', n, 'lehet ', sudoku_not[n])
printsudoku()

