class Cake(object):
	"""The cake scenario.  
	
	The numbers and everything for the problem are currently hard-wired
	into the go() method.  Could be changed if I feel like it.
	
	"""	
	
	def go(self):
		print "Your friends come inside.  You decide to make a chocolate cake."  
		print "However, the recipe is intended for 15 people and there are only"
		print "three of you.  If you want to make exactly enough for the three of you,"
		print "what should you divide the recipe by?"
		
		right_ans = 5
		ans = int(raw_input())
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
			ans = int(response())
		 
		print "That's right!"
		print """
You make the cake and it is delicious.  You eat cake and gossip
until it is time for bed.  Then you say goodbye to Ping Tao
and Ting Pao.  The next morning they come again to hang out.""",
		next = Home()
		return next
		
		
from home import Home