class BaselineAgent(object):
	"""Linear baseline agent that increases hints"""
	def __init__(self, action_space):
		self.action_space = action_space
		self.prevAction = -1

	def act(self, observation, reward, done):
		self.prevAction += 1
		return self.prevAction

	def reset(self):
		self.prevAction = -1