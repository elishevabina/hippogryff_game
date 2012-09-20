#!/usr/bin/python
"""This module(? script?) runs the Ping Tao and Ting Pao Game."""

from home import Home

beginning_message =  """
Ping Tao and Ting Pao, who are next door neighbors in China,
wake up one morning and decide to visit you.
They get on their hippogriff and fly to your house.  
Since you live in America and they live in China, 
it is early evening for you. 
	 "Hi, Ping Tao and Ting Pao," you say.
	 "Hello," they say, "What do you want to do today?"
"""




def play():
    """Plays the game."""
    print beginning_message
    next_task = Home()
    while True:
        next_task = next_task.go()
        #print "next_task is", next_task, type(next_task)
        print
	

play()