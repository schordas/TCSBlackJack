# This code is made for use in The Coding School.
# Made specifically for the middle school class at Beverly Vista School
# as an introduction to IF statements.
# This is skeleton code for the students.
# They should fill in the "TO DO" section to determine the winner 
# Code is setup to support more (yet still limted) users for future coding challenges.


# Samuel Chordas
# October 2014
import random

deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,
10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]

deckReplenish = deck

deckCounter = 0
aceCounter = 0

def main():


	# Calls player choice function, returns value corresponding to the user's choice
	playerTotal = playerTurn()

	# TO DO:
		# Could we put something here? 

	# creates a string for the players total value for printing purposes
	playerTotalStr = str(playerTotal)

	# Calls player choice function, returns value corresponding to the user's choice
	dealerTotal = dealerTurn()

	# creates a string for the players total value for printing purposes
	dealerTotalStr = str(dealerTotal)



	#*****************
	# TO DO:
		# We must determine who wins, how can we do that?
		# Put your code here
	#******************




	playAgain = raw_input("Would you like to play again? Yes or No\n")
	if isYes(playAgain):
		deck = deckReplenish
		main()
	else:
		print("I hope you enjoyed the game! Bye!\n")

	return

def isYes(inputVal):
	inputVal = inputVal.lower()
	while((not (inputVal == "yes")) and (not (inputVal == "no"))):
		inputVal = raw_input("Please enter valid input\n")
		inputVal.lower()
		

	if inputVal == "yes":
		return True
	elif inputVal == "no":
		return False
	else:
		isYes(inputVal)

	return

def is_str(inputVal):
	if isinstance(inputVal, str):
		return True

	return False

def draw():
	global deckCounter
	valid = False
	card = 0
	while(not valid):
		index = random.randrange(0, 51)
		if (not (deck[index] == -1)):
			card = deck[index]
			deck[index] = -1
			deckCounter = deckCounter + 1
			valid = True
		else:
			valid = False
			continue
	return card


def aceCheck(card1, card2):
	if (card1 == 11 and card2 == 11): # handles case of 2 aces
		return 1
	return card1


def dealerTurn():
	dealerFirstCard = draw()
	dealerSecondCard = draw()

	dealerFirstCard = aceCheck(dealerFirstCard, dealerSecondCard)

	total = dealerFirstCard + dealerSecondCard

	while(total<=17):
		hitCard = draw()
		if hitCard == 11 and (total + hitcard) > 21: # handles case where ace causes bust
			hitcard = 1
		total += hitCard

	return total



def playerTurn():

	hit = True


	playerFirstCard = draw()
	playerSecondCard = draw()
	
	playerFirstCard = aceCheck(playerFirstCard, playerSecondCard)
	
	total = playerFirstCard + playerSecondCard



	while(hit):
		totalStr = str(total)
		hitDecision = raw_input("You have " + totalStr +".\nDo you want to hit? Yes or No\n")

		if isYes(hitDecision):
			hitCard = draw()
			if hitCard == 11 and (total + hitcard) > 21: # handles case where ace causes bust
				hitcard = 1
			total += hitCard
		else:
			print("Now it is the dealer's turn.\n")
			return total

		if total < 21:
			hit = True
		elif total == 21:
			print("Blackjack, can't hit.\n")
			return 21
		else:
			print("Bust, can't hit.\n")
			return 0

	print("Welcome to The Coding School version of Blackjack\n")

	print("Let the game begin.\n")

main()