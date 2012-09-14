

class OpenBoot(object):
	"""plays the opening of the boot and sends the user to the questions."""
	
	#TODO Spanish questions
	#TODO levels for math
	def __init__(self, boot_type):
		self.boot_type = boot_type		#boot types are "math" and "spanish"
		self.box_type = "spanish"
		if self.boot_type == "math":
			self.box_type = "mult"
			#self.box_type = random.sample(["mult", "div"])
	
	def go(self):
		print "Inside the boot is a jeweled box.  As you and Ting Pao excitedly show",
		print "Ping Tao, the jewels on the box start flashing.  You notice that the",
		print "flashing jewels spell out words.  The words say,"
		print "\n'Hello, friends.  I have some questions for you three. ",
		print "If you can answer them all correctly, I will open for you.",
		print "Here is the first question:'"
		if self.box_type == "mult":
			next = AskMultQuestions()
		elif self.box_type == "spanish":
			next = AskSpanishQuestions()
		else: 
			raise Exception("There's a problem with the box_type attribute.")
		return next
		

class AskQuestions(object):
	"""Asks three questions."""
	
	def __init__(self):
		self.wrong_message = "The box says, 'Sorry, that's not correct.'"
	
	def go(self):
		for i in range(3):
			problem = self.problem_type()
			print problem.statement,
			right = self.get_answer(problem)
			if not right:
				print "I'm afraid that's not right. ",
				print "If you haven't gotten it yet you're probably not going",
				print "to.  Better go practice."
				next = EndGame()
				return next
			else:
				print "Right!"
				next = BoxOpens()		#later this will make the user ascend a level, instead
		return next	
	
	def get_answer(self, problem):
		
		"""gives the user 2 chances to answer correctly.  Returns whether they got it right."""
		
		response = raw_input()		#response as a string
		for i in range(2):
			if response == problem.answer: break
			print self.wrong_message
			response = raw_input("Try again: ")
		return response == problem.answer
	
class AskSpanishQuestions(AskQuestions):
	"""Runs a spanish vocab drill"""
	
	def __init__(self):
		super(AskSpanishQuestions, self).__init__()
		self.problem_type = SpanishProblem


class AskMultQuestions(AskQuestions):
	"""Asks three multiplication questions"""
	
	def __init__(self):
		super(AskMultQuestions, self).__init__()
		self.problem_type = MultProblem
	
	def get_answer(self, problem):
	
		"""gives the user four chances to answer correctly. Returns whether they got it or not."""
		
		response = int(raw_input())
		for j in range(4):
			if response == problem.answer: break
			if j in range(2):
				print self.wrong_message
			elif j == 2:
				print "'That's still not correct. You're allowed to count on your fingers.'"
			elif j == 3: 
				print "'Still not there!  Think about it this way.  What is {0} * 10?  ".format(problem.a)
				response = int(raw_input("> "))
				if response != problem.a * 10:
					print "I'm afraid not. It's actually {0}. ".format(problem.a * 10)
				else: 
					print "Good. "
				print "Now, {0} * {1}".format(problem.a, problem.b),
				print "is less than that by a certain amount."
				print problem.statement 
			response = int(raw_input("Try again:  "))	
		return response == problem.answer
	


class BoxOpens(object):

	def go(self):
		print "Well done!  The box lid slowly opens.  Inside are four small cakes."
		print "You each take one cake, and Ping Tao puts the last inside the small box"
		print "to take back to the hippogriff.  The three of you set off for home,"
		print "eating the cakes as you go.  When you get back, Ting Pao and Ping Tao"
		print "ask, \"What shall we do now?\""
		next = Home()
		return next
		
		
import random
from home import Home
from end_game import EndGame
from problems import *