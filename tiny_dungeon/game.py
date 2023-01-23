import pygame as pg


import logging
from tiny_dungeon.map import Map
from tiny_dungeon.player import Player

from tiny_dungeon.sprites import Spritesheet

logger = logging.getLogger(__name__)


class Game:
  SCREEN_SIZE = (1900, 800)
  FPS = 60

  def __init__(self) -> None:
    pg.init()
    self.screen = pg.display.set_mode(Game.SCREEN_SIZE)
    self.clock = pg.time.Clock()
    self.current_fps = Game.FPS
    self.running = True
    self.sprites = Spritesheet()

    logging.info("Game started")

  def setup(self):
    self.sprites.setup(scale=3)
    self.player = Player(self)
    self.map = Map(self, (10, 10))

  def update(self) -> None:
    ...

  def draw(self) -> None:
    self.screen.blit(self.sprites.surface, (0, 0))
    self.draw_sprite("wall", 10, 10)
    self.map.draw(0, 0)
    self.player.draw()
    # logging.info(f"player pos = {self.player.row}, {self.player.col}")

  def draw_sprite(self, sprite_name, row, col):
    """Draw a sprite at the given row and column"""
    self.screen.blit(self.sprites.get(
        sprite_name), (col*self.sprites.sprite_size, row*self.sprites.sprite_size))

  def draw_sprite_surface(self, sprite_surface, row, col):
    """Draw a sprite at the given row and column"""
    self.screen.blit(
        sprite_surface, (col*self.sprites.sprite_size, row*self.sprites.sprite_size))

  def handle_input(self, event):
    
    # keys = pg.key.get_pressed()
    d = [0, 0]

    if event.key == pg.K_d:  # keys[pg.K_d]:
      d[1] = 1
    if event.key == pg.K_a:  # keys[pg.K_a]:
      d[1] = -1
    if event.key == pg.K_w:  # keys[pg.K_w]:
      d[0] = -1
    if event.key == pg.K_s:  # keys[pg.K_s]:
      d[0] = 1
    if d != [0, 0]:
      self.player.move(*d)


  def run(self):
    self.setup()
    while self.running:
      for event in pg.event.get():
        if event.type == pg.QUIT:
            self.running = False

        if event.type == pg.KEYDOWN:
          self.handle_input(event)
      self.screen.fill((50, 50, 50))

      self.update()
      self.draw()
      pg.display.update()
      self.clock.tick(Game.FPS)
      self.current_fps = self.clock.get_fps()
      pg.display.set_caption(f"[{self.current_fps:.2f}]Game")
    logging.info("Game end")
    pg.quit()
