# Mastering Connect-4 game with Alpha Zero General
This project is based on https://github.com/suragnair/alpha-zero-general
For my studies I have tried the alpha-zero-general with connect-4 game.
The purpose was to see if the trained models would draw after training.
The code in this project is a skeleton of the original alpha-zero-general. 
I have added printout inorder to calculate results of trained models validation errors and investigate improvements in self-play games.
I will edit this readme with the outcome of me research.

```bash
python main.py
```
If you are interested in running this project with other parameters then modify ```main.py```.

### Experiments
I trained a PyTorch model for Connect-4 (~100 iterations, 50 episodes per iteration and 15 MCTS simulations per turn). This took about 12 hours. 

Description of relevant algorithm can be found 
1.
[Hyper-Parameter Sweep on AlphaZero General](https://arxiv.org/pdf/1903.08129.pdf).
2.
[Mastering the game of Go with deep neural networks and tree search](https://www.nature.com/articles/nature16961).
3.
[Learning to Play Othello Without Human Knowledge](https://github.com/suragnair/alpha-zero-general/raw/master/pretrained_models/writeup.pdf).


