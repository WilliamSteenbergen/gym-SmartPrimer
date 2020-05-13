import gym
from gym import wrappers

import matplotlib.pyplot as plt
import numpy as np
from rlgraph.agents import Agent
from rlgraph.environments import OpenAIGymEnv
from rlgraph.execution import SingleThreadedWorker
import json

np.random.seed(1)

agent_config_path = 'ppo_config.json'
with open(agent_config_path, 'rt') as fp:
	agent_config = json.load(fp)

env = OpenAIGymEnv.from_spec({
        "type": "openai",
        "gym_env": 'gym_SmartPrimer:SmartPrimer-v0'
    })

agent = Agent.from_spec(
        agent_config,
        state_space=env.state_space,
        action_space=env.action_space
    )

episode_returns = []
def episode_finished_callback(episode_return, duration, timesteps, *args, **kwargs):
	episode_returns.append(episode_return)
	if len(episode_returns) % 100 == 0:
		print("Episode {} finished: reward={:.2f}, average reward={:.2f}.".format(
			len(episode_returns), episode_return, np.mean(episode_returns[-100:])
		))

worker = SingleThreadedWorker(env_spec=lambda: env, agent=agent, render=False, worker_executes_preprocessing=False,
                                  episode_finish_callback=episode_finished_callback)

# Use exploration is true for training, false for evaluation.
worker.execute_episodes(1000, use_exploration=True)
plt.plot(env.gym_env.info['Performance'])
plt.show()



