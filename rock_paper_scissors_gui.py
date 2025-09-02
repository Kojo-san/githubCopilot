import tkinter as tk
import random

CHOICES = ['rock', 'paper', 'scissors']

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

class RPSGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock Paper Scissors")
        self.geometry("350x300")
        self.player_score = 0
        self.computer_score = 0

        self.label = tk.Label(self, text="Choose: Rock, Paper, or Scissors", font=("Arial", 14))
        self.label.pack(pady=10)

        self.result_label = tk.Label(self, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self, text="Player: 0 | Computer: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        for choice in CHOICES:
            btn = tk.Button(btn_frame, text=choice.capitalize(), width=10,
                            command=lambda c=choice: self.play(c))
            btn.pack(side=tk.LEFT, padx=5)

        self.quit_btn = tk.Button(self, text="Quit", command=self.destroy)
        self.quit_btn.pack(pady=10)

    def play(self, player_choice):
        computer_choice = random.choice(CHOICES)
        result = get_winner(player_choice, computer_choice)
        if result == "You win!":
            self.player_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1
        self.result_label.config(
            text=f"You chose: {player_choice}\nComputer chose: {computer_choice}\n{result}"
        )
        self.score_label.config(
            text=f"Player: {self.player_score} | Computer: {self.computer_score}"
        )

if __name__ == "__main__":
    app = RPSGame()
    app.mainloop()