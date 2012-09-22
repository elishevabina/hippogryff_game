#import codecs
from home import Home
from problems import *
from spanish_dictionary import SpanishDict


def offer_quit(question):
	"""returns two values, next_task and the response"""
	
	resp = raw_input("> ")
	if resp == "quit": quit()
	if resp == "I give up":
		print question.answer.decode('utf-8')
		return None, question.answer
	if resp == "home":
		return Home(), None
	else: return None, resp		#if they try to answer
	

while True:
	question = SpanishProblem(SpanishDict().unicode)
	offer_quit(question)
	