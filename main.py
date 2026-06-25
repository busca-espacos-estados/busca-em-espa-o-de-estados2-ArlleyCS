from puzzle.state import State
from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.a_star import AStar

def print_result(name: str, result):
    print(f"\n{'='*40}")
    print(f"Algoritmo : {name}")
    
    
    if result and hasattr(result, 'target') and result.target is not None:
        sol_actions = result.target.actions()
        print(f"Solução   : {' → '.join(sol_actions)}")
        print(f"Custo     : {result.target.cost}")
        print(f"Profund.  : {result.max_depth}")
    elif result and hasattr(result, 'found') and result.found:
        
        print("Solução   : ENCONTRADA")
    else:
        print("Solução   : NÃO ENCONTRADA")
        
    print(f"Expandidos: {result.nodes_expanded if result else 0}")
    print(f"Gerados   : {result.nodes_generated if result else 0}")
    print(f"Fronteira : {result.max_frontier_size if result else 0} (máx)")

if __name__ == "__main__":

    initial = State((1, 2, 3, 4, 5, 0, 7, 8, 6))

    print("Estado inicial:")
    print(initial)

    print_result("BFS",  BFS().search(initial))
    print_result("DFS",  DFS().search(initial))
    print_result("A*",   AStar().search(initial))