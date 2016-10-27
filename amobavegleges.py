import sys
global field
import time
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


print("Welcome to Amőba!")
print("In this game your goal is to put 3 'X'' or 3 '0' in a row or a column or a diagonal.")
time.sleep(3)
field = []

def fieldappend():
    for x in range(0,3):
        field.append(['_'] * 3)

def fieldprint():
    for i in field:
        print(' '.join(i))
    print("")


def hit1():
    
    global field
    x = input("Enter in a row! (Choose one of the following number: 1, 2, 3): ")
    y = input("Enter in a column! (Choose one of the following number: 1, 2, 3): ")
    print("")
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("Give me a " + bcolors.WARNING + "NUMBER! " + bcolors.ENDC + " \n")
        hit1()
    if (x > 3 or x < 0 or y > 3 or y <0):
        print("Out of " + bcolors.FAIL + "range. " + bcolors.ENDC + " \n")
        hit1()
    x, y = x - 1, y - 1
    if (field[x][y] == 'X' or field[x][y] == 'O'):
        print("You can't mark " + bcolors.UNDERLINE + "that" + bcolors.ENDC + " spot. \n")
        hit1()
    else:
        field[x][y] = 'X'
        fieldprint()
        checkgame()
        time.sleep(2)
        print("Now O turn. \n")
        time.sleep(1)
        hit2()
        fieldprint()


def hit2():
    global field
    x = input("Enter in a row! (Choose one of the following number: 1, 2, 3): ")
    y = input("Enter in a column! (Choose one of the following number: 1, 2, 3): ")
    print("")
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("Give me a " + bcolors.WARNING + "NUMBER! " + bcolors.ENDC + " \n")
        hit2()
    if (x > 3 or x < 0 or y > 3 or y <0):
        print("Out of " + bcolors.FAIL + "range. " + bcolors.ENDC + " \n")
        hit2()
    x, y = x - 1, y - 1
    if (field[x][y] == 'X' or field[x][y] == 'O'):
        print("You can't mark " + bcolors.UNDERLINE + "that" + bcolors.ENDC + " spot. \n")
        hit2()
    else:
        field[x][y] = 'O'
        fieldprint()
        checkgame()
        time.sleep(2)        
        print("Now X turn. \n")
        time.sleep(1)
        hit1()
        fieldprint()
        

def checkgame():
    win = False
    if ((field[0][0] == 'X' and field[0][1] == 'X' and field[0][2] == 'X') or
        (field[1][0] == 'X' and field[1][1] == 'X' and field[1][2] == 'X') or
        (field[2][0] == 'X' and field[2][1] == 'X' and field[2][2] == 'X') or
        (field[0][0] == 'X' and field[1][1] == 'X' and field[2][2] == 'X') or
        (field[0][2] == 'X' and field[1][1] == 'X' and field[2][0] == 'X') or
        (field[0][0] == 'X' and field[1][0] == 'X' and field[2][0] == 'X') or
        (field[0][1] == 'X' and field[1][1] == 'X' and field[2][1] == 'X') or
        (field[0][2] == 'X' and field[1][2] == 'X' and field[2][2] == 'X') or
        (field[0][0] == 'X' and field[1][0] == 'X' and field[2][0] == 'X') or
        (field[0][1] == 'X' and field[1][1] == 'X' and field[2][1] == 'X') or
        (field[0][2] == 'X' and field[1][2] == 'X' and field[2][2] == 'X')):
        win = True
        print("The X wins!")
        sys.exit(0)
    elif(field[0][0] != '_' and field[0][2] !='_' and field[2][0] !='_' and field[2][2] !='_' and win == False):
        print("Tie.")
        sys.exit(0)
    elif ((field[0][0] == 'O' and field[0][1] == 'O' and field[0][2] == 'O') or
        (field[1][0] == 'O' and field[1][1] == 'O' and field[1][2] == 'O') or
        (field[2][0] == 'O' and field[2][1] == 'O' and field[2][2] == 'O') or
        (field[0][0] == 'O' and field[1][1] == 'O' and field[2][2] == 'O') or
        (field[0][2] == 'O' and field[1][1] == 'O' and field[2][0] == 'O') or
        (field[0][0] == 'O' and field[1][0] == 'O' and field[2][0] == 'O') or
        (field[0][1] == 'O' and field[1][1] == 'O' and field[2][1] == 'O') or
        (field[0][2] == 'O' and field[1][2] == 'O' and field[2][2] == 'O') or
        (field[0][0] == 'O' and field[1][0] == 'O' and field[2][0] == 'O') or
        (field[0][1] == 'O' and field[1][1] == 'O' and field[2][1] == 'O') or
        (field[0][2] == 'O' and field[1][2] == 'O' and field[2][2] == 'O')):
        win = True
        print("The 0 wins!")
        sys.exit(0)
          
        
       
        

if __name__ == '__main__':
    fieldappend()
    input("Okay, lets play! Press enter to continue.")
    fieldprint()
    hit1()
    