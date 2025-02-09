import pygame

class Floor:
    def __init__(self, config):
        """Initialize the floor cells on the grid."""
        self.config = config
        self.size = 50  # Size of each grid cell
        self.floor_cells = [(6, i) for i in range(7) ]
        
        self.image = pygame.image.load('/Users/apoorvagayatrik/Desktop/FlapPyBird-master/imgs/base.png')
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
  # Row 7, all columns except column 4

    def draw(self):
        """Draw the floor cells on the grid."""
        for (x, y) in self.floor_cells:
                self.config.screen.blit(self.image, (y * self.size, x * self.size))  # Draw pipes with the image

    def tick(self):
        """Update the floor state (if needed)."""
        # For now, this is a placeholder
        pass
