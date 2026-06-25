from typing import Optional
from puzzle.state import State, GOAL_STATE
from puzzle.result import SearchResult
from puzzle.base_search import BaseSearch


class DFS(BaseSearch):

    def search(self, initial: State) -> Optional[SearchResult]:
        """Realiza a Busca em Profundidade (DFS)."""
        if initial.is_goal or initial.tiles == (1, 2, 3, 4, 5, 6, 7, 8, 0):
            return SearchResult(initial, 0, 1, 1)

        frontier = [initial]
        frontier_set = {initial}
        explored = set()
        
        nodes_expanded = 0
        nodes_generated = 1
        max_frontier = 1

        while frontier:
            current_state = frontier.pop()
            frontier_set.remove(current_state)
            
            if current_state in explored:
                continue
                
            explored.add(current_state)
            nodes_expanded += 1

            if current_state.is_goal or current_state.tiles == (1, 2, 3, 4, 5, 6, 7, 8, 0):
                return SearchResult(current_state, nodes_expanded, nodes_generated, max_frontier)

            for neighbor in reversed(current_state.neighbors()):
                if neighbor not in explored and neighbor not in frontier_set:
                    frontier.append(neighbor)
                    frontier_set.add(neighbor)
                    nodes_generated += 1
                    
            if len(frontier) > max_frontier:
                max_frontier = len(frontier)

        return SearchResult(None, nodes_expanded, nodes_generated, max_frontier)