import random
import os
attempts = 0

#into duck
print("Welcome to WordsWordsWords!")
print("You will have 6 guess to guess the right letter that is in the word.")
print(
    "After you guess the right letter it will go in to your word bank for later."
)
print("You then have 6 attempts to guess the word.\n" +
      "Using the letter you found before.\n" + "Good luck!")

play = input("Would you like to play? (y/n): ")
if play == "y":
  print("Great! Let's get started!\n")
if play == "n":
  print("Maybe next time!")
  exit()
  
#word bank

  
#3 letter words
Three = [
    "All", "Ape", "Bar", "Bat", "Cap", "Caw", "Dox", "Dug", "Eat", "Egg",
    "Far", "Fat", "Gib", "Gnu", "Him", "Hex"
]
chosen_word= random.choice(Three)

#4 letter words
Four = [
    "Able", "Acid", "Bath", "Bead", "Cabs", "Cast", "Demo", "Duck", "Echo",
    "Eros", "Face", "Fyce", "Gaid", "Gawd", "Half", "Heal"
]
chosen_word= random.choice(Four)
#5 letter words
Five = [
    "Apeak", "Abamp", "Brick", "Bawdy", "Chivy", "Chyme", "Ditzy", "Dumka",
    "Epics", "Elvan", "Faxes", "Frock", "Given", "Gawsy", "Helix", "Hawks"
]
chosen_word= random.choice(Five)
#6 letter words
Six = [
    "Abelia", "Ablate", "Blowzy", "Buqsha", "Cables", "Cabmen", "Dermic",
    "Dezinc", "Exotic", "Enolic", "Fundic", "Frolic", "Gaited", "Galiot",
    "Habits", "Hacked"
]
chosen_word= random.choice(Six)

#7 letter words
Seven = [
    "Abdomen", "Ableist", "Backfit", "Baetyls", "Cabined", "Cbrito", "Daglock", 
  "Dakoits", "earlies","Ebonics", "Fabling", "Failure", "Gahnite", "Galenic", 
  "Hackies", "Hahnium"
]
chosen_word= random.choice(Seven)

#8 letter words
Eight = [
    "Abjectly", "Aborting", "Bachelor", "Backdrop", "Cajolers", "Cajoling", "Dactylus",
  "Darksome","Earldoms", "Earplugs", "Fabulist", "Facemask", "Gapeworm", "Gambeson",
  "Halogens", "Hachures"
]
chosen_word= random.choice(Eight)

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",
            "t","u","v","w","x","y","z"]

screen = []
guessed = []
game_over = False
counter = 6

for _ in range(len(chosen_word)):
    screen += "_"
print(f"\t\t{' '.join(screen)}")
# print(hangman[0])
while not game_over:
    guess_a_letter  = input("\nGuess a letter: ").lower()

    if guess_a_letter in guessed:
        print(f"\t\tYou already guessed '{guess_a_letter}'!")
    elif guess_a_letter not in guessed:
        if guess_a_letter not in chosen_word:
            counter = counter - 1
        guessed += guess_a_letter

    for point in range(len(chosen_word)):
        letter_in_word = chosen_word[point]
        if guess_a_letter == letter_in_word:
            screen[point] = guess_a_letter

    for position in range(len(alphabet)):
        letter_in_alphabet = alphabet[position]
        if guess_a_letter == letter_in_alphabet:
            alphabet[position] = "-"

    guessed += guess_a_letter



print("Press 1: you want a 3 letter word \n" +
      "Press 2: you want a 4 letter word \n" +
      "Press 3: you want a 5 letter word \n" +
      "Press 4: you want a 6 letter word \n" +
      "Press 5: you want a 7 letter word \n" +
      "Press 6: you want a 8 letter word \n")
word_length = int(input("Enter a number: "))
if word_length == 1:
  print("You have chosen a 3 letter word.")
  chosen_word= random.choice(Three)
  
  print(random.choice(Three))
  
if word_length == 2:
  print("You have chosen a 4 letter word.")
  chosen_word= random.choice(Four)
  print(random.choice(Four))
  
if word_length == 3:
  print("You have chosen a 5 letter word.")
  chosen_word= random.choice(Five)
  print(random.choice(Five))

if word_length == 4:
  print("You have chosen a 6 letter word.")
  chosen_word= random.choice(Six)
  print(random.choice(Six))

if word_length == 5:
  print("You have chosen a 7 letter word.")
  chosen_word= random.choice(Seven)
  print(random.choice(Seven))

if word_length == 6:
  print("You have chosen a 8 letter word.")
  chosen_word= random.choice(Eight)
  print(random.choice(Eight))

play = input("Would you like to see the definition? (y/n): ")
if play == "y":
  print(("Great! Good for you! look it up!"))
  print("https://www.dictionary.com/browse/")
  exit()

if play == "n":
  print("Maybe next time!")
  exit()