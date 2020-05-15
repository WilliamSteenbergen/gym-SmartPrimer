import gym
import numpy as np
import gym_SmartPrimer.agents.linBaseline as Baseline
import matplotlib.pyplot as plt

np.random.seed(2)

env = gym.make('gym_Smart-Primer:SmartPrimer-realistic-v0')
agent = Baseline.BaselineAgent(env.action_space)


episode_count = 500

reward = 0
done = False

for i in range(episode_count):
	if i == 100:
		stop = 1
	ob = env.reset()
	while True:
		action = agent.act(ob, reward, done)
		ob, reward, done, info = env.step(action)
		if done:
			agent.reset()
			break

#make the performance plot
env.render()
