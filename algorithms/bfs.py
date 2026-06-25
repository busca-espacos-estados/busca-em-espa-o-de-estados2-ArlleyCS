from collections import deque
from typing import Optional
from puzzle.state import State, GOAL_STATE
from puzzle.result import SearchResult
from puzzle.base_search import BaseSearch


class BFS(BaseSearch):

    def search(self, initial: State) -> Optional[SearchResult]:
        """Realiza a Busca em Largura (BFS)."""
        # Força a verificação imediata por valor de tupla ou propriedade
        if initial.is_goal or initial.tiles == (1, 2, 3, 4, 5, 6, 7, 8, 0):
            return SearchResult(initial, 0, 1, 1)

        frontier = deque([initial])
        frontier_set = {initial}
        explored = set()
        
        nodes_expanded = 0
        nodes_generated = 1
        max_frontier = 1

        while frontier:
            current_state = frontier.popleft()
            frontier_set.remove(current_state)
            
            explored.add(current_state)
            nodes_expanded += 1

            if current_state.is_goal or current_state.tiles == (1, 2, 3, 4, 5, 6, 7, 8, 0):
                return SearchResult(current_state, nodes_expanded, nodes_generated, max_frontier)

            for neighbor in current_state.neighbors():
                if neighbor not in explored and neighbor not in frontier_set:
                    nodes_generated += 1
                    
                    # Verificação no momento da geração para o BFS andar mais rápido
                    if neighbor.is_goal or neighbor.tiles == (1, 2, 3, 4, 5, 6, 7, 8, 0):
                        return SearchResult(
                            neighbor, 
                            nodes_expanded, 
                            nodes_generated, 
                            max(max_frontier, len(frontier) + 1)
                        )
                        
                    frontier.append(neighbor)
                    frontier_set.add(neighbor)
                    
            if len(frontier) > max_frontier:
                max_frontier = len(frontier)

        return SearchResult(None, nodes_expanded, nodes_generated, max_frontier)