import string
import random


class BoggleBoard:
    def __init__(self, seed):
        self.board = self.generate_board(seed)

    def generate_board(self, seed):
        random.seed(seed)
        board = [[random.choice(string.ascii_uppercase) for _ in range(4)] for _ in range(4)]
        return board

    def display_board(self):
        print("+---+ +---+ +---+ +---+")
        for row in self.board:
            print("|" + "| |".join(f" {letter} " if letter else "   " for letter in row) + "|")
            print("+---+ +---+ +---+ +---+")

    def is_valid_word(self, word):
        pass  # Implement this method to check if the word is valid on the board recursively.

    def is_palindrome(self, word):
        if len(word) <= 1:
            return True
        if word[0] != word[-1]:
            return False
        return self.is_palindrome(word[1:-1])


def main():
    seed = int(input("Enter seed: "))
    boggle_board = BoggleBoard(seed)
    boggle_board.display_board()

    word = input("Enter word (in UPPERcase): ")
    if boggle_board.is_valid_word(word):
        print("Nice Job!")
        if boggle_board.is_palindrome(word):
            print(f"The word {word} is a palindrome.")
        else:
            print(f"The word {word} is not a palindrome.")

    else:
        print("I don't see that word.")
        if boggle_board.is_palindrome(word):
            print(f"The word {word} is a palindrome.")
        else:
            print(f"The word {word} is not a palindrome.")
        print("Are we looking at the same board?")


main()
