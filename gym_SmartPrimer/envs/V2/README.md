# V2
## The RL setting
In Version 2, the agent has to decide every 30 seconds to take an action. 

### Action space
The agent can choose 4 actions: do nothing, give encouragement, give a hint or ask a question. The encouragement
and question are assumed to be hardcoded in there. The hint is just the linear hint. In summary, the agent
only decides whether to give a hint/encouragement/question, not which one.

### Observation space
The observation space consists of the following variables:

* Pre-test score
* Age
* Seconds after last interaction with the screen
* Seconds after last correct answer
* Words used in last 30 seconds (put in buckets: positive, negative or 'I don't know')
* The current sub-problem
* Seconds after last interaction with the bot
* Anxiety score

Before every moment the bot has to decide an action, the observation space is updated, see [here](Realistic/NextObservation.py).

### Reward
The reward is currently defined as the post-pre score, unless the child quits, the reward then is -2. The post
test result is calculated in this [file](Realistic/ChildBehavior.py).

The child will do the post-test if he/she finished the fourth sub-question. A child finishes a sub-question when his number of needed hints is 0, the number of needed encouragements is 0
and the number of needed timesteps is 0. How many hints/encouragements/seconds a child needs can be customly defined (see 'how to use').

## How to use
First clone the repo. See [example baseline](../../examples/exampleBaseline.py) and [example PPO](../../examples/examplePPO.py) for examples of how to use the enviornment.

You can set the types of children by editing the [children config file](Realistic/childConfig.json). The parameters in this file are defined to be the following:

* nTypes: The number of different types of children you want to create (int)
* meanAge: The mean age of the child (list of int, size nTypes). Std used for simulation is 1.
* meanPreScore: The mean pre-score of the child (list of int, size nTypes). We add randint [-2,2] to this.
* meanNeededHints: The mean number of hints a child needs to solve a sub-problem (list of int, size nTypes). Std used for simulation is 0.5 (rounded).
* meanNeededTimeAfterHints: The mean number of timesteps (30 sec) a child needs after a he/she has received meanNeededHints. (list of int, size nTypes)
* meanAnxietyScore: The mean anxiety score of a child. (list of int, size nTypes)
* meanNeededEncouragements: The mean number of encouragements a child needs to solve a sub-problem (list of int, size nTypes).
* probWordsHintNeeded: The baseline probability that a child uses words when he still needs a hint (list of int, size nTypes). Increases if previous action was question,
hint or encouragement.
* probWOrdsNoHintNeeded: The baseline probability that a child uses words when he does not need a hint anymore (list of int, size nTypes). Increases if previous action was question,
hint or encouragement.
* probWrongAnswer: The probability that a child gives the wrong answer, given that he does not give the correct answer (list of int, size nTypes).

You can set the settings of PPO here [PPO settings](../../agents/ppoSmartPrimer_config.json).

To use, you first create the environment:

```env = gym.make('gym_SmartPrimer:SmartPrimer-realistic-v2')```

Then, define the agent. For example for the baseline you can use:

```import gym_SmartPrimer.agents.baselineV2 as Baseline```
```agent = Baseline.BaselineAgent(env.action_space)```

Then you can make a step by using ```env.step(action)```, where you can define action as being the action determined by 
the agent: ```action = agent.act(ob, reward, done)```. Action should be an integer between 0 and 3. 
