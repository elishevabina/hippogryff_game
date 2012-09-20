from go_fishing import GoFishing
from fishing import Fish
from home import Home


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
    	else:
    		print "I'm sorry, I don't understand that."
    		next = Home()
    	
    	return next
	
	
class GoFishing(object):
    """Represents the beginning of the fishing adventure."""
	
    def go(self):
        print "You go get your fishing rods and the three of you head to the lake."
        next = Fish(0)
        print "about to set next.first_time"
        next.first_time = True
        print "set next.first_time to True"
        return next
		
		
class Fish(object):
	
	def __init__(self, refusals):
		print "initializing Fish instance"
		self.name = "Fish"
		#the number of time the user has refused help
		self.refusals = refusals
		self.first_time = False
		print self.first_time
		print "finished initializing Fish instance"
		
	def go(self):
		print "calling Fish.go"
    	#give option to go home
		if not self.first_time:
			next = self.home_option()
			if next is not None:
				return next
			else: pass
		else: print "it is the first time"
        
        #if they don't go home, give them a boot
		print "After sitting for a while, you feel a huge tug on your line.",
		print "You start to reel it in but are having trouble. " 
		print "Do you ask for help? Say 'y' or 'n'. "
		
		resp = raw_input()
		if resp == "n":
			#should probably be modulized as a Gruesome Death class or something
			TOLERANCE = 3	#number of guesses
			if self.refusals > TOLERANCE - 2:
				print "A thunderous voice proclaims, 'Your arrogance and presumption"
				print "have angered the Angel of Cooperation!'",
				print "A monstrous being with fifteen heads appears and cuts your boat"
				print "in half with a flaming sword."
				print "As you, Ping Tao, and Ting Pao sink together into the depths,",
				print "the Leviathan and his vast brood of progeny surround you,",
				print "rending and devouring your flesh."
				print
				print "Game over."
				quit()

			print "The fish gets away and you have to rebait your line."
			next = Fish(self.refusals + 1)
		elif resp == "y":
			quit()
		else: 
			print "I don't understand that."
			next = Fish(self.refusals) 
			next.first_time = self.first_time
		return next
	
	def home_option(self):
		print "You fish for 10 minutes without catching anything.  Do you want to go home?"
		resp = raw_input().lower()
		if resp == "y" or resp == "yes": 
			next = Home()
			return next
		else: return None

 
        	

next = Home()		
while True:
	next = next.go()
	#print "next.first time is " + str(next.first_time)