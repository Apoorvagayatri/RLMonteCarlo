import pickle
import numpy as np
import matplotlib.pyplot as plt

# Load the pickle file
with open('off_policy_mc_results.pkl', 'rb') as f:
    data = pickle.load(f)

# Extract Q-values
Q_values = data['Q_values']

# Compute state values (V(s)) by taking the max Q-value for each state
state_values = {state: max(action_values) for state, action_values in Q_values.items()}

# Plot state-action values (Q-values) for each state-action pair
def plot_q_values(Q_values):
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Prepare data for plotting
    states = list(Q_values.keys())
    actions = ['UP', 'RIGHT', 'NO_ACTION']  # Assuming these are your actions
    q_values_matrix = np.array([Q_values[state] for state in states])

    # Plot the Q-values as a bar plot
    for i, action in enumerate(actions):
        ax.bar(np.arange(len(states)) + i * 0.2, q_values_matrix[:, i], width=0.2, label=action)

    # Formatting the plot
    ax.set_xlabel('State')
    ax.set_ylabel('Q-value')
    ax.set_title('Q-values for each state-action pair')
    ax.set_xticks(np.arange(len(states)))
    ax.set_xticklabels(states, rotation=45)
    ax.legend()

    plt.tight_layout()
    plt.show()

# Plot state values (V(s)) by taking the max Q-value for each state
def plot_state_values(state_values):
    fig, ax = plt.subplots(figsize=(12, 6))

    states = list(state_values.keys())
    state_vals = list(state_values.values())

    ax.bar(states, state_vals)
    ax.set_xlabel('State')
    ax.set_ylabel('State Value (V(s))')
    ax.set_title('State Values (V(s)) for each state')
    ax.set_xticklabels(states, rotation=45)

    plt.tight_layout()
    plt.show()

# Call the plotting functions
plot_q_values(Q_values)
plot_state_values(state_values)
