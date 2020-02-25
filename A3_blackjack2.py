# A3_blackjack2.py
# assignment 3: blackjack game
# This is my second implementation of the blackjack game in python
import random


# --------------------------------------------------------
# deals a random card from a standard deck of 52 cards
def dealCard():
    randCard = random.choice(fullDeck)
    fullDeck.remove(randCard)
    return randCard


# ----------------------------------------------------------
# displays the set of cards that have been dealt
# takes a list of cards as the parameter
def displayHand(listOfCards):
    for k in range(len(listOfCards)):
        # end formatting prevents the print method from automatically returning a new line
        if 2 <= listOfCards[k] <= 10:
            print(listOfCards[k], end=" ")
        elif listOfCards[k] == 1:
            print("A", end=" ")
        elif listOfCards[k] == 11:
            print("J", end=" ")
        elif listOfCards[k] == 12:
            print("Q", end=" ")
        elif listOfCards[k] == 13:
            print("K", end=" ")


# ----------------------------------------------------------
# assigns a ranking according to the user's final score
def getRank(score):
    rank = ""
    if score >= 95:
        rank = "Ace!"
    elif 85 <= score <= 94:
        rank = "King"
    elif 75 <= score <= 84:
        rank = "Queen"
    elif 50 <= score <= 74:
        rank = "Jack"
    elif 25 <= score <= 49:
        rank = "Commoner"
    elif -5 <= score <= 24:
        rank = "Noob"
    return rank


# -----------------------------------------------------------
# takes a list of cards and returns the total
def sumHand(listOfCards):
    total = 0
    for element in range(len(listOfCards)):
        if 2 <= listOfCards[element] <= 10:
            total += listOfCards[element]
        # Jack, Queen, and King are worth 10 points
        elif 11 <= listOfCards[element] <= 13:
            total += 10
        # Aces are either worth 1 or 11 points
        elif listOfCards[element] == 1:
            if total > 21:
                total += 1
            else:
                total += 11
    return total


# ------------------------------------------------------------
def main():
    # start game with score of 100
    score = 100
    # displays title
    print("\n\n\n\n----------------- Welcome to Blackjack! ---------------------------")
    # game has 5 rounds
    for roundNum in range(1, 6):
        # player is dealt two cards at beginning of each new round
        newCards = [dealCard(), dealCard()]
        print("\n\nRound", roundNum, "\nScore:", score, "\nYour hand:", end=" ")
        # displays the cards
        displayHand(newCards)
        # displays the sum of the cards
        print("(", sumHand(newCards), ")")
        # repeats question until user says "stand"
        while True:
            choice = input("Would you like to 'hit' or 'stand': ")
            # hit deals a new card
            if choice == "hit":
                newCards.append(dealCard())
                print("Your hand:", end=" ")
                displayHand(newCards)
                print("(", sumHand(newCards), ")")
                # current round ends if the sum is greater than 21
                if sumHand(newCards) > 21:
                    score = score - 21
                    print("Bust!")
                    break
            # stand goes to the next round
            elif choice == "stand":
                # new score is the absolute value between the sum of the hand and 21 subtracted from current score
                score = score - abs(21 - sumHand(newCards))
                break
    print("\nFinal score:", score, ", Your rank:", getRank(score))
# --------------------------------------------------------------


# only runs the program if the command line is running this module as the main program
if __name__ == "__main__":
    # repeats until player exits game
    while True:
        # creates a new full deck
        fullDeck = []
        for j in range(4):
            for i in range(1, 14):
                fullDeck.append(i)
        # executes the main function each new game until player exits
        main()
        cont = input("Play again? (y/n) ")
        if cont == 'n':
            break

