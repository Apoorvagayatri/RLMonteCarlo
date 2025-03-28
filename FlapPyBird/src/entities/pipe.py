import pygame
class Pipes:
    def __init__(self, config):
        """Initialize pipes on the grid."""
        self.config = config
        self.size = 50  # Size of each grid cell
        self.pipes = [
            # Define pipes as (row, col) positions
            [(0,2), (1,2), (3,2), (4,2), (5,2), (6,2)],  # Row 3, columns 1-4 and 6-7
            [(0,4), (1,4), (4,4), (5,4), (6,4)],        # Row 5, columns 1-2 and 5-7
            [(0,6), (1,6), (2,6), (4,6), (5,6), (6,6)]   # Row 7, columns 1-3 and 5-7
        ]
        self.image = pygame.image.load('/Users/apoorvagayatrik/Desktop/FlapPyBird-master/imgs/pipe.png')
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

    def draw(self):
        """Draw pipes on the grid."""
        for pipe_row in self.pipes:
            for (x, y) in pipe_row:
                self.config.screen.blit(self.image, (y * self.size, x * self.size))  # Draw pipes with the image


    def get_pipe_positions(self):
        """Return a list of all pipe positions."""
        return [pos for row in self.pipes for pos in row]
    
    def tick(self):
        pass
