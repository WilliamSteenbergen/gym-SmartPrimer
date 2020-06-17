# Version 1
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
The rewards differ whether one uses the Deterministic, Medium or Realistic/Hard environment. The rewards are based
on the difference between the hints children need and the hints we give. Depending on the environment, the rewards are
'known' after every hint (deterministic and medium), or only after the child makes the post-test (realistic/hard). See
the bottom of this document for more details.

![overview](Overview.png)


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

The idea is that the types are ordered, low types needing more help than high ones. Hint 3 gives away the answer,
which is why the lower half of the types need hint 3.


## The pre test
We then generate the performance of a child on the pre-test. The performance on the pre-test can be 0, 1 or 2 in the
deterministic and medium environment, and an integer between 0 and 9 in the realistic environment.

In the deterministic environment, children of type 0 to 7 score 0, types 8 to 11 score 1 and the rest scores 2.

In the medium environment children score the same as the deterministic environment with probability 0.7. With probability
0.3 they score differently.

In the hard environment, children score normally distributed, with mean as in the following table, and $\sigma^2=2$:

| Type | mean Pre-Score  |
|------|-----------------|
| 0    | 0               |
| 1    | 1               |
| 2    | 1               |
| 3    | 2               |
| 4    | 3               |
| 5    | 4               |
| 6    | 4               |
| 7    | 5               |
| 8    | 6               |
| 9    | 7               |
| 10   | 7               |
| 11   | 8               |
| 12   | 9               |
| 13   | 9               |
| 14   | 9               |


## Using words
The children use words that are directly translated to W2V representation of 4 dimensions. As such, the words are represented
by 4 dimensional lists. Every element in the list corresponds to a hint. One could think of this representation as a PCA reduction
result after taking the average of the 100 dimensional W2V vectors of all words used child by a child in between the previous hint
and the current time point.

In the deterministic environment, all elements in the vector are -2, except for the element corresponding to the hint
that the child needs at that moment, this will be 2. So for example, when a child needs hint 2, the word representation will be
[-2, -2, 2, -2]. Pay attention to the 0 indexing here.

In the medium environment, all elements in the list are ~N(-2,1), except for the hint that is needed, this has distribution
N(2,1).

In the realistic/hard environment, all elements in the list are ~N(-1,1), except for the hint that is needed, this has distribution
N(1,1).


## Reacting to hints
Children can react to hints in three ways: continue (and use words), quit (and make post-test) and finish (and make post-test).

### Quiting
If we the second (or more) wrong hint to a child, there is a probability for the child to quit. In the deterministic case,
this probability is 1, for the medium case it is 0.8 and the realistic case it is 0.5. After quiting the child will still
make the post-test.

### Finish assignment
If we gave a hint that is more advanced than the last hint that a child needs, the child finishes and starts the post-test.
For example, when a child needs hint 0 and 2 and we give hint 3, the child finishes the assignment. For now, in all environments
this happens with probability 1.

### Continue
If the child did not quit or finish the assignment, it uses new words and we have to take an action again.

## The post test
When the child quits or finishes the assignment, it starts making the post-test.

In the realistic scenario, the post-test result is defined by it's improvement over the pre-test, and works as following:

First we define the potential improvement, Pot = score<sub>max</sub> - score<sub>pre</sub>. score<sub>max</sub> is 9 in this case. The improvement
will then be defined as: N<sub>correct</sub> / N<sub>needed</sub> * Pot - λ* N<sub>wrong</sub> + ε.

N<sub>correct</sub> is the number of times we gave the needed hint, N<sub>needed</sub> is the number of hints a child needs, λ=1 is a penalty factor and ε~N(0,Pot/10), a
random element that has a higher variance if the potential is higher.