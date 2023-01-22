

from tiny_dungeon.game import Game
import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

if __name__ == '__main__':
  app = Game()
  app.run()
