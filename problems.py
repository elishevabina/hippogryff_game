#TODO for different kinds of problems (multiplication, division, etc) should I use inheritance?
#they'll have all the same attributes but different init methods, so I think I'd end up
#typing almost everything over and over anyway.
class MultProblem(object):
	"""An object representing a random multiplication problem	"""
	
	def __init__(self):
		self.type = "multiplication"
		self.a = randint(2, 10)
		self.b = randint(2, 10)
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
		#print "the word for this new question is: ", repr(self.english)
		#print type(self.words[self.english])
		self.spanish = self.words[self.english].encode('utf-8')
		self.statement = "What is \"{0}\" in Spanish?".format(self.english)
		self.answer = self.spanish
		
		
class CakeProblem(object):
	
	def __init__(self, ingredient, answer, ratio):
		self.type = "cake"
		self.ingredient = ingredient
		self.answer = answer
		self.ratio = ratio
		self.recipe = answer * ratio
		self.statement = """The recipe calls for {0} cups of {1}.  
How many will you need?""".format(self.recipe, self.ingredient)
		if ingredient == "eggs":
			self.statement = """The recipe calls for {0} eggs.  
How many will you need?""".format(self.recipe)
		




import random
from random import randint
