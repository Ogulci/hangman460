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
        
        self.guess=guess.lower()
        
        if self.guess in self.word:
            
            print(f'Good guess! {self.guess} is in the word.')
            
            for index,letter in enumerate(self.word):
                
                if letter==self.guess:
                    
                    self.word_guessed[index]= self.guess
            
            self.num_letters -=1 
        else:
            self.num_lives-=1
            print(f"Sorry, {self.guess} is not in the word.")
            print(f' You have {self.num_lives} lives left...')
            
    
    def ask_for_input(self):
        while True:

            self.guess= input('Please enter a single letter: ')

            if not self.guess.isalpha() or len(self.guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif self.guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(self.guess)
                self.list_of_guesses.append(self.guess)

word_list=['banana', 'pineapple', 'blueberry','strawberry','mango']
game=Hangman(word_list)
game.ask_for_input()