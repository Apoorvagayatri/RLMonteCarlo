import pygame

class Player:
    def __init__(self, config):
        """Initialize player position on the grid."""
        self.config = config
        self.position = [3, 0]  # Start at grid position (4,1) equivalent to index (3,0)
        self.size = 50  # Size of each grid cell
        self.gravity_counter = 0
        self.out_of_bounds = False  # Counter to handle gravity effect

        self.image = pygame.image.load('/Users/apoorvagayatrik/Desktop/FlapPyBird-master/imgs/bird1.png')
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

    def reset(self):
        """Reset the player to the initial start position."""
        self.position = [3, 0]  # Reset to starting grid position (4,1)
        self.gravity_counter = 0
        self.out_of_bounds = False


    def move_up(self):
        """Move the player one cell up."""
        # if self.position[0] > 0:
        #     self.position[0] -= 1  # Move up in the grid
        # else:
        #     self.out_of_bounds = True
    def move_right(self):
        """Move the player one cell to the right."""
        # if self.position[1] < 6:
        #     self.position[1] += 1  # Move right in the grid

    def move_down(self):
        """Move the player one cell down."""
        # if self.position[0] < 6:
        #     self.position[0] += 1  # Move down in the grid

    def move_left(self):
        """Move the player one cell to the left."""
        # if self.position[1] > 0:
        #     self.position[1] -= 1  # Move left in the grid

    def apply_gravity(self):
        """Apply gravity effect by moving the player down every second if no action is taken."""
        # self.gravity_counter += 1
        # if self.gravity_counter >= self.config.gravity_interval:
        #     self.gravity_counter = 0
        #     if self.position[0] < 6:
        #         self.position[0] += 1  # Move down one cell

    def draw(self):
        """Draw the player on the grid."""
        x, y = self.position
        self.config.screen.blit(self.image, (y * self.size, x * self.size))
        
    def collided(self, pipes, floor):
        """Check if the player has collided with any pipe or the floor."""
        # Check collision with floor (row 6 is the floor)
        if self.position[0] == 6:
            return True
        
        # Check collision with pipes
        if tuple(self.position) in pipes.get_pipe_positions():
            return True
        
        return False
