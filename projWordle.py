# Wordle Assignment
# Due May 02, 2022
# Ben Coladarci

import random

# Function to open up the correct file
def openFile():
    goodFile = False
    while goodFile == False:
        fname = input("Please enter a file name: ")
        # Begin exception handling
        try:
            # Try to open the file with the given name
            wordleWordList = open(fname, 'r')
            goodFile = True
        except IOError:
            # If file name is not valid IOError exception is raised
            print("Invalid file name try again ...")
    return wordleWordList



# Function that stores the words into a list and returns the list of all words from the file
def storeWords():
    infile = openFile()
    wordList = []
    line = infile.readline()
    word = line.strip()
    while line != '':
        wordList.append(word)
        line = infile.readline()
        word = line.strip()
    infile.close()
    return wordList



# Function to randomize a seed and then grab the word from that seed position in the list
def randomWord(seedIn, wordList):
    seedList = []
    # Code to not duplicate words in a game
    for i in range(1):
          seed = random.randint(0, 2499)
          if seed not in seedList:
              seedList.append(seed)
    
    wordleWord = wordList[seed]
    return wordleWord



# Function to get the user Input
def getInput(wordList):
    while True:
        guessWord = str(input("Make a guess: "))
        guessWord = guessWord.upper()
        if len(guessWord) != 5:
            print('Invalid Entry')
            continue
        elif guessWord not in wordList:
            print("Word not in dictionary - try again...")
            continue
        else:
            return guessWord



# Function prints out 'X', 'Y', 'G' depending on the word the user guesses
def computeClue(guessWord, wordleWord):
    clue = ['X', 'X', 'X', 'X', 'X']
    wordleCopy = list(wordleWord)

    # Loop to run through all matches first
    for i in range(len(wordleCopy)):
        # Getting the letters for the guessed and correct word
        expectedChar = wordleCopy[i]
        guessChar = guessWord[i]
        # Searching for 'G' matches, changing them to '-' to avoid duplicates
        if guessChar == expectedChar:
            clue[i] = 'G'
            wordleCopy[i] = '-'
    # Now searching for 'Y' or 'X'
    for i in range(len(wordleCopy)):
        expectedChar = wordleCopy[i]
        guessChar = guessWord[i]
        if clue[i] != 'G':
            if (guessChar in wordleCopy) and (expectedChar != guessChar):
                clue[i] = 'Y'
            if guessChar not in wordleWord:
                clue[i] = 'X'

    # Adding the clues to the list
    clue = clue[0] + clue[1] + clue[2] + clue[3] + clue[4]
    print(guessWord)
    print(clue)
    return clue



        
# Function returns true or false to contine or end the program based on user input
def playAgain():
    response = str(input("\nWould you like to play again (Y or N)? "))
    response = response.upper()
    if response == 'Y':
        return True
    if response == 'N':
        return False



# Main function that handles all the functions
def main(seedIn):
    random.seed(seedIn)
    play = True
    totalScoreCount = 0
    wordList = storeWords()
    
    # Code to play while the user chooses to continue playing
    while play == True:
        score = 1
        wordleWord = randomWord(seedIn, wordList)
        guessWord = getInput(wordList)

        # Loop to get the word and compute the clue when the guessed word is wrong
        while guessWord != wordleWord and score < 6:
            computeClue(guessWord, wordleWord)
            score = score + 1
            guessWord = getInput(wordList)

        # Executes if the user didn't guess the word in under 6 tries
        if guessWord != wordleWord and score >= 6:
            computeClue(guessWord, wordleWord)
            print("Sorry, you did not guess the word: ", wordleWord)
            score = 10
            totalScoreCount = totalScoreCount + score
            print("Your overall score is ", totalScoreCount)
            play = playAgain()

        # Executes if the user guesses the correct word
        if guessWord == wordleWord:
            clue = 'GGGGG'
            print(guessWord)
            print(clue)
            # Printing the text with score
            totalScoreCount = totalScoreCount + score
            print("\nCongratulations, your wordle score for this game is ", score)
            print("Your overall score is ", totalScoreCount)
            # Asking the user if they want to play again
            play = playAgain()

    # Code to stop while the user chooses to stop playing          
    while play == False:
        print("\nThanks for playing!")
        break
