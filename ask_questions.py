"""Implements the various subclasses of AskQuestions which
run the question-asking and answering activities, using the various Problems
from the problems module.

Most of the randomization happens in the problems module, 
with the exception of the set of spanish flashcards (i.e. the category),
which is chosen randomly here in the ask_questions module.
"""

import problems
from end_game import EndGame
from spanish_dictionary import SpanishDict
from random import randint
import codecs
import sys

class AskQuestions(object):
	"""Asks three questions."""
	
	wrong_message = "The box says, 'Sorry, that's not correct.'"
	
	def go(self):
		for i in range(self.num_questions):
			if type(self) == AskSpanishQuestions:
				#problem = self.problem_type(SpanishDict().unicode)
				problem = self.problem_type(self.words)
				if i > 0 and problem.answer == last.answer:
					problem = self.problem_type(self.words)
			else: problem = self.problem_type()
			print problem.statement,
			next, right = self.get_answer(problem)
			if not right:
				return next
			else: 
				print "Right!"
			last = problem
		
		print "The box flashes and says"
		print "\tVery good!  You have answered all my questions correctly."
		next = self.get_next_task()		#later this will make the user ascend a level, instead
		return next	
	
	def hint_one(self, problem): pass
	
	def hint_two(self, problem): pass

	def get_answer(self, problem):
		"""returns two values, next_task and a boolean right, whether they got it right
		
			next_task is either the fail_response if the question
			is answered wrong, or home if the user asked to go home.
			
		"""
		
		next_task, response = self.get_response(problem)
		if next_task is not None:			#i.e. if the user wants to go home
			return next_task, False
		
		
		for j in range(self.num_tries - 1):
			if response == problem.answer: break
			if j == 0:
				print self.wrong_message
			elif j == 1:
				self.hint_one(problem)
			elif j == 2: 
				self.hint_two(problem)
			next_task, response = self.get_response(problem, "Try again:  ")
			#the Home case
			if next_task is not None: 
				return next_task, None
		#the vanilla case, at the end
		if response != problem.answer:
			next_task = self.fail_response(problem)			
		return next_task, response == problem.answer
	
	def get_response(self, problem, prompt="\n> "):
		"""returns two values, the next_task and a response	"""
		
		value_error_message = """Type 'quit' to quit or 'home' to go home, 
or type a number (digits only) to answer the question."""
		
		response = raw_input(prompt)
		if response == "quit": quit()
		while True:
			try:
				response = int(response)
				return None, response
			except ValueError:
				print value_error_message
				next_task, response = self.offer_quit(problem)
				if next_task is not None:
					return next_task, response
				else: continue
				 
			
	def offer_quit(self, question):
		"""returns two values, next_task and the response"""
		
		resp = raw_input("> ")
		if resp == "quit": quit()
		if resp == "I give up":
			if type(question.answer) is str:	#can only decode a str
				print question.answer.decode('utf-8')	#question.answer is a utf-8 str, not a unicode object
			else: 
				print question.answer
			next = self
			next.words = self.words
			return next, "something that won't equal the answer"
		if resp == "home":
			return Home(), None
		else: return None, resp		#if they try to answer
			
	def fail_response(self, problem):
		"""To be overwritten by the subclasses"""
		pass
		
	def get_next_task(self):
		"""Returns the next state."""
		next = BoxOpens()
		return next
		
		
class AskSpanishQuestions(AskQuestions):
	"""Runs a spanish vocab drill
	
	Note: the fail_response method presents the possibility that the user
	get stuck here forever, or until they learn the vocabulary.
	
	"""
	problem_type = problems.SpanishProblem
	
	def __init__(self):
		super(AskSpanishQuestions, self).__init__()
	
		self.num_questions = 6
		self.num_tries = 2
		Dict = SpanishDict()
		self.words = Dict.lists[randint(0, len(Dict.lists)-1)]
		
	def fail_response(self, problem):
		print "I'm afraid that's still wrong. "
		print "The answer is \"{0}\"".format(problem.answer)
		next = AskSpanishQuestions()
		return next

	def get_response(self, problem, prompt="\n> "):
		"""returns next_task and response as a string"""
		
		response = raw_input(prompt).decode(sys.stdin.encoding)
		if response == "quit": quit()
		if response == "":
			print "Type 'quit' to quit, 'home' to go home, 'I give up' to give up,"
			print "or try to answer the question."
			next_task, response = self.offer_quit(problem)
			if next_task is not None:
				return next_task, response
		return None, response.encode('utf-8')

class AskMultQuestions(AskQuestions):
	"""Asks three multiplication questions"""
	
	num_questions = 3
	num_tries = 3
	problem_type = problems.MultProblem
	
	def __init__(self):
		super(AskMultQuestions, self).__init__()
	
	def hint_one(self, problem):
		print "'That's still not correct. You're allowed to count on your fingers.'"
	
	def hint_two(self, problem):
		raise Exception("This should never happen.  num_tries must be wrong.")
	
	def fail_response(self, problem):
				print "I'm afraid that's not right. ",
				print "If you haven't gotten it yet you're probably not going",
				print "to.  Better go practice your times tables."
				next = EndGame()
				return next
				
	def get_next_task(self):
		print "\tNow I have some harder questions for you."
		next = AskHardMultQuestions()
		return next
	
class AskDivQuestions(AskMultQuestions):
	"""Asks three division questions"""
	
	problem_type = problems.DivProblem
	
	def __init__(self):
		super(AskDivQuestions, self).__init__()
	#	self.
		self.num_tries = 3
		


class AskHardMultQuestions(AskMultQuestions):
	
	num_tries = 4
	problem_type = problems.HardMultProblem
	
	def __init__(self):
		super(AskHardMultQuestions, self).__init__()
		
		
	def hint_one(self, problem):
		print "That's still not right.  Try breaking the problem down."
		
	def hint_two(self, problem):
		print "Still not there! Think about it this way."
		
		if problem.b > 7:
			print "What is {0} * 10?  ".format(problem.a)
			response = self.get_response(problem)[1]
			print "you said", response
			if response != problem.a * 10:
				print "I'm afraid not. It's actually {0}. ".format(problem.a * 10)
			else: 
				print "Good. "
				print "Now, {0} * {1}".format(problem.a, problem.b),
				print "is less than that by a certain amount."
				print problem.statement 
		else:
			round_part = (problem.a / 10) * 10
			remainder = problem.a % 10
			print "What is {0} * {1}?  ".format(round_part, problem.b)
			response = self.get_response(problem)[1]
			ans = round_part * problem.b
			
			if response != ans:
				print "I'm afraid not.  It's actually {0}. ".format(ans)
			else:
				print "Good. "
				
			print "Now, what is {0} * {1}? ".format(remainder, problem.b)
			response = self.get_response(problem)[1]
			ans = remainder * problem.b
			
			if response != ans:
				print "Sorry, no. It's %d." % ans
			else:
				print "Good. "
				
			print "Now add these together to get the answer."
			print problem.statement

	def get_next_task(self):
		return BoxOpens()

class BoxOpens(object):

	def go(self):
		print "Well done!  The box lid slowly opens.  Inside are four small cakes."
		print "You each take one cake, and Ping Tao puts the last inside the small box"
		print "to take back to the hippogriff.  The three of you set off for home,"
		print "eating the cakes as you go.  When you get back, Ting Pao and Ping Tao"
		print "ask, \"What shall we do now?\""
		next = Home()
		return next



from home import Home
