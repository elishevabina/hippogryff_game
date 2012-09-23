class GoFishing(object):
    """Represents the beginning of the fishing adventure."""
	
    def go(self):
        print "You go get your fishing rods and the three of you head to the lake."
        next = Fish(0)
        next.first_time = True
        return next
		
		
class Fish(object):
	"""Plays the lake where the user gets a tug on the line."""

	def __init__(self, refusals):
		
		#the number of time the user has refused help
		self.refusals = refusals
		self.first_time = False

		
	def go(self):
    	#give option to go home
		if not self.first_time:
			next = self.home_option()
			if next is not None:
				return next
			else: pass
        
        #if they don't go home, give them a boot
		print "After sitting for a while, you feel a huge tug on your line."
		print "You start to reel it in but are having trouble. " 
		print "Do you ask for help? Say 'y' or 'n'. "
		
		resp = raw_input()
		if resp == "n":
			#should probably be modulized as a Gruesome Death class or something
			TOLERANCE = 3	#number of guesses
			if self.refusals > TOLERANCE - 2:
				print "A thunderous voice proclaims, 'Your arrogance and"
				print "presumption have angered the Angel of Cooperation!'"
				print "A monstrous being with fifteen heads appears and cuts"
				print "your boat in half with a flaming sword. As you, Ping Tao"
				print "and Ting Pao sink together into the depths, the Leviathan"
				print " and his vast brood of progeny surround you, rending"
				print "and devouring your flesh."
				print
				print "Game over."
				quit()

			print "The fish gets away and you have to rebait your line."
			next = Fish(self.refusals + 1)
		elif resp == "y":
			next = ReelBoot()
		else: 
			print "I don't understand that."
			next = Fish(self.refusals) 
			next.first_time = self.first_time
		return next
	
	def home_option(self):
		print "You fish for 10 minutes without catching anything.  Do you want to go home?"
		resp = raw_input().lower()
		if resp == "y" or resp == "yes": 
			print
			print "You and Ping Tao and Ting Pao go home."
			print "You have to decide what to do now."
			next = Home()
			return next
		else: return None
        	
        	

class ReelBoot(object):
	"""Plays the reeling in of the boot, presenting the choice to open it or throw it back in."""
	
	boot_types = ["math", "spanish"]
	decorations = ["numbers", "letters"]
	
	#picks a random boot type and prints the appropriate messages
	def go(self): 
		type = random.randint(0, 1)
		print "Ting Pao helps you reel in your catch.  It's a huge, dripping boot"
		print "with {0} embossed on the sides!".format(self.decorations[type])
		print "Do you:"
		print "1. Look inside the boot"
		print "2. Throw it back into the lake"
		resp = raw_input()
		if resp == "1":
			next = OpenBoot(self.boot_types[type])
		else: 
			print "You rebait your line and start fishing again."
			next = Fish(0)
		return next
 

#imports at bottom to avoid circular issues 
from home import Home
from boot import OpenBoot   
import random