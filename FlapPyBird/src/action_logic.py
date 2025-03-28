import random

class ActionHandler:
    def __init__(self):
        self.last_action = None  # Track last action for RL
        self.action_delay = 0.1  # Delay between actions
        self.last_action_time = 0

    def reset(self):
        """Reset the action handler state."""
        self.last_action = None
        self.last_action_time = 0

    def take_action(self, action, player):
        """Programmatically take an action (0: do nothing, 1: move up, 2: move right)."""
        # Perform action based on the input
        if action == 1:
            print("Move up action taken")
            player.move_up()
        elif action == 2:
            print("Move right action taken")
            player.move_right()
        # No action or invalid action
        elif action == 0:
            print("No action taken")
            player.fall()

        # Update last action
        self.last_action = action

    def get_action(self):
        """Get a random action for testing."""
        return random.choice([0, 1, 2])  # Adjust to include move_right action
