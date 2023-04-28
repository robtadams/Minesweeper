import tkinter as tk
import random

global TEST
TEST = True

class minesweeper():
    def __init__(self):

        # How many rows and columns are there in the game?
        self.rows = 9
        self.cols = 9

        # A 2-dimensional array, where each cell contains the number of bombs adjacent to the cell
        self.cellArray = [ [0]*self.cols for _ in range(self.rows)]

        # A 2-dimensional array, where each cell contains the button for the game
        self.buttons = [[None]*self.cols for _ in range(self.rows)]

        # A boolean, which keeps track if the bombs have been primed or not
        self.bombsPrimed = False

        # A 1-dimensional array, where each cell is the coordinate of a valid bomb location
        self.safe = []
        for y in range(self.cols):
            for x in range(self.rows):
                self.safe.append([y, x])

        # Print out the values in the cellArray
        if TEST:
            for i in range(self.cols):
                print(self.cellArray[i])
                
    def main(self):
        
        self.buildWindow()

        running = True

        #self.prime()

    def buildWindow(self):

        # Create the Tkinter window
        window = tk.Tk()

        window.resizable(False, False)

        # Build the status Frame
        statusFrame = tk.Frame(
            master = window,
            relief = tk.FLAT
        )

        statusFrame.grid(row = 0, column = 0, columnspan = 10)
        
        newGameButton = tk.Button(master = statusFrame, text = "Restart", command = self.reset)
        newGameButton.grid(row = 0, column = 0, pady = 10)

        divLabel = tk.Label(master = statusFrame)
        divLabel.grid(row = 1, column = 0)

        for y in range(self.rows):
            for x in range(self.cols):
                self.buttons[x][y] = tk.Button(
                    window,
                    width = 2,
                    height = 1,
                    relief = tk.RAISED,
                    command = lambda row = x, col = y: self.dig(row, col)
                )
                self.buttons[x][y].grid(row = x + 1, column = y)

    def dig(self, row, column):

        if not self.bombsPrimed:
            self.safe.pop((row + 1) * column)
            self.prime()

        if TEST:
            print(row, column)
        self.buttons[row][column].config(relief = tk.SUNKEN)

    def reset(self):

        # Reset the array containing the valid bomb cells
        self.safe = []
        for y in range(self.cols):
            for x in range(self.rows):
                self.safe.append([y, x])

        # Reset the display for each button
        for row in self.buttons:
            for button in row:
                button.config(relief = tk.RAISED, bg = 'SystemButtonFace', text = "")
                self.cellArray = [ [0]*self.cols for _ in range(self.rows)]


        self.bombsPrimed = False

    def prime(self):

        # Prime the bombs
        self.bombsPrimed = True

        # Generate 10 bombs
        #self.primed = []
        for i in range(10):

            # Get a random cell within the array
            randCel = random.randint(0, len(self.safe) - 1)

            # Remove that cell from the safe array, and get it's coordinates
            bombCoords = self.safe.pop(randCel)

            #self.primed.append(self.buttons[bombCoords[0]][bombCoords[1]])
            
            if TEST:
                self.buttons[bombCoords[0]][bombCoords[1]].config(bg = "red")

            # Set that cell to -1, indicating that it is a bomb
            self.cellArray[bombCoords[0]][bombCoords[1]] = -1
            self.buttons[bombCoords[0]][bombCoords[1]].config(text = -1)

            # Check each adjacent cell
            for y in [-1, 0, 1]:
                for x in [-1, 0, 1]:

                    # Get an adjacent cell
                    tempX = bombCoords[0] + x
                    tempY = bombCoords[1] + y

                    # Check if that cell is in bounds...
                    if tempX >= 0 and tempX <= 8:
                        if tempY >= 0 and tempY <= 8:

                            # Do math to that cell
                            if self.cellArray[tempX][tempY] >= 0:
                                self.cellArray[tempX][tempY] += 1
                                self.buttons[tempX][tempY].config(text = self.cellArray[tempX][tempY])
            if TEST:
                print()
                for i in range(self.cols):
                    print(self.cellArray[i])
                        
            
    
app = minesweeper()
app.main()
