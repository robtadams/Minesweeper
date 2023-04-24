import tkinter as tk

def main():
    
    buildWindow()

    running = True

def buildWindow():

    # Create the Tkinter window
    window = tk.Tk()

    # Configure the window's rows and columns
    window.rowconfigure([0, 1], pad = 10, weight = 1)
    window.columnconfigure([0], pad = 10, weight = 1)

    # Build the status Frame
    statusFrame = tk.Frame(
        master = window,
        relief = tk.FLAT,
        borderwidth = 10
    )

    statusFrame.pack()
    
    newGameButton = tk.Button(master = statusFrame, image = "")
    newGameButton.pack()

main()
