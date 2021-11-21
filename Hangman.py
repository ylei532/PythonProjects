import random

class HangmanGame:
    
    def __init__(self):
        self.game_over = False
        self.errors = 0
        self._word = []
        self.show_word = []
    
    def DisplayStatus(self):
        if self.errors == 0:
            print("")    
        elif self.errors == 1:
            print("-----")
        elif self.errors == 2:
            print("""  |        
  |
  |        
  |       
  |      
  | 
  |   
  |    
  |      
  |        
  |
  |        
  |       
  |      
  |
  |
  |
  |
  |
-----""")
        elif self.errors == 3:
            print("""------------------
  |        
  |        
  |     
  |       
  |    
  |
  |  
  | 
  |     
  |       
  |      
  |      
  |      
  |     
  |   
  |
  |
  |
-----""")
          
        elif self.errors == 4:
            print(("""------------------
  |        |
  |        |
  |        |
  |      
  |     
  | 
  |   
  |    
  |     
  |       
  |        
  |       
  |       
  |     
  |     
  |    
  |
  |
  |
-----"""))

        elif self.errors == 5:
            print("""------------------
  |        |
  |        |
  |        |
  |       ***
  |      *   *
  |      *   *     
  |       ***    
  |         
  |      
  |        
  |        
  |        
  |       
  |       
  |     
  |   
  |
  |
  |
-----""")
            
        elif self.errors == 6:
            print("""------------------
  |        |
  |        |
  |        |
  |       ***
  |      *   *
  |      *   *     
  |       ***    
  |        *   
  |        * 
  |        *
  |        *
  |        *
  |        
  |       
  |
  |
  |
  |
-----""")

        elif self.errors == 7:
            print("""------------------
  |        |
  |        |
  |        |
  |       ***
  |      *   *
  | *    *   *     *
  |   *   ***    *
  |    *   *   *
  |      * * *
  |        *
  |        *
  |        *
  |      
  |      
  |     
  |    
  |
  |
  |
-----""")

        elif self.errors == 8:
            print("""------------------
  |        |
  |        |
  |        |
  |       ***
  |      *   *
  | *    *   *     *
  |   *   ***    *
  |    *   *   *
  |      * * *
  |        *
  |        *
  |        *
  |       * *
  |      *   *  
  |     *     *
  |    *       *
  |
  |
  |
-----""")

    
    def GenerateWord():
        
        words = ['apple', 'banana', 'awesome', 'Microphone', 'dead', 'cool', 'super']
    
        return random.choice(words)
       
        
    def GuessWord(self, letter):
        
        correct = False
        if len(letter) == 1 and letter.isalpha():
            for char in self.word:
                if letter == char:
                    self.show_word[self.word.index(letter)] = letter
                    self.word[self.word.index(letter)] = -1
                    correct = True
                    
            if not correct:
                self.errors+=1
                
        else:
            print('Please provide a valid input (a single letter)')
        

    def DisplayWord(self):
        print("\n")
        for char in self.show_word:
            print(f"\033[4m{char}\033[0m ", end="")
        


    def Start(self):
        
        self.game_over = False
        self.errors = 0
        self.word = [char for char in HangmanGame.GenerateWord()]
        self.show_word = [" " for i in range(len(self.word))]
        
        HangmanGame.DisplayWord(self)
        while not self.game_over:
            
            letter = input('\nGuess: ')
            
            HangmanGame.GuessWord(self, letter)
            HangmanGame.DisplayStatus(self)
            HangmanGame.DisplayWord(self)
            
            if self.errors == 8:
                self.game_over = True
                
            if self.word.count(-1) == len(self.word):
                self.game_over = True
             
                
        print("\n\nGame Over")

          
def main():
    game = HangmanGame()
    game.Start()       
       
if __name__ == "__main__":
    main()    

       

      
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       