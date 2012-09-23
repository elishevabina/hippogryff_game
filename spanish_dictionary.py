# -*- coding: utf-8 -*-

class SpanishDict(object):

	def __init__(self):
		self.nouns = {"table": "mesa", "bottle": "botella", "water": "agua", 
		 	"food": "comida", "knife": "cuchillo", "word": "palabra",
		 	"gloves": "guantes", "week": "semana", "year": u"año",
		 	"hour": "hora", "beer": "cerveza", "head": "cabeza",
		 	"thing": "cosa"
		}
					  
					  
		self.days = {"today": "hoy", "tomorrow": u"mañana", "yesterday": "ayer", 
			"Monday": "lunes", "Tuesday": "martes", "Wednesday": u"miércoles",
			"Thursday": "jueves", "Friday": "viernes", "Saturday": u"sábado",
			"Sunday": "domingo"		  
		}
			 
		self.prepositions = {"on top of": "encima de", "under": "debajo de", 
			"inside": "dentro de", "before": "antes de", "after": "despues de",
			"in front of": "delante de", "beside": "al lado de", "behind": u"detrás"
		}	
							 
				
		self.verbs = {"to be able": "poder", "to use": "usar", "to go": "ir", 
		 "to make, do": "hacer", "(I) do": "hago", "(you) do": "haces",
		 "(he) does": "hace", "to come": "venir", "to see": "ver",
		 "I see": "veo", "you see": "ves", "she sees": "ve", 
		 "we see": "vemos", "they see": "ven", "(you all) see": "veis",
		 "I can": "puedo", "you can": "puedes", "he can": "puede",
		 "we can": "podemos", "you all can": "podéis", "they can": "pueden",
		 "to want": "querer", 
		 }
		 
		self.adjectives = {"small": u"pequeño", "beautiful": "hermoso", "ugly": "feo",
			  "difficult": "difícil", "easy": u"fácil", "tall": "alto", "red": "rojo",
			 }

		self.adverbs = {"maybe": u"quizás", "now": "ahora", "already": "ya", 
		   "here": u"aquí", "together": "juntos", "alone": "solo",
			}
			
		#self.unicode = {"small": u"pequeño", "easy": u"fácil", 
		#"tomorrow": u"mañana"}
			
		self.lists = [self.nouns, self.days, self.prepositions, self.verbs,
			self.adjectives, self.adverbs
		]
			
