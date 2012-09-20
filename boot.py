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
from ask_questions import *