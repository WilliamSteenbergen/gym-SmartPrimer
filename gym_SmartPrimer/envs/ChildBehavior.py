import numpy as np


def react2hint(action, child):
	done = False

	if child.neededHint >= len(child.hints):
		a = 1

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

	if child.wrongHints >=2 and np.random.binomial(1,1) == 1:
		reward = -2
		done = True

	elif action >= child.hints[-1]: #if we gave a new hint more or equal to needed
		done = True

	if action != 3: #if we did not give the last hint, otherwise it doesn't matter
		child.prev_q[action] = 1

	return reward, done

def nextObservation(observation_space, child):
	#the new words
	newWordOHE = [0,0,0,0]
	newWordOHE[child.hints[child.neededHint]] = 1

	#The new previous questions
	prev_q = child.prev_q

	nextObs = np.array([child.pre_score] + newWordOHE + prev_q)
	return nextObs
