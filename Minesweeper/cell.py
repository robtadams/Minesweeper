class Cell():

    def __init__(self, row, column):

        # row:      an integer that contains the Y coordinate of the cell
        # The value held inside row can be from 0 to 9 (default)
        self.row = row
        
        # column:   an integer that contains the X coordinate of the cell
        # The value held inside column can be from 0 to 9 (default)
        self.column = column

        # isBomb: a boolean that keeps track if the cell is a bomb
        # A True value indicates that the cell is a bomb, a False value indicates that the cell isn't a bomb
        self.isBomb = False

        # isClicked: a boolean that keeps track if the cell has been clicked on or not
        # A True value indicates that the cell has been clicked, a False value indicates the cell hasn't been clicked
        # Note: this value may be flipped without the cell being clicked, as it may be exposed by an adjacent
        #       cell being clicked that has no adjacent bombs
        self.isClicked = False

        self.isFlagged = False

        # numAjdacentBombs: an integer that contains the number of bombs adjacent to the cell
        # The value held inside the variable can be -1 (to indicate that it is a bomb) or 0 to 8
        # If the cell has no bombs adjacent to it, then the button associated with the cell should be empty
        self.numAdjacentBombs = 0

    def dig(self):

        if isBomb:

            # TODO: Stuff later
            print("Ka-bloom!")

        else:

            # TODO: Stuff later
            print("Sploosh...")
