import os
import logging

import pygame as pg

# assets\kenney_tinydungeon\Tilemap\tilemap_packed.png


class Spritesheet:
  SPRITES_CONFIG = [
      ('floor', (0, 0)),
      ("wall", (1, 2)),
      ("player", (8, 4))
  ]
  BASE_SPRITE_SIZE = 16
  SPRITE_COUNT = (11, 12)

  def __init__(self):
    self.surface = pg.image.load(os.path.join(
        'assets', "kenney_tinydungeon", "Tilemap", "tilemap_packed.png")).convert_alpha()
    # self.surface = pg.transform.scale2x(self.surface)
    # self.surface = pg.transform.scale2x(self.surface)
    self.sprite_size = Spritesheet.BASE_SPRITE_SIZE

  def setup(self, scale=3):
    # tile_size = screen_size//tiles
    # scale = tile_size // Spritesheet.BASE_SPRITE_SIZE

    self.sprite_size = scale * self.BASE_SPRITE_SIZE
    s = self.surface.get_size()
    self.surface = pg.transform.scale(self.surface, (s[0]*scale, s[1]*scale))
    self.sprites = {}
    for sprite_config in self.SPRITES_CONFIG:
      rect = pg.Rect(sprite_config[1][1] * self.sprite_size, sprite_config[1][0]
                     * self.sprite_size, self.sprite_size, self.sprite_size)
      logging.info(
          f"""Creating sprite "{sprite_config[0]}"  at {rect} [{self.surface.get_size()}]""")

      self.sprites[sprite_config[0]] = self.surface.subsurface(rect)
      pg.image.save(self.sprites[sprite_config[0]], f"{sprite_config[0]}.png")
    logging.info(f"Loaded {len(self.sprites)} sprites.")

  def get(self, sprite_name):
    return self.sprites[sprite_name]
