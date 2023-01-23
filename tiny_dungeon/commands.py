
from dataclasses import dataclass

from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
    from tiny_dungeon.game import Game


@dataclass
class Command:
    target: Any

    def execute(self):
        ...

    def validate(self, game: "Game") -> bool:
      return True

class MoveCommand(Command):

    def __init__(self, target, d_row, d_col):
        super().__init__(target)
        self.d_row = d_row
        self.d_col = d_col

    def execute(self):
      self.target.move(self.d_row, self.d_col)

    def _desired_position(self):
      return (self.target.row+self.d_row, self.target.col+self.d_col)

    def validate(self, game: "Game") -> bool:
      map = game.map
      desired_row,desired_col = self._desired_position()
      cell = map.get(desired_row,desired_col)
      return cell.walkable