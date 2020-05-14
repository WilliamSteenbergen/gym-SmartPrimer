import numpy as np

class DynaQAgent(object):
	"""DynaQ agent"""
	def __init__(self, action_space):
		nS = 120
		nA = 4

		self.action_space = action_space
		self.prevAction = -1
		self.Q = np.zeros((nS, nA))

		self.N = np.zeros((nS + 1, nA))
		self.NA = np.zeros((nS, nS + 1, nA))
		self.NR = np.zeros((nS + 1, nA))

		self.model_P = np.zeros((nS, nS + 1, nA))
		self.model_R = np.zeros((nS + 1, nA))

		self.statesSeen = []
		self.actionsSeen = [[] for i in range(nS)]


	def act(self, observation, reward, done):
		self.prevAction += 1
		return self.prevAction
