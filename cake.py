class Cake(object):
	"""The cake scenario.  
	
	The numbers and everything for the problem are currently hard-wired
	into the go() method.  Could be changed if I feel like it.
	
	"""	
	
	def go(self):
		num = random.sample(range(6, 25, 3), 1)[0]
		print "Your friends come inside.  You decide to make a chocolate cake."  
		print "However, the recipe is intended for",
		print "{0} people and there are only".format(num)
		print "three of you.  If you want to make exactly enough for the three of you,"
		print "what should you divide the recipe by?"
		
		ratio = num / 3
		self.get_ratio_loop(ratio)

		print "That's right!"
		
		flour_prob = CakeProblem("flour", 2, ratio)
		sugar_prob = CakeProblem("sugar", 1, ratio)
		eggs_prob = CakeProblem('eggs', 3, ratio)
		milk_prob = CakeProblem('milk', 1.5, ratio)
		
		for prob in [flour_prob, sugar_prob, eggs_prob, milk_prob]:
			self.get_answer(prob)
		
		print """
You make the cake and it is delicious.  You eat cake and gossip
until it is time for bed.  Then you say goodbye to Ping Tao
and Ting Pao.  The next morning they come again to hang out.""",
		next = Home()
		return next
		
	def get_answer(self, problem):
		print problem.statement
		resp = self.get_float()
		for i in range(3):
			if resp == problem.answer: break
			print "Nope, try again."
			if i > 1:
				print "Remember, you are dividing the recipe by {0}.".format(problem.ratio)
			resp = self.get_float()
		if resp != problem.answer:
			self.fail_response(problem)
		print "Right!"
	
	def fail_response(self, problem):
			print "I'm afraid you still haven't got it."
			if problem.ingredient != "eggs":
				print "You would need {0} cups of {1}.".format(problem.answer, problem.ingredient)
			else:
				print "You would need {0} eggs.".format(problem.answer)
				
	def get_ratio_loop(self, right_ans):
		ans = self.get_float()
		while ans != right_ans: 
	
			if ans > right_ans: 
				print "There wouldn't be enough cake for all of you!"
			elif ans < right_ans: 
				print """
That might be good if you all want seconds, but see if you can 
figure out what to divide by to get exactly enough cake for 3 people."""
			else: 
				print "There's something wrong here."
				quit()
				
			print "Try again."
			ans = self.get_float()
	
	def get_float(self, prompt="> "):
		while True:
			ans = raw_input(prompt)
			try: 	
				ans = float(ans)
				return ans
			except ValueError:
				if ans == "quit": quit()
				else: print "Please enter a number using decimal notation."
		
	
	
	
from home import Home
from problems import CakeProblem
import random