import random

class Hangman:
    def __init__(self, word_list, num_lives=5):

        self.word_list=word_list
        self.num_lives=num_lives
        self.word= random.choice(word_list)
        self.word_guessed=['_' for _ in self.word]
        self.num_letters= len(set(self.word))
        self.list_of_guesses=[]
    
    def check_guess(self,guess):
        
        guess=guess.lower()
        
        if guess in self.word:
            
            print(f'Good guess! {guess} is in the word.')
            
            for index,letter in enumerate(self.word):
                
                if letter== guess:
                    
                    self.word_guessed[index]= guess
            
            self.num_letters -=1 
        else:
            self.num_lives-=1 #Reducing the players no of chances incase of a wrong answer.
            print(f"Sorry, {guess} is not in the word.")
            print(f' You have {self.num_lives} lives left...')
            
    
    def ask_for_input(self):
    

        self.guess= input('Please enter a single letter: ')

        if not self.guess.isalpha() or len(self.guess) != 1: #Checking if the player input valid answer.
            print("Invalid letter. Please, enter a single alphabetical character.")

        elif self.guess in self.list_of_guesses:
            print('You already tried that letter!') # If player input the same letter again. 

        else:
            self.check_guess(self.guess)
            self.list_of_guesses.append(self.guess) # Adding players input to list of guesses. 

def play_game(word_list):
    num_lives=5 #Number of chances for player to input wrong letter.
    game=Hangman(word_list,num_lives)

    while True:

        if game.num_lives==0: #Condition in the player lost all his 5 chances. 
            print("You lost!")
            break
        
        elif game.num_letters>0 : #Continue asking for input if the player still have chances.
            game.ask_for_input()
        
        else:
            print("Congrats! You won!")
            break


word_list=['banana', 'pineapple', 'blueberry','strawberry','mango']
play_game(word_list)


    
