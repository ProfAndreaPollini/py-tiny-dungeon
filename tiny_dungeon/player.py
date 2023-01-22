import pygame as pg
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from tiny_dungeon.game import Game


class Player:

  def __init__(self, game: "Game"):
    self.sprites = game.sprites
    self.game = game
    self.sprite = self.sprites.get("player")
    self.pos = [5, 5]

  @property
  def row(self):
    return self.pos[0]

  @property
  def col(self):
    return self.pos[1]

  def draw(self):
    self.game.draw_sprite_surface(self.sprite, self.row, self.col)

  def move(self, d_row, d_col):
    self.pos[0] += d_row
    self.pos[1] += d_col
