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

        # Build the game window
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
                self.buttonArray[buttonRow][buttonCol] = tk.Button(
                    window,
                    width = 2,
                    height = 1,
                    relief = tk.RAISED,
                    command = lambda row = buttonRow, col = buttonCol: self.dig(row, col)
                )

                # ... and put that button into the buttonArray
                self.buttonArray[buttonRow][buttonCol].grid(row = buttonRow + 1, column = buttonCol)

    def dig(self, row, column):

        """ Prime bombs """

        # If the bombs aren't primed...
        if not self.bombsPrimed:

            # ... prime the bombs
            self.primeBombs(row, column)

        """ Dig cell """

        clickedButton = self.buttonArray[row][column]

        clickedButton.config(relief = tk.SUNKEN, text = self.cellArray[row][column].numAdjacentBombs)

        if self.cellArray[row][column].numAdjacentBombs == -1:

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

            bombCell.isBomb = True

            bombCell.numAdjacentBombs = -1            

            """ Testing """

            # If testing...
            if TEST:

                # ... print the coordinate that was pulled from tempArray
                print("{0}: [{1}, {2}]".format(i + 1, randCoordinate[0], randCoordinate[1]))

                # ... set the color of the button to red to signify that there is a bomb there
                self.buttonArray[randCoordinate[0]][randCoordinate[1]].config(bg = "red", text = "-1")
            
            for rowModifier in [-1, 0, 1]:

                for colModifier in [-1, 0, 1]:

                    tempRow = randCoordinate[0] + rowModifier

                    tempCol = randCoordinate[1] + colModifier

                    if tempRow >= 0 and tempRow < self.rows:

                        if tempCol >= 0 and tempCol < self.cols:

                            if not self.cellArray[tempRow][tempCol].isBomb:

                                self.cellArray[tempRow][tempCol].numAdjacentBombs += 1

                                if TEST:

                                    self.buttonArray[tempRow][tempCol].config(text = self.cellArray[tempRow][tempCol].numAdjacentBombs)

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
                        print("{0} : {1}, {2} is a bomb".format(tempIndex, row, col))

                        # Increase the tempIndex counter by 1
                        tempIndex += 1

    def reset(self):

        # For each row in the game...
        for row in range(self.rows):

            # ... for each column in the game...
            for column in range(self.cols):

                # ... reset the buttons to the default color, relief, and text
                self.buttonArray[row][column].config(bg = "SystemButtonFace", relief = tk.RAISED, text = "")

                self.cellArray[row][column].isBomb = False

                self.cellArray[row][column].numAdjacentBombs = 0

        # Set bombsPrimed to False, so the next dig will re-prime the bombs
        self.bombsPrimed = False

        """ Testing """

        if TEST:

            print("\n\n\n Resetting... \n\n\n")
        
app = minesweeper()
app.main()
