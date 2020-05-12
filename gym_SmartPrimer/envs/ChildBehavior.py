import numpy as np

def react2hint(action, child):
	done = False
	if action == child.hints[child.neededHint]: #if we gave the correct hint
		child.neededHint += 1
		if np.random.binomial(1,1) == 1:
			reward = 1
		else:
			reward = -0.5
	else:
		child.wrongHints += 1
		if np.random.binomial(1,1) == 1:
			reward = -0.5
		else:
			reward = 1

	if action >= child.hints[child.neededHint-1]:
		done = True

	if child.wrongHints >=2 and np.random.binomial(1,1) == 1:
		reward = -2
		done = True

	info = {}
	return reward, done, info

def nextObservation(observation_space, child):
	newWordOHE = [0,0,0,0]
	newWordOHE[child.hints[child.neededHint]] = 1

	#THIS IS WHERE I WAS LEFT
	nextObs = 1 #change this for new session


	return nextObs
