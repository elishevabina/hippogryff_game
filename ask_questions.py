from home import Home
from spanish_dictionary import SpanishDict
from problems import *

class AskQuestions(object):
	"""Asks three questions."""
	
	def __init__(self):
		self.wrong_message = "The box says, 'Sorry, that's not correct.'"
	
	def go(self):
		for i in range(self.num_questions):
			if self.problem_type == SpanishProblem:
				problem = self.problem_type(self.words)
			else: problem = self.problem_type()
			print problem.statement,
			next, right = self.get_answer(problem)
			if not right:
				next = self.fail_response(problem)
				return next
			else: 
				print "Right!"
		
		print "The box flashes and says"
		print "\tVery good!  You have answered all my questions correctly."
		next = self.get_next_task()		#later this will make the user ascend a level, instead
		return next	
	
	def get_answer(self, problem):
		
		"""gives the user 2 chances to answer correctly.  Returns whether they got it right."""
		
		response = self.get_response()		#response as an int
		for i in range(1):
			if response == problem.answer: break
			print self.wrong_message
			response = self.get_response("Try again: ", problem)
		return response == problem.answer
	
	def get_response(self, prompt="\n> ", problem):
		"""returns the response as an int. 
		
		 The SpanishQuestions subclass needs to overwrite this."""
	
		response = raw_input(prompt)
		
		while True:
			try:
				response = int(response)
			except ValueError:
				print "Type 'quit' to quit or type a number (digits only) to answer the question." 
				response = self.offer_quit(problem)
			return response
		
	def offer_quit(self, question):
		resp = raw_input("> ")
		if resp == "quit": quit()
		if resp == "I give up":
			print question.answer
			return question.answer
		else: return resp
			
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
	
	def __init__(self):
		super(AskSpanishQuestions, self).__init__()
		self.problem_type = SpanishProblem
		self.num_questions = 6
		Dict = SpanishDict()
		self.words = Dict.lists[randint(0, len(Dict.lists)-1)]
		
	def fail_response(self, problem):
		print "I'm afraid that's still wrong. "
		print "The answer is \"{0}\"".format(problem.answer)
		next = AskSpanishQuestions()
		return next

	def get_response(self, prompt="> ", problem):
		"""returns response as a string"""
		response = raw_input(prompt)
		if response == "":
			print "Type 'quit' to quit or 'I give up' to give up,"
			print "or try to answer the question."
			response = self.offer_quit(problem)
		return response

class AskMultQuestions(AskQuestions):
	"""Asks three multiplication questions"""
	
	def __init__(self):
		super(AskMultQuestions, self).__init__()
		self.problem_type = MultProblem
		self.num_questions = 3
		self.num_tries = 3
	
	def get_answer(self, problem):
	
		"""gives the user three chances to answer correctly. Returns whether they got it or not."""
		
		response = self.get_response()
		for j in range(self.num_tries - 1):
			if response == problem.answer: break
			if j == 0:
				print self.wrong_message
			elif j == 1:
				self.hint_one(problem)
			elif j == 2: 
				self.hint_two(problem)
			response = self.get_response("Try again:  ")
		return response == problem.answer
	
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
	
	def __init__(self):
		super(AskDivQuestions, self).__init__()
		self.problem_type = DivProblem
		self.num_tries = 3
		


class AskHardMultQuestions(AskMultQuestions):
	
	def __init__(self):
		super(AskHardMultQuestions, self).__init__()
		self.problem_type = HardMultProblem
		self.num_tries = 4
		
	def hint_one(self, problem):
		print "That's still not right.  Try breaking the problem down."
		
	def hint_two(self, problem):
		print "Still not there! Think about it this way."
		
		if problem.b > 7:
			print "What is {0} * 10?  ".format(problem.a)
			response = self.get_response()
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
			response = self.get_response()
			ans = round_part * problem.b
			
			if response != ans:
				print "I'm afraid not.  It's actually {0}. ".format(ans)
			else:
				print "Good. "
				
			print "Now, what is {0} * {1}? ".format(remainder, problem.b)
			response = self.get_response()
			ans = remainder * problem.b
			
			if response != ans:
				print "Sorry, no. It's %d." % ans
			else:
				print "Good. "
				
			print "Now add these together to get the answer."
			print problem.statement

	def get_next_task(self):
		return AskQuestions.get_next_task()

from boot import BoxOpens
from end_game import EndGame
import spanish_dictionary