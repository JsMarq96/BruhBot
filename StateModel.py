class State:
	'''
	State Model class
		Given a scalar, it will choose in which on of his child models's bucket
		is contained.
		The bucket size is from 0 to the indicated size of each child
	'''
	def __init__(self, content = None):
		self.states = []
		self.cont = content

	def addState(self, prob_mass, new_state):
		'''
		Add a new state, with a asociated bucket size
		'''
		self.states.append( (prob_mass, new_state) )

	def getState(self, in_prob):
		'''
		Get the element asscoated with the probability
		'''
		# Sort all the states that are available for the inputed number
		travel_states = sorted( [(prob, state) for prob, state in self.states if in_prob >= prob], key = lambda x: x[0] )

		if len(travel_states) <= 0:
			return None
		# Get the top one
		selected = travel_states[len(travel_states)-1]
		return selected[1]

if __name__ == '__main__':

	s1 = State(1)
	s2 = State(2)
	s3 = State(3)

	start = State()

	s1.addState(0.0, s2)
	s1.addState(0.4, s3)

	print(s1.getState(0.2).cont)
	print(s1.getState(0.4).cont)
	print(s1.getState(0.7).cont)