import tkinter as tk
import random
from cell import Cell

global TEST
TEST = True

class minesweeper():
    
    def __init__(self):

        """ Variable initialization """

        # rows: an integer that holds the total number of rows in the game
        self.rows = 9

        # cols: an integer that holds the total number of columns in the game
        self.cols = 9

        """ List initialization """

        # cellArray: a 2-dimensional array that contains each cell in the game
        self.cellArray = []

        # buttonArray: a 2-dimensional array that contains each button in the window
        self.buttonArray = []

        """ List construction """

        # For each row in the game...
        for row in range(self.rows):

            # ... Create a list of cells for that row
            cellRow = []

            # ... Create a list of buttons for that row
            buttonRow = []

            # ... and for each column in the game...
            for column in range(self.cols):

                # ... Create a new cell
                newCell = Cell(row, column)

                # Put that cell into the rowList
                cellRow.append(newCell)

                # ... Create a new space for a button
                buttonRow.append(None)

            # Then place the filled cellRow into the cellArray
            self.cellArray.append(cellRow)

            # Then place the filled buttonRow into the buttonArray
            self.buttonArray.append(buttonRow)

        """ Testing """
        
        # If you are testing...
        if TEST:

            # For each row in the cellArray...
            for row in self.cellArray:

                # ... for each column in the row...
                for column in row:

                    # ... print out the coordinates of that cell
                    print(column.row, column.column, sep=",", end="")
                    print(" ", end="")
                    
                print()

            # For each row in the buttonArray...
            for row in self.buttonArray:

                # ... for each column in the row...
                for column in row:

                    # ... print out the contents of the button array (None)
                    print(column, sep = ", ", end = "")
                    print(" ", end = "")

                print()
                                
    def main(self):

        self.buildWindow()

    def buildWindow(self):

        """ Window construction """

        # window: a Tkinter window that will serve as the game screen
        window = tk.Tk()

        # Prevent window from being resized
        window.resizable(False, False)

        """ Frame construction """

        # statusFrame: a Tkinter frame that contains the Reset button
        statusFrame = tk.Frame(
            master = window,
            relief = tk.FLAT
        )

        # Place the statusFrame onto 0,0 and set it's width to the number of columns
        statusFrame.grid(row = 0, column = 0, columnspan = self.cols)

        """ Reset button construction """

        # resetButton: a Tkinter button that will reset the game when pressed
        resetButton = tk.Button(master = statusFrame, text = "Restart", command = self.reset # COMMAND GOES HERE
                                )

        # Place the button in the center of statusFrame
        resetButton.grid(row = 0, column = 0, pady = 10)

        """ Divider Label construction """

        # divLabel: a Tkinter label that serves to divide the resetButton from the game grid
        divLabel = tk.Label(master = statusFrame)
        divLabel.grid(row = 1, column = 0)

        """ Button construction """

        # For each row in the grid...
        for buttonRow in range(self.rows):

            # ... for each column in the grid...
            for buttonCol in range(self.cols):

                # ... build a button...
                self.buttonArray[buttonCol][buttonRow] = tk.Button(
                    window,
                    width = 2,
                    height = 1,
                    relief = tk.RAISED
                    # COMMAND GOES HERE
                )

                # ... and put that button into the buttonArray
                self.buttonArray[buttonCol][buttonRow].grid(row = buttonRow + 1, column = buttonCol)

    def dig(self, row, column):
        7

    def reset(self):
        7

    def prime(self):
        7

app = minesweeper()
app.main()
