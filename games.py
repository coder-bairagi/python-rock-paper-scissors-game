import random

class RockPaperScissor():    
    
    def __init__(self):
        self.choices = ['R', 'P', 'S']

    def choose(self):
        return random.choice(self.choices)
    
    def win(self, user, machine):
        user = user.upper()
        if user == machine:
            return f"\nResult: It's a tie! Machine choosed {machine}"
        elif (user == 'R' and machine == 'S') or (user == 'P' and machine == 'R') or (user == 'S' and machine == 'P'):
            return f"\nResult: You Win! Machine choosed {machine}"
        else:
            return f"\nResult: Machine Wins. Machine choosed {machine}"
        
    def play(self):
        exit = False
        while(exit==False):
            machine_choice = self.choose()
            user_choice = input("Please Type R for Rock, P for Paper, and S for Scissor: ")
            print(self.win(user_choice, machine_choice))
            termination = input("\nType exit for exiting the game or any key for continue playing\n")
            if termination.lower() == 'exit':
                exit = True

if __name__=='__main__':
    game = RockPaperScissor()
    game.play()