from random import uniform, seed
import math

def lerp(x, fx1, fx2):
	'''
	Lineal Interlpolation function
	'''
	return fx1 + x * (fx2 - fx1)

def smoothing(x):
	'''
	Smoothing function defined by Kim Perlin on his improved Perlin noise paper
	'''
	return x * x * x * ( x * (x * 6 -15) + 10)

class PerlinNoise:
	'''
		Custom implmentation to the Perlin noise Algortihm (is it imporved??)
		for didactical purposes
	'''
	def __init__(self, seed_no = 100):
		seed(seed_no)
		self.P0_mag = uniform(-1, 1)
		self.P1_mag = uniform(-1, 1)

		self.P0 = 0
		self.P1 = 1

		# Hashes of size 256 to avoid overflows
		# Defined by Kim Perlin in his Noise implementation
		self.hashes = [ 151, 160, 137, 91, 90, 15,
			131, 13, 201, 95, 96, 53, 194, 233, 7, 225, 140, 36, 103, 30, 69, 142, 8, 99, 37, 240, 21, 10, 23,
			190, 6, 148, 247, 120, 234, 75, 0, 26, 197, 62, 94, 252, 219, 203, 117, 35, 11, 32, 57, 177, 33,
			88, 237, 149, 56, 87, 174, 20, 125, 136, 171, 168, 68, 175, 74, 165, 71, 134, 139, 48, 27, 166,
			77, 146, 158, 231, 83, 111, 229, 122, 60, 211, 133, 230, 220, 105, 92, 41, 55, 46, 245, 40, 244,
			102, 143, 54, 65, 25, 63, 161, 1, 216, 80, 73, 209, 76, 132, 187, 208, 89, 18, 169, 200, 196,
			135, 130, 116, 188, 159, 86, 164, 100, 109, 198, 173, 186, 3, 64, 52, 217, 226, 250, 124, 123,
			5, 202, 38, 147, 118, 126, 255, 82, 85, 212, 207, 206, 59, 227, 47, 16, 58, 17, 182, 189, 28, 42,
			223, 183, 170, 213, 119, 248, 152, 2, 44, 154, 163, 70, 221, 153, 101, 155, 167, 43, 172, 9,
			129, 22, 39, 253, 19, 98, 108, 110, 79, 113, 224, 232, 178, 185, 112, 104, 218, 246, 97, 228,
			251, 34, 242, 193, 238, 210, 144, 12, 191, 179, 162, 241, 81, 51, 145, 235, 249, 14, 239, 107,
			49, 192, 214, 31, 181, 199, 106, 157, 184, 84, 204, 176, 115, 121, 50, 45, 127, 4, 150, 254,
			138, 236, 205, 93, 222, 114, 67, 29, 24, 72, 243, 141, 128, 195, 78, 66, 215, 61, 156, 180, 151 ]

	def hashed_gradient(self, x_dist):
		'''
		Rewrite of the proposed perlin noise function into a more readable function
		'''
		hash_x = self.hashes[x_dist % 255] # Limit the output to the range of 0-255
		# First we use the first 4 bits to delcare create the gradient
		beta = hash_x & 0b1111 # We use only the 4 last bits
		grad = beta & 0b111 # For the acutal value of the gradient we just use the last 3 bytes nums from (0 to 7)
		grad += 1.0 # We dont want the gradient to be 0

		# We use tha 4th byte to decide the sign of the gradient
		if (beta & 0b1000) != 0:
			return grad
		else:
			return -grad

	def calculate1D(self, x, smooth_func = smoothing, lin_interp = lerp):
		# Get the corner's positions (unit distance)
		p0 = math.floor(x)
		p1 = p0 + 1
		
		# Calculate the point relative to the gradients
		d0 = x - p0

		# Get the hased gradients
		grad_p0 = self.hashed_gradient(p0)
		grad_p1 = self.hashed_gradient(p1)

		# Interpolate the new point, given the distance from the left corner and
		# the selected gradients
		# Divide by 8 to have unit size, since the gradient values goes from [-8.0, 8.0]
		return lin_interp(smooth_func(d0), grad_p0, grad_p1) / 8
		

	def calculate1DNew(self, x, smooth_func = smoothing, lin_interp = lerp):
		'''
		Calculate the gradient with a more purer algorithm focused code
		The original Perlin noise implementation, is more focused on perfomance
		'''
		# If we are avode the current window of the Perlin noise, we create another window
		if x >= self.P1:
			self.P0_mag = self.P1_mag
			self.P1_mag = uniform(-1, 1)

			self.P0 = self.P1
			self.P1 += 1
		# Calculate the point relative to the gradients
		d0 = x - self.P0

		# Calculate the point, as in the old function
		return lin_interp(smooth_func(d0), self.P0_mag, self.P1_mag)


if __name__ == '__main__':
	from matplotlib import pyplot as plt
	from numpy import arange

	generator = PerlinNoise()
	indexes = arange(0, 10, 0.2)
	new_values = [generator.calculate1DNew(x) for x in indexes]
	old_values = [generator.calculate1D(x) for x in indexes]

	plt.plot(indexes, new_values, 'r')
	plt.plot(indexes, new_values, 'rx')

	plt.plot(indexes, old_values, 'b')
	plt.plot(indexes, old_values, 'bx')
	plt.show()


