import tkinter as tk
import random

global TEST
TEST = False

class minesweeper():
    def __init__(self):

        self.rows = 9
        self.cols = 9
        
        self.buttons = [[None]*self.cols for _ in range(self.rows)]

            
    def main(self):
        
        self.buildWindow()

        running = True

        self.prime()

        #while running:

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

        if TEST:
            print(row, column)
        self.buttons[row][column].config(relief = tk.SUNKEN)

    def reset(self):

        for row in self.buttons:
            for button in row:
                button.config(relief = tk.RAISED, bg = 'SystemButtonFace')

        self.prime()

    def prime(self):
        self.safe = []
        for y in range(self.cols):
            for x in range(self.rows):
                self.safe.append([y, x])
        if TEST:
            print(self.safe)
        self.primed = []
        for i in range(10):
            bomb = random.randint(0, len(self.safe) - 1)
            coords = self.safe.pop(bomb)
            self.primed.append(self.buttons[coords[0]][coords[1]])
            self.buttons[coords[0]][coords[1]].config(bg = "red")
            
    
app = minesweeper()
app.main()
