# BruhBot
## Twitter bot that procedurally says "Bruh"

### The project itself
I have always wondered about procedurally generated content, so I wanted a quick project to toy arround and implement a noise function.
In this proyect I programmed the Perlin Noise Generator, and a State Model (to force a coherent string structure), with probability associated transitions, like a Markov Chain. (Note: I did not feel confortable calling the State Model a Markov Chain, since the Noise generator have a memmory, and that MAYBE contradicts slightly the Markov Propierty.

### How
First, we generate the State model transitions, in which each letter is a state, with transition to the next letter and itself.
The random variable used for the transitions is the Comulative Distribution Function of a segment of the Perlin Noise.
If I just used the Perlin noise, the string may had come out completely unrecognizable, so the State Model is used for basic formatting.

### Perlin Noise Generator Implementation
The Perlin noise in N-Dimensions algortihm, consists in interpolating values between a N+1, unit distanced, random gradient vectors, in order to generate a smooth surface between the gradients. But the implmentation that Ken Perlin did, presents a more confusing implementation, with perfomance in mind. Taking into consideration the moment the paper was presented, the processing power and memmory where limited, so he implemented a pseudo-random, low-cost, hashed random gradient.
This is implemented in the `calculate1D` method in PerlinNoise.py.

I also included a more straight-forward implementation of the algorithm, in the `calculate1DNew` method, in PerlinNoise.py.
Both methods have been comented with a lot of detail, in order to provide some help undestanding both. 

### Python Dependencies
- Numpy
- Random
- Math
- Matplotlib (for testing the PerlinNoise.py)

### Launch
In order to lauch the Bot, just execute
```
python BruhBot.py
```
If you want to test the PerlinNoise.py, use
```
python PerlinNoise.py
```

### References
* [Understanding Perlin Noise](https://flafla2.github.io/2014/08/09/perlinnoise.html) Very good read, to gather some intuition and first hand knowleadge on 3D Perlin Noise, with code samples.
* [Improved Noise Implementation](https://mrl.nyu.edu/~perlin/noise/) Implementation of the improved Noise generator, by Kim Perlin, in with I based this code sample.
* [The original Perlin Noise Paper](http://delivery.acm.org/10.1145/330000/325247/p287-perlin.pdf?ip=84.89.157.24&id=325247&acc=ACTIVE%20SERVICE&key=DD1EC5BCF38B3699%2EBD9BF0B02D94E6D5%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&__acm__=1573040398_12472517b66c35499756dc7b57d7670e)

### Bruh
Bruh
