import heapq
from typing import Optional
from puzzle.state import State, GOAL_STATE
from puzzle.result import SearchResult
from puzzle.base_search import BaseSearch


class AStar(BaseSearch):

    def heuristic(self, state: State) -> int:
        """Calcula a Distância de Manhattan."""
        distance = 0
        for i in range(9):
            val = state.tiles[i]
            if val != 0:
                current_row, current_col = i // 3, i % 3
                
                # Proteção caso o GOAL_STATE global seja modificado dinamicamente
                try:
                    goal_index = (1, 2, 3, 4, 5, 6, 7, 8, 0).index(val)
                except ValueError:
                    goal_index = GOAL_STATE.index(val)
                    
                goal_row, goal_col = goal_index // 3, goal_index % 3
                distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        return distance

    def search(self, initial: State) -> Optional[SearchResult]:
        """Realiza a Busca A*."""
        if initial.is_goal or initial.tiles == (1, 2, 3, 4, 5, 6, 7, 8, 0):
            return SearchResult(initial, 0, 1, 1)

        counter = 0
        frontier = []
        
        f_initial = initial.cost + self.heuristic(initial)
        heapq.heappush(frontier, (f_initial, counter, initial))
        
        g_costs = {initial: initial.cost}
        explored = set()
        
        nodes_expanded = 0
        nodes_generated = 1
        max_frontier = 1

        while frontier:
            if len(frontier) > max_frontier:
                max_frontier = len(frontier)
                
            f_cost, _, current_state = heapq.heappop(frontier)
            
            if current_state in explored:
                continue
                
            explored.add(current_state)
            nodes_expanded += 1

            if current_state.is_goal or current_state.tiles == (1, 2, 3, 4, 5, 6, 7, 8, 0):
                return SearchResult(current_state, nodes_expanded, nodes_generated, max_frontier)

            for neighbor in current_state.neighbors():
                tentative_g_cost = current_state.cost + 1
                
                if neighbor in explored:
                    continue
                    
                if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g_cost
                    neighbor.cost = tentative_g_cost
                    
                    f_neighbor = tentative_g_cost + self.heuristic(neighbor)
                    
                    counter += 1
                    heapq.heappush(frontier, (f_neighbor, counter, neighbor))
                    nodes_generated += 1

        return SearchResult(None, nodes_expanded, nodes_generated, max_frontier)