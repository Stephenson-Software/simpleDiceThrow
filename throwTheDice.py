from random import randint
class Dice(object):
	
	def __init__(self):
		"New Dice Created!\n"
		
	def rollDice(self):
		self.number = (randint(1, 7))
		return self.number

		
myDice = Dice()

	print "A six sided dice lays next to you. (ONCE to roll once, HUNDRED to roll a hundred times, QUIT to quit)"
	next = raw_input("> ").lower()
	
	if next == "once":
		print myDice.rollDice()
		
	elif next == "hundred":
		times = []
		for x in xrange(0,100):
			myDice.rollDice()
			times.append(myDice.number)
	
		ones = 0
		twos = 0
		threes = 0
		fours = 0
		fives = 0
		sixes = 0
		
		for num in times:
			if num == 1:
				ones = ones + 1
			elif num == 2:
				twos = twos + 1
			elif num == 3:
				threes = threes + 1
			elif num == 4:
				fours = fours + 1
			elif num == 5:
				fives = fives + 1
			elif num == 6:
				sixes = sixes + 1
		print "There were %d ones" % ones
		print "There were %d twos" % twos
		print "There were %d threes" % threes
		print "There were %d fours" % fours
		print "There were %d fives" % fives
		print "There were %d six" % sixes
		
	else:
		print "That wasn't an option silly!"