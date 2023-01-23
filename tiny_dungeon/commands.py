
from typing import Any

from dataclasses import dataclass


@dataclass
class Command:
  target: Any

  def execute(self):
    ...


class MoveCommand(Command):

  def __init__(self, target, dx, dy):
    super().__init__(target)
    self.dx = dx
    self.dy = dy

  def execute(self):
    self.target.move(self.dx, self.dy)
