import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym_SmartPrimer.envs.ChildClass import Child
import numpy as np
import gym_SmartPrimer.envs.ChildBehavior as ChildBehavior

class SmartPrimerEnv(gym.Env):
	""" Smart primer environment that simulates children trying to solve a geometry problem """

	metadata = {'render.modes': ['human']}

	def __init__(self):
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
		self.nHints = len(self.hints)
		self.child = Child(np.random.uniform(0, self.nHints), self.hints)

		low = np.array((0,0,0,0,0,0,0,0), dtype=int) #pre-test, 4 words, 3 prev-hints
		high = np.array((10,1,1,1,1,1,1,1), dtype=int) #pre-test, 4 words, 3 prev-hints

		self.observation_space = spaces.Box(low, high, dtype=np.int64)
		self.action_space = spaces.Discrete(4)  # action space at start is all actions, but this actions space changes

	def step(self, action):
		self.prev_hint = action

		reward, done, info = ChildBehavior.react2hint(action, self.child)
		next_obs = ChildBehavior.nextObservation(self.observation_space, self.child)


		return next_obs, reward, done, info


	def reset(self):
		self.action_space = spaces.Discrete(4)  # action space at start is all actions
		self.child = Child(np.random.uniform(0, self.nHints), self.hints)  # create a child of random type



	def render(self, mode='human'):
		print('Did one step')

	def close(self):
		...