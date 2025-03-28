import asyncio
from src.flappy2 import Flappy  # Adjust the import path as needed

def main():
    game = Flappy()
    asyncio.run(game.start())

if __name__ == "__main__":
    main()
