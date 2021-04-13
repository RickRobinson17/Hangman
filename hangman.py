import random
from words import words
import string 

def get_valid_word(words):


    word = random.choice(words)

    while '-' in word or ' ' in word:
        word == random.choice(words)

    return word.upper()
def hangman():

    word = get_valid_word(words)

    word_letter = set(word)

    alphabet = set(string.ascii_uppercase)


    used = set()

    lives = 5
    while len(word_letter)>0 and lives> 0 :


        
        print("you have used these letters: ",' '.join(used))


        word_list =[letter if letter in used else '-' for letter in word]

        print("current word: ",''.join(word_list))
        print(f'you have: {lives} lives left')

        user_letter = input("Enter a letter: ").upper()
    
        if user_letter in alphabet - used:
            used.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
            else:
                lives -=1
        elif user_letter in used:
            print("already guessed this letter")
        else:
            print("Not valid input")
   
    print(word)
    


hangman()
