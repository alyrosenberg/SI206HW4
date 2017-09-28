import random
import unittest


# SI 206 Fall 2017
# Homework 3 - Code

##COMMENT YOUR CODE WITH:
# Section Day/Time: Section 002 Thursday 8:30 AM
# People you worked with: Abigail Snyder

######### DO NOT CHANGE PROVIDED CODE #########
### Below is the same cards.py code you saw in lecture.
### Scroll down for assignment instructions.
#########

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison 

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list 
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)


def play_war_game(testing=False):
	# Call this with testing = True and it won't print out all the game stuff -- makes it hard to see test results
	player1 = Deck()
	player2 = Deck()

	p1_score = 0
	p2_score = 0

	player1.shuffle()
	player2.shuffle()
	if not testing:
		print("\n*** BEGIN THE GAME ***\n")
	for i in range(52):
		p1_card = player1.pop_card()
		p2_card = player2.pop_card()
		if not testing:
			print("Player 1 plays", p1_card,"& Player 2 plays", p2_card)

		if p1_card.rank_num > p2_card.rank_num:
			if not testing:
				print("Player 1 wins a point!")
			p1_score += 1
		elif p1_card.rank_num < p2_card.rank_num:
			if not testing:
				print("Player 2 wins a point!")
			p2_score += 1
		else:
			if not testing:
				print("Tie. Next turn.")

	if p1_score > p2_score:
		return "Player1", p1_score, p2_score
	elif p2_score > p1_score:
		return "Player2", p1_score, p2_score
	else:
		return "Tie", p1_score, p2_score

if __name__ == "__main__":
	result = play_war_game()
	print("""\n\n******\nTOTAL SCORES:\nPlayer 1: {}\nPlayer 2: {}\n\n""".format(result[1],result[2]))
	if result[0] != "Tie":
		print(result[0], "wins")
	else:
		print("TIE!")


######### DO NOT CHANGE CODE ABOVE THIS LINE #########

## You can write any additional debugging/trying stuff out code here... 
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

#########




##**##**##**##@##**##**##**## # DO NOT CHANGE OR DELETE THIS COMMENT LINE -- we use it for grading your file
###############################################

### Write unit tests below this line for the cards code above.

class test(unittest.TestCase):

# 1. Test that if you create a card with rank 12, its rank will be "Queen"
	def test_1(self):
		self.assertEqual(str(Card(2,12)).split(' ')[0], 'Queen')
		

# 2. Test that if you create a card with rank 1, its rank will be "Ace"
	def test_2(self):
		self.assertEqual(str(Card(0,1)).split(' ')[0], 'Ace')
	
	
# 3. Test that if you create a card instance with rank 3, its rank will be 3
	def test_3(self):
		self.assertEqual(str(Card(1,3)).split(' ')[0], '3')

	
# 4. Test that if you create a card instance with suit 1, it will be suit "Clubs"
	def test_4(self):
		self.assertEqual(str(Card(1,12)).split(' ')[2], 'Clubs')
	
		
# 5. Test that if you create a card instance with suit 2, it will be suit "Hearts"
	def test_5(self):
		self.assertEqual(str(Card(2,12)).split(' ')[2], 'Hearts')
		
# 6. Test that if you create a card instance, it will have access to a variable suit_names
# that contains the list ["Diamonds","Clubs","Hearts","Spades"]
	def test_6(self):
		card6 = Card(1,2)
		self.assertEqual(card6.suit_names, ["Diamonds","Clubs","Hearts","Spades"])
			

# 7. Test that if you invoke the __str__ method of a card instance that is created with 
# suit=2, rank=7, it returns the string "7 of Hearts"
	def test_7(self):
		card7 = Card(2,7)
		self.assertEqual(card7.__str__(), '7 of Hearts')
			
# 8. Test that if you create a deck instance, it will have 52 cards in its cards instance variable
	def test_8(self):
		Deck1 = Deck()
		self.assertEqual(len(Deck1.cards), int(52))
			

# 9. Test that if you invoke the pop_card method on a deck, it will return a card instance.
	def test_9(self):
		Deck2 = Deck()
		Card9 = Card(1,3)
		self.assertEqual(type(Deck2.pop_card()), type(Card9))
			


# # 10 Test that the return value of the play_war_game function is a tuple with three elements, 
# # the first of which is a string. (This will probably require multiple test methods!)
	def test_10(self):
		tup = ('x','y',1)
		self.assertEqual(type(play_war_game(testing=True)), type(tup))
		self.assertEqual(type(tup[0]), str) 
		self.assertEqual(len(tup), int(3))
				

# # 11 and 12)  Write at least 2 additional tests (not repeats of the above described tests). 
# # Make sure to include a descriptive message in these two so we can easily see what you are testing!
 
# I am testing to see that there are 26 cards that are hearts or clubs.
	def test_11(self):
		deck3 = Deck()
		count = 0
		for card in deck3.cards:
			if card.suit == "Hearts" or card.suit == "Clubs":
				count += 1
		self.assertEqual(count, 26)

 				

# #testing to see that after using pop_card function there is one less card in the deck
	def test_12(self):
		Deck4 = Deck()
		x = len(Deck4.cards)
		lengthdeck = int(x)
		Deck4.pop_card()
		self.assertEqual(len(Deck4.cards), (lengthdeck - 1))
		



#############
## The following is a line to run all of the tests you include:
unittest.main(verbosity=2)

## verbosity 2 to see detail about the tests the code fails/passes/etc.