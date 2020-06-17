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

NOTE: pip installation is work in progress.

One can run any of these environments by cloning this repo and then loading the environment with:

`gym.make('gym_SmartPrimer:SmartPrimer-deterministic-v0')` (for deterministic)

`gym.make('gym_SmartPrimer:SmartPrimer-medium-v0')` (for medium)

`gym.make('gym_SmartPrimer:SmartPrimer-realistic-v0')` (for realistic/hard)

