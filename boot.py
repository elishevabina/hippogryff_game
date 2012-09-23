"""Implements OpenBoot"""

from end_game import EndGame
from ask_questions import *
import random

class OpenBoot(object):
	"""plays the opening of the boot and sends the user to the questioning activity."""
	
	def __init__(self, boot_type):
		"""sets self.boot_type to either AskMultQuestions or AskSpanishQuestions.
		These are classes, and an instance of the class will be returned
		by self.go()"""
		
		self.boot_type = boot_type		

	
	def go(self):
		print "Inside the boot is a jeweled box.  As you and Ting Pao excitedly show",
		print "Ping Tao, the jewels on the box start flashing.  You notice that the",
		print "flashing jewels spell out words.  The words say,"
		print "\n'Hello, friends.  I have some questions for you three. ",
		print "If you can answer them all correctly, I will open for you.",
		print "Here is the first question:'"
		next = self.boot_type()
		return next
		


		
		
from home import Home
