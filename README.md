# Smartprimer simulation environment

This repo contains a OpenAI gym environment for simulating high school children doing the follow tasks:
* Doing a pre-test that is scored from 0 to 100
* Use words that correspond to the hint that the child needs
* React to hints that are given to the child by:
    * Quiting
    * Using new words for a new hint
    * Finish the assignment
* Do the post-test



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