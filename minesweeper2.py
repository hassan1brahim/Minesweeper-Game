import random
import pyinputplus as pyip 

class MineSweeper:

    def __init__(self, row, col): #Constructor
        #ah so self is a property of an instance of a class got it
        #btw an instance of a class is an object
        self.row = row
        self.col = col
        self.frontEnd = [['.'] * col for _ in range(row)]
        self.backEnd = [[' '] * col for _ in range(row)]
        #The underscore (_) just means “I don’t care about the number, just loop it.”
        #['*'] for _ in range(100) basically creates 100 ['*'] and since its ['*']*100, 
        #a 2d array of size[100][100] is made

    def isValidRow(self, row): #Checks if the row number entered is valid
        if row >= 0 and row < self.row:
            return True 
        return False
    
    def isValidCol(self, col): #Checks if the col number entered is valid
    
        if col >= 0 and col < self.col:
            return True 
        return False

    def isValidAssign(self, row, col): #Assigns the count to each element
        
        if self.backEnd[row][col] == '*':
            return '*'
        
        count = 0
        
        # Checks all around the block, how many bombs is the block connected to
        if self.isValidRow(row - 1):
            if self.isValidCol(col - 1):
                if self.backEnd[row - 1][col - 1] == '*':
                    count += 1
            if self.isValidCol(col):
                if self.backEnd[row - 1][col] == '*':
                    count += 1
            if self.isValidCol(col + 1):
                if self.backEnd[row - 1][col + 1] == '*':
                    count += 1
        
        if self.isValidRow(row + 1):
            if self.isValidCol(col - 1):
                if self.backEnd[row + 1][col - 1] == '*':
                    count += 1
            if self.isValidCol(col):
                if self.backEnd[row + 1][col] == '*':
                    count += 1
            if self.isValidCol(col + 1):
                if self.backEnd[row + 1][col + 1] == '*':
                    count += 1
        
        if self.isValidCol(col - 1):
            if self.backEnd[row][col - 1] == '*':
                    count += 1

        if self.isValidCol(col + 1):
            if self.backEnd[row][col + 1] == '*':
                    count += 1
        
        c = str(count)

        return c

    def printList(self): #Prints the frontEnd array
        
        print('  ', end = ' ')
        for i in range(len(self.frontEnd[0])): #Formatting
            if i < 10:
                print(i, end = '  ')
            else:
                print(i, end = ' ')
        
        print()
        i = 0
        for row in self.frontEnd:  #So here a row is an element of a 2d list, meaning it itself is a 1d list
            print(i, end = ' ')
            if i < 10:
                print(end = ' ')
            for col in row:  #Each col is an element of that 1d array
                print(col, end='  ') #end = ' ' insures that it doesnt go to the next line

            i += 1
            print()
    
    def generateBombs(self, mines):
        '''
        An approach that did not work, because this does not deal with the repetitions
        for i in range(0, mines): #Assigning a specific amount of mines 
            x = random.randint(0, self.row - 1) #A random number from 0 to self.row - 1
            y = random.randint(0, self.col - 1) #A random number from 0 to self.col - 1
            self.backEnd[x][y] = '*' # A mine is represented by the symbol B
        '''

        mySet = set() #Declares a new set

        while len(mySet) < mines: #Set can only have 
            x = random.randint(0, self.row - 1) #A random number from 0 to self.row - 1
            y = random.randint(0, self.col - 1) #A random number from 0 to self.col - 1
            mySet.add((x,y))
        
        for num in mySet:
            self.backEnd[num[0]][num[1]] = '*' # A mine is represented by the symbol *

        

    def assignNumbers(self): #Assigns each block a number depending on how many mines it touches
        for i in range(0, self.row):
            for j in range(0, self.col):
                self.backEnd[i][j] = self.isValidAssign(i, j)
    
    def recursive(self, row, col): #Recursively opens up all the spaces connected to each other
        #Base Case
        if not (self.isValidRow(row) and self.isValidCol(col) ) or self.backEnd[row][col] != '0':
            return
        
        self.frontEnd[row][col] = self.backEnd[row][col] = ' ' #A space is opened

        #Recursively opens more spaces
        self.recursive(row + 1, col)
        self.recursive(row + 1, col - 1)
        self.recursive(row + 1, col + 1)
        self.recursive(row - 1, col)
        self.recursive(row - 1, col - 1)
        self.recursive(row - 1, col + 1)
        self.recursive(row, col - 1)
        self.recursive(row, col + 1)
    
    def giveInput(self, row, col, character = ' '): #The only way we can change the array from outside the class
        
        while True:
            #Takes an input between 0 and row/col - 1. Accepts no otger input
            input_Row = int(pyip.inputNum('Enter the row: ', min = 0, lessThan = row))
            input_Col = int(pyip.inputNum('Enter the col: ', min = 0, lessThan = col))

            choice = self.backEnd[input_Row][input_Col]
            #Checks if a flag is entered
            if character == 'F':
                choice = self.frontEnd[input_Row][input_Col]
                if choice == '.':
                    self.frontEnd[input_Row][input_Col] = self.backEnd[input_Row][input_Col] = 'F'
                elif choice == 'F':
                    print('The block is already flagged! Try again!')
                else:
                    print('The block is opened! Try again')
                    continue
                return '0'
            
            #Checks and deals with all the conditions unless its a bomb
            if choice == '*':
                return '*'
            
            if choice == '0':
                self.recursive(input_Row, input_Col)
                break 

            if not (choice == 'F' or choice == ' '):
                self.frontEnd[input_Row][input_Col] = choice
                break

            
            if choice == 'F':
                print('The block is already flagged! Try again!')
                continue

            if choice == ' ':
                print('The block is already open! Try again!')
                continue
        
        return '0'
    
    #After each loop, check how many bobms are left and end the prgram whe their no bombs
    def checkBombNum(self):
        count = 0
        for row in self.backEnd:
            for col in row:
                if col == '*':
                    count += 1
        
        return count
        





def main():
    while True:

        print('Welcome to MineSweeper!')
        level = pyip.inputNum('Enter the level you wish to play at! 0 for Beginner, 1 for Intermediate and 2 for expert!: ', min = 0, lessThan = 3)

        #Determine the level and the grid size after taking input
        if level == 0:
            row, col, bombs = 9, 9, 10
        elif level == 1:
            row, col, bombs = 16, 16, 40
        elif level == 2:
            row, col, bombs = 30, 16, 99

        Ms = MineSweeper(row, col)
        Ms.generateBombs(bombs)
        Ms.assignNumbers()


        while True:
            Ms.printList()
            #Since case sesitive is false, it turns 'y' into Y
            choice = pyip.inputChoice(['Y', 'N'], prompt = 'Do you wish to flag? ', caseSensitive = False)

            if choice == 'Y':
                Ms.giveInput(row, col, 'F')
                continue 

            print('Enter the coordinates you wish to open!')
            choice = Ms.giveInput(row, col)

            #Bomb detected, end the program
            if choice == '*':

                Ms.printList()
                print('You clicked a bomb! Too bad you lost!')
                print('You opened ' + str(bombs - Ms.checkBombNum()) + ' bombs')
                break 

            #No bombs left, end the program
            if Ms.checkBombNum() == 0:
                print('You won! Congratulations!')
                break
        
        choice = pyip.inputChoice(['Y', 'N'], prompt = 'Do you want to play again? ', caseSensitive = False)
        
        if choice == 'N':
            print('Ending program......')
            break
    
main()