#TODO for different kinds of problems (multiplication, division, etc) should I use inheritance?
#they'll have all the same attributes but different init methods, so I think I'd end up
#typing almost everything over and over anyway.
class MultProblem(object):
	"""An object representing a random multiplication problem	"""
	
	def __init__(self):
		self.type = "multiplication"
		self.a = randint(1, 10)
		self.b = randint(1, 10)
		self.answer = self.a * self.b
		self.statement = "What is {0} * {1}?  ".format(self.a, self.b)
		

class HardMultProblem(object):
	"""An object representing a random hard multiplication problem."""
	
	def __init__(self):
		self.type = "hard mult"
		self.a = randint(10, 100)
		self.b = randint(1, 10)
		self.answer = self.a * self.b
		self.statement = "What is {0} * {1}?  ".format(self.a, self.b)
		
		
		
class DivProblem(object):
	"""An object representing a random division problem with no remainder."""
	
	def __init__(self):
		self.type = "division"
		self.answer = randint(1, 10)
		self.divisor = randint(1, 10)
		self.dividend = self.answer * self.divisor
		self.statement = "What is {0} / {1}? ".format(self.dividend, self.divisor)
		
		
class SpanishProblem(object):
	"""An object representing a random Spanish vocabulary flashcard"""
		
	def __init__(self, words):
		self.type = "spanish"
		self.words = words
		self.english = self.words.keys()[randint(0, len(self.words)-1)]
		self.spanish = self.words[self.english]
		self.statement = "What is \"{0}\" in Spanish?".format(self.english)
		self.answer = self.spanish
		




import random
from random import randint
