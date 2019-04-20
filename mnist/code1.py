#this is going to be the mnist data ml model
import matplotlib as plt
import numpy as nu
import sys
import random

print("build done")
def sigmoid(x):
	return 1.0/(1.0+exp(-x))

def sigmoidprime(x):
	 return sigmoid(x)*(1-sigmoid(x))
