from random import uniform, seed
import math
import time
import tweepy

from BruhGenerator import BruhGenerator
from PerlinNoise import PerlinNoise

CONFIG= {}
CONFIG['T_CONSUMER_KEY'] = ''
CONFIG['T_CONSUMER_KEY_SECR'] = ''
CONFIG['T_ACCESS_TOKEN'] = ''
CONFIG['T_ACCESS_TOKEN_SECR'] = ''
CONFIG['debug'] = True

def getTwittingFunction():
	'''
	Function that returns the tweeting function
	'''
	if CONFIG['debug']:
		return print

	twi_auth = tweepy.OAuthHandler(CONFIG['T_CONSUMER_KEY'], CONFIG['T_CONSUMER_KEY_SECR'])
	twi_auth.set_access_token(CONFIG['T_ACCESS_TOKEN'], CONFIG['T_ACCESS_TOKEN_SECR'])

	t_api = tweepy.API(twi_auth)

	return t_api.update_status

seed(time.time())

perlin = PerlinNoise()

# Initiate a generator with the perlin noise function as
# the random variable for the state transitions
generator = BruhGenerator(perlin.calculate1D)

tweet = getTwittingFunction()

starting_val = uniform(0,0.5)

# Main loop
while True:
	new_bruh = generator.getBruh(starting_val)
	tweet(new_bruh)
	print('He tuiteado ', new_bruh)

	starting_val += 1

	time.sleep(60 * 30)