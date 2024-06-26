from tkinter import *
from tkinter.ttk import *
import random

userChoice = "nothing yet"
computerChoice = "nothing yet"
def terminate(event=None): # exiting program
    exit()

def reset_game(): # resetting the game
    global userChoice, computerChoice
    userChoice = "nothing yet"
    computerChoice = "nothing yet"
    Player.config(text="The player chose " + userChoice)
    Computer.config(text="The computer chose " + computerChoice)
    TestLabel.config(text=" ")
    play_game() 

def scissors(event=None): #this happens when you choose scissors
    global userChoice
    userChoice = "scissors"
    print("Scissors")

def rock(event=None):     #this haappens when you choose rock
    global userChoice
    userChoice = "rock"
    print("Rock")

def paper(event=None):    #this happens when you choose paper
    global userChoice
    userChoice = "paper"
    print("Paper")

def get_computer_choice(): #this makes the 'computer' choose randomly
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(computer_choice): #this determines whether the user or the computer wins
    global userChoice #referencing the actual variable in the program
    if userChoice == computer_choice:
        TestLabel.config(text="It's a tie")
    elif (userChoice == 'rock' and computer_choice == 'scissors') or \
         (userChoice == 'paper' and computer_choice == 'rock') or \
         (userChoice == 'scissors' and computer_choice == 'paper'):
        TestLabel.config(text="You win!")
    else:
        TestLabel.config(text="Computer wins!")

def play_game():
    global userChoice
    userChoice = "nothing yet"
    Player.config(text="The player chose " + userChoice)
    
    mainWindow.update()
    
    while userChoice == "nothing yet":
        mainWindow.update()
    ExitButton.place(x=900, y= 110)

    computer_choice = get_computer_choice()
    determine_winner(computer_choice)
    Player.config(text="The player chose " + userChoice)
    Computer.config(text="The computer chose " + computer_choice)

if __name__ == "__main__":
    mainWindow = Tk()
    mainWindow.title('Main Window')
    mainWindow.geometry('1280x720+10+20')

    button_font = ("Helvetica", 16)

    TestLabel = Label(text=" ", foreground="black", font=("Helvetica", 22))
    TestLabel.place(x=500, y=100)

    Player = Label(text="The player chose " + userChoice, foreground="black", font=("Helvetica", 22))
    Player.place(x=500, y=200)

    Computer = Label(text="The computer chose " + computerChoice, foreground="black", font=("Helvetica", 22))
    Computer.place(x=500, y=300)

    style = Style()
    style.configure('TButton', font=button_font)

    Scissors = Button(text="Scissors", style='TButton')
    Scissors.place(x=840, y=610)
    Scissors.bind('<Button-1>', scissors)

    Rock = Button(text="Rock", style='TButton')
    Rock.place(x=640, y=610)
    Rock.bind('<Button-1>', rock)

    Paper = Button(text="Paper", style='TButton')
    Paper.place(x=440, y=610)
    Paper.bind('<Button-1>', paper)

    ExitButton = Button(text="Terminate Program",padding=10)
    ExitButton.bind('<Button-1>', terminate)

    ResetButton = Button(text="Restart Program",padding=10, style='TButton')
    ResetButton.place(x=100, y= 110)
    ResetButton.config(command=reset_game)

    play_game()

    mainWindow.mainloop()
