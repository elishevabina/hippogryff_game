from home import Home
from spanish_dictionary import SpanishDict
from problems import *
import codecs
import sys

class AskQuestions(object):
	"""Asks three questions."""
	
	def __init__(self):
		self.wrong_message = "The box says, 'Sorry, that's not correct.'"
		self.num_tries = 2
		self.words = {}
	
	def go(self):
		for i in range(self.num_questions):
			if self.problem_type == SpanishProblem:
				#problem = self.problem_type(SpanishDict().unicode)
				problem = self.problem_type(self.words)
			else: problem = self.problem_type()
			print problem.statement,
			next, right = self.get_answer(problem)
			if not right:
				return next
			else: 
				print "Right!"
		
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
			if type(question.answer) is str:
				print question.answer.decode('utf-8')
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
	
	def __init__(self):
		super(AskMultQuestions, self).__init__()
		self.problem_type = MultProblem
		self.num_questions = 3
		self.num_tries = 3

	
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

from boot import BoxOpens
from end_game import EndGame
import spanish_dictionary