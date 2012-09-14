class Home(object):
    """class Home(object) represents the home location, where the user must
    chose an activity."""
    
    
    def __init__(self):
           #name attribute will be useful for debugging
           self.name = "Home"
    
    def go(self):
    	"""returns an instance of the next task."""
    	print "Do you say: "
    	print "1. \"Let's go on an adventure!\""
    	print "2.\"Let's make cake.\""
    	print "3. \"I'm so sorry, but I'm busy now.  See you soon!\""
    	
    	response = raw_input("> ")
        if response == "1":
    		next = GoFishing()
    	elif response == "2":
    		next = Home()
    	elif response == "3":
    	    next = EndGame()
    	elif response == "boot":
    		next = fishing.ReelBoot()
    	else:
    		print "I'm sorry, I don't understand that."
    		next = Home()
    	
    	return next
	
	
#imports at end because they are circular
from end_game import EndGame
from fishing import GoFishing
from boot import OpenBoot

#for debugging
import fishing
		
	