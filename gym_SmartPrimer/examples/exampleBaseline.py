import gym
import numpy as np
import gym_SmartPrimer.agents.baselineV2 as Baseline
import matplotlib.pyplot as plt

np.random.seed(2)

env = gym.make('gym_SmartPrimer:SmartPrimer-realistic-v2')
agent = Baseline.BaselineAgent(env.action_space)

episode_count = 1000

reward = 0
done = False

for i in range(episode_count):
	if i == 100:
		stop = 1
	ob = env.reset()
	while True:
		action = agent.act(ob, reward, done)
		ob, reward, done, Baseinfo = env.step(action)
		if done:
			agent.reset()
			break

env.render()

