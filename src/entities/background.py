from ..utils import GameConfig
from .entity import Entity

class Background(Entity):
    def __init__(self, config: GameConfig) -> None:
        super().__init__(
            config,
            config.images.background,  # Load the background image from config
            0,                         # X position
            0,                         # Y position
            config.window.width,       # Width of the background
            config.window.height       # Height of the background
        )

    def draw(self) -> None:
        """Draw the background image on the screen."""
        self.config.screen.blit(self.image, (self.x, self.y))
