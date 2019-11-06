from StateModel import State
import numpy as np


def CDF(start, interval, delta, noise):
	'''
	Calculate integral area for the CDF in the delimited area
	'''
	return sum([ abs(noise(value)) * delta for value in np.arange(start, start + interval, delta) ]) / interval

class BruhGenerator:
	'''
	Main generator class
		First it generates the state graph with the transition probabilities
		Then it parse the model as a search tree, usign the CDF
	'''
	def __init__(self, rand_var, max_len = 200):
		'''
		Configure the BruhGenerator with a random variable func and a maximun char length
		'''
		# Generate the State Model for the Different iterations of the 'BRUH' word
		b_start = State('B')
		r_state = State('R')
		u_state = State('U')
		h_state = State('H')

		h_state.addState(0.60, h_state)

		u_state.addState(0.40, h_state)
		u_state.addState(0.0, u_state)

		r_state.addState(0.60, None)
		r_state.addState(0.20, u_state)
		r_state.addState(0.0, r_state)

		b_start.addState(0.0, r_state)

		self.start_state = b_start
		self.rand_var = rand_var
		self.max_bruh_len = max_len


	def getBruh(self, start, length = 5, delta = 2.5):
		'''
		Use the CDF function for transverse the State model, in order
		to generate different iterations of the Bruh Word
		'''
		result_str = ''

		it_state = self.start_state
		curr_len = self.max_bruh_len

		# Stablish a max len in case it gets stuck in a loop
		# Iterate trought all the states, with the CDF transitions
		while it_state != None and curr_len > 0:
			result_str += it_state.cont
			prob = CDF(start, start + length, delta, self.rand_var)
			it_state = it_state.getState(prob)

			start += length
			curr_len -= 1

		return result_str