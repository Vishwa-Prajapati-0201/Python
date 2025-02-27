# Write a class called Rock_paper_scissors that implements the logic of the game Rock paper-
# scissors. For this game the user plays against the computer for a certain number of rounds.
# Your class should have fields for the how many rounds there will be, the current round number,
# and the number of wins each player has. There should be methods for getting the computer’s
# choice, finding the winner of a round, and checking to see if someone has one the (entire)
# game. You may want more methods.

import random

class RockPaperScissors:
    choices = ["rock", "paper", "scissors"]

    def _init_(self, rounds):
        """Initialize the game with the number of rounds."""
        self.total_rounds = rounds
        self.current_round = 0
        self.user_wins = 0
        self.computer_wins = 0

    def get_computer_choice(self):
        """Randomly selects Rock, Paper, or Scissors for the computer."""
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        """Determines the winner for the round."""
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "user"
        else:
            return "computer"

    def play_round(self):
        """Plays a single round of Rock-Paper-Scissors."""
        self.current_round += 1
        print(f"\nRound {self.current_round} of {self.total_rounds}")

        user_choice = input("Enter rock, paper, or scissors: ").strip().lower()
        while user_choice not in self.choices:
            user_choice = input("Invalid choice! Enter rock, paper, or scissors: ").strip().lower()

        computer_choice = self.get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = self.determine_winner(user_choice, computer_choice)
        if winner == "user":
            print("You win this round!")
            self.user_wins += 1
        elif winner == "computer":
            print("Computer wins this round!")
            self.computer_wins += 1
        else:
            print("It's a tie!")

    def check_game_winner(self):
        """Checks if someone has won the overall game."""
        if self.user_wins > self.computer_wins:
            print("\n You win the game! ")
        elif self.computer_wins > self.user_wins: 
            print("\n Computer wins the game! ")
        else:
            print("\n The game is a tie! ")

    def play_game(self):
        """Runs the full game until all rounds are played."""
        print("\nWelcome to Rock-Paper-Scissors!")
        for _ in range(self.total_rounds):
            self.play_round()
        
        self.check_game_winner()

# Example Usage:
rounds = int(input("Enter the number of rounds to play: "))
game = RockPaperScissors(rounds)
game.play_game()