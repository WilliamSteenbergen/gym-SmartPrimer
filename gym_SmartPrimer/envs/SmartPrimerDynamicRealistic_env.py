import gym
from gym import spaces
from gym_SmartPrimer.envs.Realistic_Dynamic.ChildClassDynamic  import Child
import numpy as np
from gym_SmartPrimer.envs.Realistic_Dynamic import ChildBehaviorDynamic as ChildBehavior
import matplotlib.pyplot as plt

class SmartPrimerDynamicEnv(gym.Env):
	""" Realistic and dynamic Smart primer environment that simulates children trying to solve a geometry problem
	 using a simulation that samples from different simulations"""

	metadata = {'render.modes': ['human']}

	def __init__(self):
		self.env = {}
		self.info = {}
		#self.i = 0
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

		low = np.array((0,-2,-2,-2,-2,0,0,0), dtype=float) #pre-test, 4 words dim, 3 prev-hints
		high = np.array((9,2,2,2,2,1,1,1), dtype=float) #pre-test, 4 words dim, 3 prev-hints

		self.observation_space = spaces.Box(low, high, dtype=np.float)
		self.action_space = spaces.Discrete(4)  # action space at start is all actions, but this actions space changes
		self.reward_range = (-2, 1)

		self.reset()

	def step(self, action):
		self.prev_hint = action

		if self.simulationSetting == 0:
			reward, done = ChildBehavior.react2hint1(action, self.child)
		elif self.simulationSetting == 1:
			reward, done = ChildBehavior.react2hint2(action, self.child)
		elif self.simulationSetting == 2:
			reward, done = ChildBehavior.react2hint3(action, self.child)

		if not done:
			if self.simulationSetting == 0:
				self.state = ChildBehavior.nextObservation1(self.child)
			elif self.simulationSetting == 1:
				self.state = ChildBehavior.nextObservation2(self.child)
			elif self.simulationSetting == 2:
				self.state = ChildBehavior.nextObservation3(self.child)

		self.childRewards.append(reward)

		if done:
			self.avgRewardsPerChild.append(sum(self.childRewards)/len(self.childRewards))
			performance = self.avgRewardsPerChild[-min(len(self.avgRewardsPerChild), 100):]
			self.performance.append(np.mean(performance))

		self.info = {'avgRewardsPerChild': self.avgRewardsPerChild, 'Performance': self.performance}
		return self.state, reward, done, self.info


	def reset(self):
		self.simulationSetting = np.random.randint(0,3)
		# self.simulationSetting = 2

		self.child = Child(np.random.randint(0, self.nHints), self.hints)  # create a child of random type
		self.childRewards = []

		if self.simulationSetting == 0:
			self.state = ChildBehavior.nextObservation1(self.child)
		elif self.simulationSetting == 1:
			self.state = ChildBehavior.nextObservation2(self.child)
		elif self.simulationSetting == 2:
			self.state = ChildBehavior.nextObservation3(self.child)

		return self.state

	def render(self, mode='human'):
		plt.plot(self.info['Performance'])
		plt.show()


