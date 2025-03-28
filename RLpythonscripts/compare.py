import pickle
import numpy as np
import matplotlib.pyplot as plt

def load_results():
    with open('on_policy_mc_results.pkl', 'rb') as f:
        on_policy_results = pickle.load(f)
    
    with open('off_policy_mc_results.pkl', 'rb') as f:
        off_policy_results = pickle.load(f)
    
    return on_policy_results, off_policy_results

def plot_results(on_policy_results, off_policy_results):
    # Extracting metrics for comparison (modify as needed)
    on_policy_avg = np.mean(list(on_policy_results.values()), axis=0)
    off_policy_avg = np.mean(list(off_policy_results.values()), axis=0)

    plt.figure(figsize=(12, 6))
    plt.plot(on_policy_avg, label='On-Policy MC', color='blue')
    plt.plot(off_policy_avg, label='Off-Policy MC', color='red')
    plt.xlabel('States')
    plt.ylabel('Value')
    plt.title('On-Policy vs Off-Policy Monte Carlo')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    on_policy_results, off_policy_results = load_results()
    plot_results(on_policy_results, off_policy_results)
