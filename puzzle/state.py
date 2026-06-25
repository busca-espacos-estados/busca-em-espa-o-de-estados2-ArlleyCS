from __future__ import annotations
from typing import List, Optional, Tuple

GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

class State:
    """Representa um estado do 8-puzzle como tupla imutável de 9 inteiros (0 = espaço vazio)."""

    def __init__(self, tiles: Tuple[int, ...], parent: Optional["State"] = None, action: Optional[str] = None, cost: int = 0):
        if len(tiles) != 9 or set(tiles) != set(range(9)):
            raise ValueError("Estado inválido: deve conter exatamente os valores 0-8.")
        self.tiles = tuple(int(x) for x in tiles)  # Garante puramente inteiros
        self.parent = parent
        self.action = action
        self.cost = cost

    @property
    def is_goal(self) -> bool:
        return self.tiles == GOAL_STATE

    @property
    def blank_index(self) -> int:
        return self.tiles.index(0)

    def neighbors(self) -> List["State"]:
        """Retorna os estados filhos válidos a partir deste estado."""
        states = []
        idx = self.blank_index
        row, col = idx // 3, idx % 3

       
        moves = [
            (row - 1, col, 'Up'),
            (row + 1, col, 'Down'),
            (row, col - 1, 'Left'),
            (row, col + 1, 'Right')
        ]

        for r, c, action in moves:
            if 0 <= r < 3 and 0 <= c < 3:
                new_idx = r * 3 + c
                
                new_tiles = list(self.tiles)
                # Troca o 0 com a peça vizinha
                new_tiles[idx], new_tiles[new_idx] = new_tiles[new_idx], new_tiles[idx]
                
                child_state = State(
                    tiles=tuple(new_tiles),
                    parent=self,
                    action=action,
                    cost=self.cost + 1
                )
                states.append(child_state)
                
        return states

    def path(self) -> List["State"]:
        """Retorna a sequência de estados do estado inicial até este."""
        current = self
        sequence = []
        while current is not None:
            sequence.append(current)
            current = current.parent
        return list(reversed(sequence))

    def actions(self) -> List[str]:
        """Retorna a sequência de ações do estado inicial até este."""
        return [state.action for state in self.path() if state.action is not None]

    def __eq__(self, other: object) -> bool:
        return isinstance(other, State) and self.tiles == other.tiles

    def __hash__(self) -> int:
        return hash(self.tiles)

    def __lt__(self, other: "State") -> bool:
        return self.cost < other.cost

    def __repr__(self) -> str:
        t = self.tiles
        return (
            f"+-------+\n"
            f"| {t[0]} {t[1]} {t[2]} |\n"
            f"| {t[3]} {t[4]} {t[5]} |\n"
            f"| {t[6]} {t[7]} {t[8]} |\n"
            f"+-------+"
        ).replace("0", " ")