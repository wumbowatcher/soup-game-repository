##########################################
### Name: soup game repository         ###
### Version: 0.0.1                     ###
### By: WumboWatcher and Solath Prime  ###
##########################################

## imports
import os, sys, time
import random as rn
from arts import credits, logo

## helper functions
def clear() -> None:
  """ clears screen """
  os.system("clear || cls") # to clear the screen buffer!


def print_flush(text: str, seconds: float = 0.1) -> None:
    """custom print function"""
    for char in text:
        print(char, end= "", flush= True)
        time.sleep(seconds)
    print(" ", end= "\n")


## global variables

# all words must be lower case.
words: list[str] = [
  "abroad",
  "accept",
  "access",
  "across",
  "acting",
  "casual",
  "caught",
  "centre",
  "centum",
  "chance",
  "change",
  "beaker",
  "budget",
  "better",
  "during",
  "bishop",
  "beyond",
  "costly",
  "county",
]


# to allow for user asked hints
another_words:list[ dict[ str, str ] ] = [
    {
        "word":"something",
        "hint":"this thing does that"
    }
]


# for later updates
game_settings:dict[ ( str, str | float ) ] = {
    "text_typing_speed" : 0.1
}

## game functions

def main_menu() -> None:
    clear()
    """ 
    Main menu
    we can initialize logo here ok
    """
    print(credits)


def main_settings_menu() -> None:
    """
    Settings 
    we allow for user to change settings here
    """
    ... # this means I'll implement it later!


def print_credits() -> None:
  """ prints game credits """
  print(credits)


def main_gameplay(play: bool = True) -> None:
  player_score: int = 0
  playing: bool = play
  while (playing):
    # pick word!
    word: str = rn.choice(words)
    # randomize word
    word_sh: str = "".join(rn.sample(word, len(word))) # shuffles word
    # print randomized word
    print_flush(f"score: {player_score} \nThe word is: '{word_sh}'. ", 0.1) # make it float
    inputed_word: str = input("what is the right spelling? \n>>> ").lower() # safe term
    clear()
    main_menu()

    # check up if word is right
    if (inputed_word == word):
      player_score += 1
      clear()
      main_menu()
      
    else:
      print_flush(f"The right word is: {word} \nscore: {player_score}", 0.1)
      play_again: str = input("would you like to play again? y/n: ")
      if ( play_again.lower().startswith("y")):
        playing: bool = True

      elif ( play_again.startswith("n") ):
        playing: bool = False

      else:
        print("invalid input!. ", "\nexiting...")
        time.sleep(0.5)
        break # faster



## GAME
def main() -> None:
  """ Main Game routine """
  main_menu()

  # to allow for menu choices
  player_menu_choice: str = input("do you want to play y/n: ")
  if player_menu_choice.startswith("y"):
    playing: bool = True
    
  else :
    print_flush("Then! \nwhy did you come here, user?.", 0.1)
    playing: bool = False
  
  main_gameplay(playing)
  
  clear()
  sys.exit(0)

if __name__ == "__main__":
    main()

# do i make the credits an option in the game menu?
# I'll do it for you :-)
# 
