import tkinter as tk
import random
from cell import Cell

global TEST
TEST = False

class minesweeper():
    
    def __init__(self):

        """ Variable initialization """

        # rows: an integer that holds the total number of rows in the game
        self.rows = 9

        # cols: an integer that holds the total number of columns in the game
        self.cols = 9

        # numBombs: an integer that holds the number of bombs in the game
        self.numBombs = 10

        # bomsPrimed: a boolean that holds if the bombs in the game have been created or not
        self.bombsPrimed = False

        # numSafeCells: an integer that is equal to the total number of cells in the game,
        #               minus the number of bombs. This will be used to keep track 
        self.numSafeCells = (self.rows * self.cols) - self.numBombs

        """ Testing """

        # If testing...
        if TEST:

            # ... print the number of rows, columns, and bombs in the game
            print("\n--- INITIALIZATION TESTING ---\n")

            print("Number of rows: {0}".format(self.rows),
                  "Number of columns: {0}".format(self.cols),
                  "Number of bombs: {0}".format(self.numBombs),
                  sep = "\n")

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

            print("\n--- CELL ARRAY TESTING ---\n")

            # For each row in the cellArray...
            for row in self.cellArray:

                # ... for each column in the row...
                for column in row:

                    # ... print out the coordinates of that cell
                    print(column.row, column.column, sep=",", end="")
                    print(" ", end="")
                    
                print()

            print("\n--- BUTTON ARRAY TESTING ---\n")

            # For each row in the buttonArray...
            for row in self.buttonArray:

                # ... for each column in the row...
                for column in row:

                    # ... print out the contents of the button array (None)
                    print(column, sep = ", ", end = "")
                    print(" ", end = "")

                print()
                                
    def main(self):
        
        # window: a variable that holds the Tkinter window
        window = tk.Tk()

        # Build the game window
        self.buildWindow(window)

        window.bind("<Escape>", quit)

        # Enter into the main loop of the game
        window.mainloop()

    def buildWindow(self, window):

        """ Window construction """

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
        resetButton = tk.Button(master = statusFrame, text = "Restart", command = self.reset)

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
                thisButton = tk.Button(
                    window,
                    width = 2,
                    height = 1,
                    relief = tk.RAISED,
                    command = lambda row = buttonRow, col = buttonCol: self.dig(row, col)
                )

                # ... let the user flag that button in the game...
                thisButton.bind("<Button-3>", lambda event, row = buttonRow, col = buttonCol: self.flag(event, row, col))

                # ... put that button in the buttonArray ...
                self.buttonArray[buttonRow][buttonCol] = thisButton

                # ... and place that button in the game window
                thisButton.grid(row = buttonRow + 1, column = buttonCol)

    def flag(self, event, row, col):
        
        # thisButton: the button the user right-clicked on
        thisButton = self.buttonArray[row][col]

        # thisCell: the cell that corresponds to the button the user right-clicked on
        thisCell = self.cellArray[row][col]

        # If the cell is not already flagged and hasn't been left-clicked on...
        if not thisCell.isFlagged and not thisCell.isClicked:

            # ... change the button's color to red
            thisButton.config(bg = "red")

        # If the cell is already flagged...
        else:

            # ... change the button's color to the default
            thisButton.config(bg = "SystemButtonFace")

        # Swap the button's isFlagged state from True to False, or False to True
        thisCell.isFlagged = not thisCell.isFlagged


    def dig(self, row, column):

        """ Recursion Protection """

        # If the cell the player left-clicks on has already been clicked or flagged...
        if self.cellArray[row][column].isClicked or self.cellArray[row][column].isFlagged:

            # ... then ignore that click
            return

        """ Prime bombs """

        # If the bombs aren't primed...
        if not self.bombsPrimed:

            # ... prime the bombs
            self.primeBombs(row, column)
            
            # ... if Testing...
            if TEST:

                # ... print the Dig Testing header
                print("\n--- DIG TESTING ---\n")

        """ Dig cell """
        
        # Set the isClicked variable in the clicked cell to True
        self.cellArray[row][column].isClicked = True
        
        # clickedButton: a Tkinter button that is the button the user clicked on
        clickedButton = self.buttonArray[row][column]

        # If the clicked cell has no adjacent bombs...
        if self.cellArray[row][column].numAdjacentBombs == 0:

            # ... make the button appear clicked
            clickedButton.config(relief = tk.SUNKEN)

            # ... for each row adjacent to the clicked cell...
            for modRow in [-1, 0, 1]:

                # ... get the adjacent rows
                # newRow: the row adjacent to the clicked cell (Row above, same row, row below)
                newRow = row + modRow

                # ... if those rows are inside the game area...
                if newRow >= 0 and newRow < self.rows:

                    # ... for each adjacent column...
                    for modCol in [-1, 0, 1]:

                        # ... get the adjacent columns
                        # newCol: the column adjacent to the clicked cell (Column left, same column, column right)
                        newCol = column + modCol

                        # ... if those columns are inside the game area...
                        if newCol >= 0 and newCol < self.cols:

                            # ... if the new cell hasn't already been clicked...
                            if not self.cellArray[newRow][newCol].isClicked:
                                
                                # If Testing...
                                if TEST:
                                    print("{0}, {1} --> {2}, {3}".format(row, column, newRow, newCol))

                                # ... dig up that cell
                                self.dig(newRow, newCol)

                    
        # If the clicked cell has bombs adjacent to it...
        else:

            # ... make the button appear clicked and print the number of adjacent bombs on the button
            clickedButton.config(relief = tk.SUNKEN, text = self.cellArray[row][column].numAdjacentBombs)

            # If the cell is a bomb...
            if self.cellArray[row][column].numAdjacentBombs == -1:

                # ... change the color of the button to red to indicate that it is a bomb
                clickedButton.config(bg = "red")


    def primeBombs(self, row, column):

        """ Boolean Switch """

        # Set bombsPrimed to True, so the next dig will not prime any more bombs
        self.bombsPrimed = True

        """ Temp Array construction """

        # tempArray: a list that contains a duplicate of the cellArray, where each value is a coordinate
        tempArray = []

        # For each row in the grid...
        for tempRow in range(self.rows):

            # ... Build an empty list for the row
            tempList = []

            # ... for each column in the row...
            for tempCol in range(self.cols):

                # ... build a coordinate point
                tempCoord = [tempRow, tempCol]

                # Put that coordinate point into the tempList
                tempList.append(tempCoord)

            # Put that tempList of coordinate points into the tempArray
            tempArray.append(tempList)

        # Remove the clicked cell from the tempArray, which prevents a bomb from being placed there
        tempArray[row].pop(column)

        """ Testing """

        # If testing...
        if TEST:

            print("\n--- TEMP ARRAY TESTING ---\n")

            # For every row in the tempArray...
            for testRow in tempArray:

                # ... print the contents of that row
                print(testRow)

        """ Bomb Placement """

        # If testing...
        if TEST:

            # ... place the bomb testing header
            print("\n--- BOMB TESTING ---\n")

        # For each bomb to be placed...
        for i in range(self.numBombs):

            # randRow: an integer that contains a random number from 0 to the number of rows - 1
            randRow = random.randint(0, len(tempArray) - 1)

            # randCol: an integer that contains a random number from 0 to the number of columns - 1
            randCol = random.randint(0, len(tempArray[randRow]) - 1)

            # randCoordinate: a list that contains the coordinate point randRow, randCol
            randCoordinate = tempArray[randRow].pop(randCol)

            # If the row is empty...
            if len(tempArray[randRow]) == 0:

                # ... remove that row from tempArray
                tempArray.pop(randRow)

            # Set the cell at randCoordinate[0], randCoordinate[1] to be a bomb
            bombCell = self.cellArray[randCoordinate[0]][randCoordinate[1]]

            # Set the isBomb variable on the bomb cell to True
            bombCell.isBomb = True

            # Set the bomb's number of adjacent bombs to -1 to indicate that it is, itself, a bomb
            bombCell.numAdjacentBombs = -1            

            # For each adjacent row...
            for rowModifier in [-1, 0, 1]:

                # ... for each adjacent column...
                for colModifier in [-1, 0, 1]:

                    # ... get the adjacent row and column
                    tempRow = randCoordinate[0] + rowModifier

                    tempCol = randCoordinate[1] + colModifier

                    # If the row is in the game boundry...
                    if tempRow >= 0 and tempRow < self.rows:

                        # ... and if the column is in the game boundry...
                        if tempCol >= 0 and tempCol < self.cols:

                            # ... and if the cell is not a bomb...
                            if not self.cellArray[tempRow][tempCol].isBomb:

                                # ... increase the number of adjacent bombs for that cell
                                self.cellArray[tempRow][tempCol].numAdjacentBombs += 1

                                """ TESTING """

                                # If testing...
                                if TEST:

                                    # ... print out the number of adjacent bombs on that cell
                                    self.buttonArray[tempRow][tempCol].config(text = self.cellArray[tempRow][tempCol].numAdjacentBombs)

                            else:

                                if TEST:

                                    self.buttonArray[tempRow][tempCol].config(bg = "red")

        # If testing...
        if TEST:

            # tempIndex: an integer that holds the number of times this test has been printed
            tempIndex = 1

            # For each row in the game...
            for row in range(len(self.cellArray)):

                # ... for each column in the row...
                for col in range(len(self.cellArray[row])):

                    # ... if the cell in self.cellArray[row][col] is a bomb...
                    if self.cellArray[row][col].isBomb:

                        # ... print "{tempIndex}: {row}, {col}" to indicate that the cell there is a bomb
                        print("{0}, {1} is a bomb".format(row, col))

                        # Increase the tempIndex counter by 1
                        tempIndex += 1

    def reset(self):

        # For each row in the game...
        for row in range(self.rows):

            # ... for each column in the game...
            for column in range(self.cols):

                thisButton = self.buttonArray[row][column]

                # ... reset the buttons to the default color, relief, and text
                thisButton.config(bg = "SystemButtonFace", relief = tk.RAISED, text = "")

                thisCell = self.cellArray[row][column]

                thisCell.isBomb = False

                thisCell.isClicked = False

                thisCell.isFlagged = False

                thisCell.numAdjacentBombs = 0

        # Set bombsPrimed to False, so the next dig will re-prime the bombs
        self.bombsPrimed = False

        """ Testing """

        if TEST:

            print("\n\n\n Resetting... \n\n\n")
        
app = minesweeper()
app.main()
