import pickle
from collections import defaultdict
import random
import numpy as np
from src.flappy import Flappy  # Ensure this imports the Flappy environment
import matplotlib.pyplot as plt

class OnPolicyMC:
    def __init__(self, env, num_episodes, epsilon=0.1, gamma=0.99):
        self.env = env
        self.num_episodes = num_episodes
        self.epsilon = epsilon
        self.gamma = gamma
        self.action_space = env.action_space  # List of action strings
        self.action_space_size = len(self.action_space)  # Number of actions
        self.Q = defaultdict(self.default_q_value)
        self.returns_sum = defaultdict(self.default_q_value)
        self.returns_count = defaultdict(self.default_q_value)
        self.rewards_per_episode = []  # Track rewards per episode
        self.q_value_changes = []  # Track Q-value changes per episode
        self.episode_lengths = []  # Track episode lengths per episode

    def default_q_value(self):
        """Returns an array of zeros with size equal to the action space size."""
        return np.zeros(self.action_space_size)

    def policy(self, state):
        """Epsilon-greedy policy for action selection."""
        if random.random() < self.epsilon:
            return random.choice(range(self.action_space_size))
        else:
            return np.argmax(self.Q[state])

    def generate_episode(self):
        """Generates an episode by interacting with the environment."""
        state = self.env.reset()
        episode = []
        done = False
        while not done:
            action_index = self.policy(state)
            action = self.action_space[action_index]  # Convert index back to action string
            next_state, reward, done = self.env.step(action)
            episode.append((state, action_index, reward))
            state = next_state
        return episode

    def update_Q(self, episode):
        """Updates the Q-values using the episode."""
        G = 0
        previous_q_values = defaultdict(self.default_q_value)  # Store previous Q-values for comparison

        for state, action_index, reward in reversed(episode):
            G = reward + self.gamma * G
            self.returns_sum[state][action_index] += G
            self.returns_count[state][action_index] += 1
            previous_q_values[state][action_index] = self.Q[state][action_index]  # Save old Q-value for tracking changes
            self.Q[state][action_index] = self.returns_sum[state][action_index] / self.returns_count[state][action_index]

        # Track Q-value change for this episode
        q_value_change = np.mean([np.linalg.norm(self.Q[state] - previous_q_values[state]) for state in self.Q])
        self.q_value_changes.append(q_value_change)

    def train(self):
        """Trains the agent using on-policy MC and tracks metrics."""
        for episode in range(self.num_episodes):
            episode_data = self.generate_episode()

            # Calculate total reward and episode length
            total_reward = sum([step[2] for step in episode_data])
            episode_length = len(episode_data)

            self.rewards_per_episode.append(total_reward)
            self.episode_lengths.append(episode_length)

            # Update Q-values and track changes
            self.update_Q(episode_data)

            # Debug prints to track training progress
            print(f"Episode {episode + 1}/{self.num_episodes}: Total Reward: {total_reward}, Episode Length: {episode_length}")

        # Save the results to a pickle file
        with open('on_policy_mc_results1.pkl', 'wb') as f:
            pickle.dump({
                'Q_values': dict(self.Q),
                'rewards_per_episode': self.rewards_per_episode,
                'q_value_changes': self.q_value_changes,
                'episode_lengths': self.episode_lengths
            }, f)

        print("Training complete. Results saved to 'on_policy_mc_results.pkl'.")

        # Plot the training progress
        self.plot_training_progress()

    def plot_training_progress(self):
        """Plots the total rewards, Q-value changes, and episode lengths."""
        plt.figure(figsize=(12, 10))

        plt.subplot(3, 1, 1)
        plt.plot(self.rewards_per_episode)
        plt.xlabel('Episode')
        plt.ylabel('Total Reward')
        plt.title('Total Reward per Episode')

        plt.subplot(3, 1, 2)
        plt.plot(self.q_value_changes)
        plt.xlabel('Episode')
        plt.ylabel('Q-value Change')
        plt.title('Q-value Change per Episode')

        plt.subplot(3, 1, 3)
        plt.plot(self.episode_lengths)
        plt.xlabel('Episode')
        plt.ylabel('Episode Length')
        plt.title('Episode Length per Episode')

        plt.tight_layout()
        plt.savefig('training_progress_on_policy1.png')
        plt.show()

if __name__ == '__main__':
    env = Flappy()
    agent = OnPolicyMC(env, num_episodes=1000)  # Adjust number of episodes as needed
    agent.train()
