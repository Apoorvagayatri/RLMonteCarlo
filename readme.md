# FlapPyBird

A Flappy Bird Clone made using [Python-Pygame](http://www.pygame.org).

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Running the Game](#running-the-game)
- [Gameplay](#gameplay)
- [Training](#training)
- [Results](#results)
- [Documentation](#documentation)
- [License](#license)

## Introduction

FlapPyBird is a clone of the popular Flappy Bird game, where players control a bird and navigate through pipes by tapping the screen or pressing a key. The plain game of Flappy was taken from [@sourabhv/FlapPyBird](https://github.com/sourabhv/FlapPyBird).

## Setup

1. **Install Python 3**: Download from [here](https://www.python.org/download/releases/) or use a package manager like `brew` or `apt`.

2. **Install Dependencies**: 
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Game**: 
   ```bash
   python src/main.py
   ```

4. **Debug Mode**: To see rectangles and coordinates, run:
   ```bash
   DEBUG=True python src/main.py
   ```

## Running the Game

- Use the **Up Arrow** or **Space** key to make the bird flap.
- Press **Esc** to close the game.

## Gameplay

The objective is to navigate the bird through the pipes without hitting them. The game ends when the bird collides with a pipe or the ground.

## Training

The project includes scripts for training agents using both on-policy and off-policy Monte Carlo methods. 

- To train an agent using on-policy MC:
  ```bash
  python src/train_on_policy_mc.py
  ```

- To train an agent using off-policy MC:
  ```bash
  python src/train_off_policy_mc.py
  ```

## Results

Results from training are saved in the `results/` directory. You can visualize the results using the provided plotting scripts.

## Documentation

Comprehensive documentation is available in the `docs/` directory:

- [Observations Report](docs/observations_report.pdf)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.