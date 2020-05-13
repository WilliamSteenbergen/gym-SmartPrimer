import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym_SmartPrimer.envs.ChildClass import Child
import numpy as np
from gym_SmartPrimer.envs import ChildBehavior

class SmartPrimerEnv(gym.Env):
	""" Smart primer environment that simulates children trying to solve a geometry problem """

	metadata = {'render.modes': ['human']}

	def __init__(self):
		self.env = {}
		self.info = {}
		self.i = 0
		self.hints = [
		[0, 1, 2, 3],
		[0, 1, 3],
		[0, 2, 3],
		[1, 2, 3],
		[0, 3],
		[1, 3],
		[2, 3],
		[3],
		[0, 1, 2],
		[0, 1],
		[0, 2],
		[1, 2],
		[0],
		[1],
		[2]
		]
		self.childRewards = []
		self.avgRewardsPerChild = []
		self.performance = []

		self.nHints = len(self.hints)

		low = np.array((0,0,0,0,0,0,0,0), dtype=float) #pre-test, 4 words, 3 prev-hints
		high = np.array((2,1,1,1,1,1,1,1), dtype=float) #pre-test, 4 words, 3 prev-hints

		self.observation_space = spaces.Box(low, high, dtype=np.float)
		self.action_space = spaces.Discrete(4)  # action space at start is all actions, but this actions space changes
		self.reward_range = (-2, 1)

		self.reset()

	def step(self, action):
		self.prev_hint = action

		reward, done = ChildBehavior.react2hint(action, self.child)

		if not done:
			self.state = ChildBehavior.nextObservation(self.state, self.child)

		self.childRewards.append(reward)

		if done:
			self.avgRewardsPerChild.append(sum(self.childRewards)/len(self.childRewards))
			performance = self.avgRewardsPerChild[-min(len(self.avgRewardsPerChild), 100):]
			self.performance.append(np.mean(performance))

		self.info = {'avgRewardsPerChild': self.avgRewardsPerChild, 'Performance': self.performance}
		return self.state, reward, done, self.info


	def reset(self):
		self.i +=1

		#self.action_space = spaces.Discrete(4)  # action space at start is all actions
		self.child = Child(np.random.randint(0, self.nHints), self.hints)  # create a child of random type
		self.childRewards = []

		newWordOHE = [0,0,0,0]
		newWordOHE[self.child.hints[self.child.neededHint]] = 1
		self.state = np.array([self.child.pre_score] + newWordOHE + [0,0,0], dtype = np.float)
		return self.state


	def render(self, mode='human'):
		print('Did one step')

	#def close(self):
