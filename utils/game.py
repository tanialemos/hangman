from typing import List
import random

class Hangman:
    """Class with all logic to play a hangman game."""
    possible_words: List[str] = ["becode", "learning", "mathematics", "sessions"]

    def __init__(self):
        self.word_to_find: List[str] = []
        self.lives: int = 5
        self.correctly_guessed_letters: List[str] = []
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0

        for char in random.choice(Hangman.possible_words):
            self.word_to_find.append(char) 
            self.correctly_guessed_letters.append('_')

    def play(self) -> None:
        """Method that checks if the user input is correct."""
        user_input = input("Please provide a letter:")
        if user_input.isalpha() and len(user_input) == 1:
            self.turn_count += 1 # increment turn count only after each valid input
            if user_input in self.word_to_find:
                for index in [i for i, x in enumerate(self.word_to_find) if x == user_input]:
                    self.correctly_guessed_letters[index] = user_input.capitalize()
            else:
                self.wrongly_guessed_letters.append(user_input)
                self.lives -= 1
                self.error_count +=1          
        else:
            print(f"\n{user_input} is not valid input.")
        return

    def game_over(self):
        print("\nGAME OVER!")

    def well_played(self):
        print(f"\nWELL PLAYED!\nYou found the word: \"{''.join(self.word_to_find)}\" in {self.turn_count} turns with {self.error_count} errors!")

    def start_game(self):
        """Method that starts the game.
        It calls the method play to ask the user for input.
        If calls the methods game_over and well_playd accordingly.
        It prints the game status."""        

        print("The Hangman Game!\nGame started")
        print(f"This is the word to find: {self.correctly_guessed_letters}.")       
        while True:
            self.play()
            
            if self.lives == 0:
                self.game_over()
                break
            
            if '_' not in self.correctly_guessed_letters:
                self.well_played()
                break
            
            print(f"\ncorrectly guessed letters: {self.correctly_guessed_letters}")
            print(f"Wrong letters: {self.wrongly_guessed_letters}")
            print(f"Remaining lives: {self.lives}")
            print(f"Error count: {self.error_count}")
    






