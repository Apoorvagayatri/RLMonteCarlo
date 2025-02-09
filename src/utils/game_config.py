import os
import pygame
from .images import Images
from .sounds import Sounds
from .window import Window

class GameConfig:
    def __init__(
        self,
        screen: pygame.Surface,
        clock: pygame.time.Clock,
        fps: int,
        window: Window,
        images: Images,
        sounds: Sounds,
        gravity_interval: int = 1  # Set a default value
    ) -> None:
        self.screen = screen
        self.clock = clock
        self.fps = fps
        self.window = window
        self.images = images
        self.sounds = sounds
        self.debug = os.environ.get("DEBUG", False)
        self.gravity_interval = gravity_interval  # Add this line

    def tick(self) -> None:
        self.clock.tick(self.fps)
