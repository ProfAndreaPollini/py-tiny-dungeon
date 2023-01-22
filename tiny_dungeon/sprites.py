import os
import pygame as pg

# assets\kenney_tinydungeon\Tilemap\tilemap_packed.png


class Spritesheet:
  SPRITES_CONFIG = [
      ('floor', (0, 0)),
      ("wall", (1, 2)),
      ("player", (8, 4))
  ]
  SPRITE_SIZE = 32

  def __init__(self):
    self.surface = pg.image.load(os.path.join(
        'assets', "kenney_tinydungeon", "Tilemap", "tilemap_packed.png")).convert_alpha()
    self.surface = pg.transform.scale2x(self.surface)
    # self.surface = pg.transform.scale2x(self.surface)
    self.sprites = {}
    for sprite_config in self.SPRITES_CONFIG:
      rect = pg.Rect(sprite_config[1][1] * Spritesheet.SPRITE_SIZE, sprite_config[1][0]
                     * Spritesheet.SPRITE_SIZE, Spritesheet.SPRITE_SIZE, Spritesheet.SPRITE_SIZE)
      self.sprites[sprite_config[0]] = self.surface.subsurface(rect)

  def get(self, sprite_name):
    return self.sprites[sprite_name]
