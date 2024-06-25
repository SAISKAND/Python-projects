import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo,"\n")

chosen_word=random.choice(word_list)
print("The chosen word: ", chosen_word)
display=[]
lives=6
for i in range(0,len(chosen_word)):
  display.append("_")
print(f"{' '.join(display)}")
end_of_game=False

while not end_of_game:
  guess=input("\nGuess a letter: ")
  for i in range(0,len(chosen_word)):
    if guess==chosen_word[i]:
      display[i]=guess
  
  if guess not in chosen_word:
    lives-=1
    print("You have chosen the incorrect letter.Hence you will lose a life")
    print(stages[lives])
  else:
    print("You have chosen the right letter! You save your life")
  print(f"{' '.join(display)}")
  if "_" not in display:
    end_of_game=True
    print("You win")
  elif lives==0:
    end_of_game=True
    print("You lost")
