# Mastering Connect-4 game with Alpha Zero General
This project is based on [alpha-zero-general](https://github.com/suragnair/alpha-zero-general)

For my studies I have tried the alpha-zero-general with connect-4 game.
The purpose was to see if the trained models would draw after training.
The code in this project is a skeleton of the original alpha-zero-general. 

A deep neural network traning process learn how to improve its model. The winner model will be challenge by a new model. If the new model is taken to be better than the previous, then the new model will lead for next game. This routine will go on until we have two models who are invincible. The two models plays against each other, called self-play, expecting that all the games will result with draws

A second indication that our models are improved by the time of iterations, is meseaured by validation loss and policy loss. If the loss (error) is improved by each iteration then Neural Network is learning properly without overfitting. 

I have added printout inorder to calculate results of trained models validation errors and investigate improvements in self-play games.

![Self-play in connect-4](https://user-images.githubusercontent.com/45011444/130492136-2c25b8ea-7dee-4360-b7fc-a9f16cca370f.png)

![Self-play in connect-4. By the time win less](https://user-images.githubusercontent.com/45011444/130493395-c69527f4-3040-4143-a20f-fc607cf864d7.png)

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


