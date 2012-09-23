class Home(object):
    """class Home(object) represents the home location, where the user must
    chose an activity."""

    
    def go(self):
    	"""returns an instance of the next task."""
    	print "Do you say: "
    	print "1. \"Let's go on an adventure!\""
    	print "2. \"Let's make cake.\""
    	print "3. \"I'm so sorry, but I'm busy now.  See you soon!\""
    	
    	response = raw_input("> ")
        if response == "1":
    		next = GoFishing()
    	elif response == "2":
    		next = Cake()
    	elif response == "3":
    	    next = EndGame()
    	elif response == "boot":
    		next = fishing.ReelBoot()
    	elif response == "spanish":
    		next = AskSpanishQuestions()
    	else:
    		print "I'm sorry, I don't understand that."
    		next = Home()
    	
    	return next
	
	
#imports at end because they are circular
from end_game import EndGame
from fishing import GoFishing
from boot import OpenBoot
from cake import Cake

from ask_questions import *
import fishing
		
	