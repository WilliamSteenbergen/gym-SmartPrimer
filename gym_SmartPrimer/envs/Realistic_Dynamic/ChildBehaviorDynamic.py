import numpy as np


def react2hint1(action, child):
	done = False
	reward = 0
	penalty = 0.1
	potential = 10 - child.pre_score  # 9 is max score

	if action == child.hints[child.neededHint]: #if we gave the correct hint
		child.neededHint += 1
		child.correctHints += 1

	else:
		child.wrongHints += 1

	if child.wrongHints >= 2 and np.random.binomial(1, 0.5) == 1:
		# if we've given all hints that the child needs, we achieve potential minus a penalty for wrong hints
		improvement = child.correctHints / len(child.hints) * potential
		improvement -= penalty * child.wrongHints * potential

		improvement += np.random.normal(0,
		                                 potential / 10)  # add random element to improvement, with std dependent on potential
		reward = max(improvement,0)
		done = True

	elif action >= child.hints[-1]: #if we gave a new hint more or equal to needed, the child does the post-test
		# if we've given all hints that the child needs, we achieve potential minus a penalty for wrong hints
		improvement = child.correctHints / len(child.hints) * potential
		improvement -= penalty * child.wrongHints * potential

		improvement += np.random.normal(0,
		                                potential / 10)  # add random element to improvement, with std dependent on potential

		reward = max(improvement,0)
		done = True

	if action != 3: #if we did not give the last hint, otherwise it doesn't matter
		child.prev_q[action] = 1

	return reward, done

def react2hint2(action, child):
	done = False
	reward = 0
	penalty = 0.5
	potential = 10 - child.pre_score  # 9 is max score


	if action == child.hints[child.neededHint]: #if we gave the correct hint
		child.neededHint += 1
		child.correctHints += 1

	else:
		child.wrongHints += 1

	if np.random.binomial(1, 0.01 + 0.1 * child.wrongHints) == 1:
		# if we've given all hints that the child needs, we achieve potential minus a penalty for wrong hints
		improvement = child.correctHints / len(child.hints) * potential
		improvement -= potential * penalty

		improvement += np.random.normal(0,
		                                 potential / 10)  # add random element to improvement, with std dependent on potential

		reward = max(improvement,0)
		done = True

	elif action == child.hints[-1] and action == child.hints[child.neededHint-1]: #if we gave a new hint more or equal to needed, the child does the post-test
		# if we've given all hints that the child needs, we achieve potential minus a penalty for wrong hints
		improvement = child.correctHints / len(child.hints) * potential

		improvement += np.random.normal(0,
		                                potential / 10)  # add random element to improvement, with std dependent on potential

		reward = max(improvement,0)
		done = True

	elif action == 3:
		improvement = child.correctHints / len(child.hints) * potential
		improvement -= potential * penalty * 0.5

		improvement += np.random.normal(0,
		                                potential / 10)  # add random element to improvement, with std dependent on potential

		reward = max(improvement, 0)
		done = True

	if action != 3: #if we did not give the last hint, otherwise it doesn't matter
		child.prev_q[action] = 1

	return reward, done

def react2hint3(action, child):
	done = False
	reward = 0
	penalty = 0.2
	potential = 10 - child.pre_score  # 9 is max score


	if action == child.hints[child.neededHint]: #if we gave the correct hint
		child.neededHint += 1
		child.correctHints += 1

	else:
		child.wrongHints += 1
		if action > child.hints[child.neededHint]:
			child.wrongHintsLarger += 1

	if np.random.binomial(1, 0.05 + 0.15 * child.wrongHints) == 1:
		# if we've given all hints that the child needs, we achieve potential minus a penalty for wrong hints
		improvement = child.correctHints / len(child.hints) * potential
		improvement -= penalty * child.wrongHintsLarger * potential
		improvement -= 0.5 * potential

		improvement += np.random.normal(0,
		                                 potential / 10)  # add random element to improvement, with std dependent on potential

		reward = max(improvement, 0)
		done = True

	elif (action == child.hints[-1] and child.neededHint-1 == len(child.hints) - 1) or action == 3: #if we gave a new hint more or equal to needed, the child does the post-test
		# if we've given all hints that the child needs, we achieve potential minus a penalty for wrong hints
		improvement = child.correctHints / len(child.hints) * potential
		improvement -= penalty * child.wrongHintsLarger * potential

		improvement += np.random.normal(0,
		                                potential / 10)  # add random element to improvement, with std dependent on potential

		reward = max(improvement, 0)
		done = True

	return reward, done


def nextObservation1(child):
	#the new words
	newWordW2V = [-2, -2, -2, -2]


	for i in range(0, len(newWordW2V)):
		if i == child.hints[child.neededHint]:
			newWordW2V[i] = min(2, np.random.normal(1,1))
		else:
			newWordW2V[i] = min(2, max(-2, np.random.normal(-1, 1)))


	#The new previous questions
	prev_q = child.prev_q

	# float since RLgraph requires that
	nextObs = np.array([child.pre_score] + newWordW2V + prev_q, dtype=np.float)
	return nextObs

def nextObservation2(child):
	#the new words
	newWordW2V = [-2, -2, -2, -2]


	for i in range(0, len(newWordW2V)):
		if i == child.hints[child.neededHint]:
			newWordW2V[i] = min(2, np.random.normal(0.5,1))
		else:
			newWordW2V[i] = min(2, max(-2, np.random.normal(-0.5, 1)))


	#The new previous questions
	prev_q = child.prev_q

	# float since RLgraph requires that
	nextObs = np.array([child.pre_score] + newWordW2V + prev_q, dtype=np.float)
	return nextObs

def nextObservation3(child):
	#the new words
	newWordW2V = [-2, -2, -2, -2]


	for i in range(0, len(newWordW2V)):
		if i == child.hints[child.neededHint]:
			newWordW2V[i] = min(2, np.random.normal(1, 1))
		else:
			newWordW2V[i] = min(2, max(-2, np.random.normal(-1, 1)))


	#The new previous questions
	prev_q = child.prev_q

	# float since RLgraph requires that
	nextObs = np.array([child.pre_score] + newWordW2V + prev_q, dtype=np.float)
	return nextObs
