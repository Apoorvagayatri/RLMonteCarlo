import pygame
import sys
import time
from pygame.locals import K_ESCAPE, K_UP, K_DOWN, K_RIGHT, K_LEFT, KEYDOWN, QUIT
from .entities import Background, Floor, Pipes, Player, Score, WelcomeMessage
from .utils import GameConfig, Images, Sounds, Window

class Flappy:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Flappy Bird")
        window = Window(350, 350)  # Use a smaller window for the grid
        screen = pygame.display.set_mode((window.width, window.height))
        images = Images()

        self.config = GameConfig(
            screen=screen,
            clock=pygame.time.Clock(),
            fps=30,
            window=window,
            images=images,
            sounds=Sounds(),
            gravity_interval=1  # Interval for gravity effect
        )
        self.action_space = ['UP', 'RIGHT', 'NO_ACTION']  # Define the action space

        self.background = Background(self.config)
        self.floor = Floor(self.config)
        self.player = Player(self.config)
        self.welcome_message = WelcomeMessage(self.config)
        self.pipes = Pipes(self.config)
        self.score = Score(self.config)
        self.gravity_interval = 1  # Define gravity interval here

        self.last_action_time = time.time()  # Track last action time

    def reset(self):
        """Reset the environment to start a new episode."""
        self.player.reset()
        self.pipes = Pipes(self.config)  # Reinitialize pipes
        self.last_action_time = time.time()
        return self.get_state()

    def get_state(self):
        """Return the current state as player's coordinates."""
        return tuple(self.player.position)  # Return only player's coordinates

    def step(self, action):
        """Take a step in the environment based on the action."""
        done = False
        reward = 0

        current_time = time.time()
        time_elapsed = current_time - self.last_action_time
        
        if action == 'UP':
            self.player.move_up()
            if self.player.out_of_bounds:
                reward = -500  # Penalty for moving out of bounds
                done = True

        elif action == 'RIGHT':
            self.player.move_right()
        elif action == 'NO_ACTION':
            pass  # No action taken, gravity should apply

        # Apply gravity if no action has been taken for a certain interval
        if time_elapsed >= self.config.gravity_interval and action == 'NO_ACTION':
            self.player.apply_gravity()

        # Check for collisions
        if self.player.collided(self.pipes, self.floor):
            reward = -500  # Penalty for hitting the floor or pipes
            done = True
        elif self.player.position == [3, 6]:
            reward = 500  # Win reward
            done = True
        else:
            new_column = self.player.position[0]
            progress_reward = new_column * 10  # Reward increases linearly with column
            reward = progress_reward + 100  # Base reward for moving forward

        if done:
            return self.get_state(), reward, done

        self.draw_grid()
        pygame.display.update()
        self.config.tick()
        self.config.clock.tick(self.config.fps)

        return self.get_state(), reward, done

    def draw_grid(self):
        """Draws the grid, floor, pipes, and player on the screen."""
        self.background.draw()
        self.floor.draw()
        self.pipes.draw()
        self.player.draw()

        grid_size = 7
        cell_size = self.config.window.width // grid_size
        for x in range(grid_size + 1):
            pygame.draw.line(self.config.screen, (255, 255, 255), (x * cell_size, 0), (x * cell_size, self.config.window.height))
        for y in range(grid_size + 1):
            pygame.draw.line(self.config.screen, (255, 255, 255), (0, y * cell_size), (self.config.window.width, y * cell_size))


    def display_win_message(self):
        """Display a win message and prompt the user to restart or quit."""
        self.background.draw()  # Clear screen for the win message
        self.draw_grid()
        font = pygame.font.Font(None, 74)
        win_text = font.render('You Win!', True, (255, 255, 0))
        self.config.screen.blit(win_text, (self.config.window.width // 4, self.config.window.height // 3))
        pygame.display.update()
        pygame.time.wait(2000)  # Show win message for 2 seconds

        # Wait for user input to restart or quit
        while True:
            for event in pygame.event.get():
                self.check_quit_event(event)
                if event.type == KEYDOWN:
                    if event.key == K_r:  # Press 'R' to restart
                        return 'restart'
                    elif event.key == K_q:  # Press 'Q' to quit
                        pygame.quit()
                        sys.exit()

    def game_over(self):
        """Displays game over message and waits for restart."""
        font = pygame.font.SysFont(None, 25)
        game_over_text = font.render("Game Over! Press Enter to Restart", True, (255, 255, 255))

        while True:
            self.background.draw()  # Clear the screen with black
            self.config.screen.blit(game_over_text, (20, self.config.window.height // 2))
            pygame.display.update()

            for event in pygame.event.get():
                self.check_quit_event(event)
                if event.type == KEYDOWN and event.key == K_RETURN:
                    self.reset()  # Reset game state

            self.config.clock.tick(self.config.fps)

    def check_quit_event(self, event):
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
