from .helpers.factories import generate_adjacency_list
from .helpers.immutable import (copy_path_and_add_vertex, copy_path_and_add_edge_path)
from .helpers.validators import validate_and_add_to_lists

# O(m) in the worst case scenario
# where m is the amount of edges
def search_cycle_with_size(vertex, adjacency_list, visited, all_cycles, all_edge_cycles, size, path = [], edge_path = set()):
  if (len(path) == size):
    return
  
  if (visited.get(vertex) is True):
    if len(path) + 1 == size and vertex is path[0]:
      validate_and_add_to_lists(vertex, path, edge_path, all_cycles, all_edge_cycles)
    return

  new_visited = visited.copy()
  new_visited[vertex] = True
  new_path = copy_path_and_add_vertex(vertex, path)
  new_edge_path = edge_path

  if len(new_path) > 1:
    new_edge_path = copy_path_and_add_edge_path(path[len(path)-1], vertex, edge_path)

  for child in adjacency_list[vertex]:
    search_cycle_with_size(child, adjacency_list, new_visited, all_cycles, all_edge_cycles, size, new_path, new_edge_path)

# O(n^2)
# First loop is executed n - 3 times (to look for cycles with sizes going from 4 to n)
# Second loop is executed n times
def find_cycles_by_permutation(graph):
  adjacency_list = generate_adjacency_list(graph)

  all_cycles = list()
  all_edge_cycles = list()

  for length in range(4, len(graph['vertices']) + 2):
    for vertex in graph['vertices']:
      visited = dict()
      search_cycle_with_size(vertex, adjacency_list, visited, all_cycles, all_edge_cycles, length)

  return all_cycles