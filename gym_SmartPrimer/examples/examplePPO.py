import gym
from gym import wrappers

import matplotlib.pyplot as plt
import numpy as np
from rlgraph.agents import Agent
from rlgraph.environments import OpenAIGymEnv
from rlgraph.execution import SingleThreadedWorker
import json

### NOTE ###
#if you want to use PPO that never selects the same hint twice sequentially, use the ppo_agentSmartPrimer.py
#file in gym_SmartPrimer/agents/. Copy that file and place it into the rlraph/agents directory, under
# the name 'ppo_agent' (replace the old one)

np.random.seed(1)

agent_config_path = 'ppoSmartPrimer_config.json' #configure the settings in this file
with open(agent_config_path, 'rt') as fp:
	agent_config = json.load(fp)

env = OpenAIGymEnv.from_spec({
        "type": "openai",
        "gym_env": 'gym_SmartPrimer:SmartPrimer-realistic-v0'
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

env.render()




