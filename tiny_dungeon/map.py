

from dataclasses import dataclass
import pygame as pg
from typing import TYPE_CHECKING, Optional

from random import choice

if TYPE_CHECKING:
  from tiny_dungeon.game import Game


@dataclass
class Cell:
  walkable: bool
  sprite: Optional[str]


class Map:
  def __init__(self, game: "Game", size=(10, 10)):
    self.cells = [choice((Cell(sprite="floor", walkable=True), Cell(sprite="wall", walkable=False)))
                  for _ in range(size[0]*size[1])]
    self.game = game
    self.size = size

  def get(self, row, col):
    return self.cells[row*self.size[1] + col]

  def draw(self, center_x: int, center_y: int):
    for col in range(self.size[1]):
      for row in range(self.size[0]):
        cell = self.get(row, col)
        if cell.sprite:
          sprite = self.game.sprites.get(cell.sprite)
          self.game.draw_sprite_surface(sprite, row, col)
