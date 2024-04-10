# Duelling DQN Implementation

This section implements a reinforcement learning agent that learns to play the classic Atari game Breakout using the Duelling Deep Q-Network (Duelling DQN) algorithm implemented in PyTorch.


## Overview:-
The Duelling DQN architecture is a variation of the Deep Q-Network (DQN) algorithm, which is a deep reinforcement learning technique that uses a deep neural network to approximate the Q-function, which represents the expected future reward for each possible action in a given state. The Duelling DQN architecture separates the network into two streams: one that estimates the state value function, and another that estimates the advantage function for each action. This allows the network to learn a more stable and accurate Q-function, leading to improved performance on various Atari games, including Breakout.

## Features:-

- Duelling DQN architecture implemented in PyTorch
- Experience replay buffer for efficient training
- Prioritized experience replay for improved sample efficiency
- Asynchronous model updates for faster training
- Evaluation of the agent's performance during training
- Saving and loading of trained models

## Steps of Execution:-

1. Install the required dependencies
2. If you experience some error similar to this:-

    ```
    MESA-LOADER: failed to open iris: /usr/lib/dri/iris_dri.so: cannot open shared object file: No such file or directory (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri, suffix _dri) failed to load driver: iris MESA-LOADER: failed to open iris: /usr/lib/dri/iris_dri.so: cannot open shared object file: No such file or directory (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri, suffix _dri) failed to load driver: iris MESA-LOADER: failed to open swrast: /usr/lib/dri/swrast_dri.so: cannot open shared object file: No such file or directory (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri, suffix _dri) failed to load driver: swrast X Error of failed request: BadValue (integer parameter out of range for operation) Major opcode of failed request: 152 (GLX) Minor opcode of failed request: 3 (X_GLXCreateContext) Value in failed request: 0x0 Serial number of failed request: 96 Current serial number in output stream: 97 Process finished with exit code 1
    ```

    Then you can try to run the following command:-

    ```
    conda install -c conda-forge libstdcxx-ng
    ```

3. Set the hyperparameters as required and run main.py
4. The agent will start training and saving the model weights in the 'models' directory
5. The training progress and evaluation results will be displayed in the console
6. Model Performance visualisation can be found in plots folder
7. Run test.py to verify the model performance

## Acknowledgement:-

The implementation was heavily influenced by the YouTube tutorials of Robert Cowher, whose content was instrumental in understanding the Duelling DQN algorithm and its application to Atari games.