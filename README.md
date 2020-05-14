# Smartprimer simulation environment

This repository contains an OpenAI gym environment for simulating high school children that try to solve a problem and
learn a task. The goal of an algorithm in this simulation is to generate hints for the child that correspond to the
hints the child needs. The children will react to hints with words, or will finish or quit the exercise. Before the
children start the exercise, the will make a pre-test. After the children are finished, they make a post-test. The
performance of the algorithm is determined by the average difference between the post-test and pre-test.


The simulation is done by simulating the following tasks
* Doing a pre-test that is scored from 0 to 100
* Use words that correspond to the hint that the child needs
* React to hints that are given to the child by:
    * Quiting
    * Using new words for a new hint
    * Finish the assignment
* Do the post-test

There are three different environments in the current repository: [Deterministic](gym_SmartPrimer/envs/Deterministic), [Medium](gym_SmartPrimer/envs/Medium) and
[Realistic/Hard](gym_SmartPrimer/envs/Realistic_Hard).

One can run any of these environments by `pip install -e gym-SmartPrimer` and then running the following line:

`gym.make('gym_SmartPrimer:SmartPrimer-v0')` (for deterministic)
`gym.make('gym_SmartPrimer:SmartPrimer-Medium-v0')` (for medium)
`gym.make('gym_SmartPrimer:SmartPrimer-Realistic_Hard-v0')` (for realistic/hard)

## The RL situation
### The action space
In this simulation, the agent can give out 4 different actions, and thus the action space is 4 dimensional. It is always
favorable for an agent to not give the same child two of the same hints sequentially. This given fact is not in the
simulation (the action space is not dynamic), and thus should be reflected in the agent's behavior. For example, use
[PPO for SmartPrimer](gym_SmartPrimer/agents/ppo_agentSmartPrimer.py) for an adapted version of the PPO
algorithm.

### The state space
The state space is encoded by three elements:
* The pre-test score
* Words used between the last hint and the current time point
* Previously given hints

### The rewards


## The children
Every episode in the simulation is a different child. A child is generated as following:

First, we generate a random number between 0 and 14. This will be the child's 'type'. The child's type
determines what hints the child needs:

| Type | Hints needed  |
|------|---------------|
| 0    | 0 - 1 - 2 - 3 |
| 1    | 0 - 1 - 3     |
| 2    | 0 - 2 - 3     |
| 3    | 1 - 2 - 3     |
| 4    | 0 - 3         |
| 5    | 1 - 3         |
| 6    | 2 - 3         |
| 7    | 3             |
| 8    | 0 - 1 - 2     |
| 9    | 0 - 1         |
| 10   | 0 - 2         |
| 11   | 1 - 2         |
| 12   | 0             |
| 13   | 1             |
| 14   | 2             |






## The pre test

## Using words

## Reacting to hints

### Quiting
### Using words
### Finish assignment

## The post test