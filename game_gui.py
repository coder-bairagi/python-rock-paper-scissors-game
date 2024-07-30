import random
import tkinter as tk
from tkinter import messagebox

class RockPaperScissorGUI():

    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissor")
        # self.root.geometry("300x200")
        self.root.geometry("640x360")

        self.choices = ['Rock', 'Paper', 'Scissor']

        self.label = tk.Label(root, text="Choose Rock, Paper, or Scissor:", font=('Arial', 14))
        self.label.pack(pady=10)

        self.choice_var = tk.StringVar()
        self.choice_var.set(self.choices[0])  # Default choice

        self.choice_menu = tk.OptionMenu(root, self.choice_var, *self.choices)
        self.choice_menu.config(font=('Arial', 12), width=20)
        self.choice_menu.pack(pady=10)

        self.play_button = tk.Button(root, text="Play", font=('Arial', 12), width=20, command=self.play)
        self.play_button.pack(pady=10)

    def choose(self):
        return random.choice(self.choices)

    def win(self, user, machine):
        if user == machine:
            return f"It's a tie! Machine chose {machine}"
        elif (user == 'Rock' and machine == 'Scissor') or \
             (user == 'Paper' and machine == 'Rock') or \
             (user == 'Scissor' and machine == 'Paper'):
            return f"You Win! Machine chose {machine}"
        else:
            return f"Machine Wins. Machine chose {machine}"

    def play(self):
        machine_choice = self.choose()
        user_choice = self.choice_var.get()
        result = self.win(user_choice, machine_choice)
        messagebox.showinfo("Result", result)

if __name__ == '__main__':
    root = tk.Tk()
    RockPaperScissorGUI(root)
    root.mainloop()
