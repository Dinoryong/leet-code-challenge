class Solution:
  def minReorder(self, n: int, connections: List[List[int]]) -> int:
    adj_out = collections.defaultdict(list)
    adj_in = collections.defaultdict(list)

    for st, fin in connections:
      adj_out[st] += [fin]
      adj_in[fin] += [st]

    S = [0] + adj_out[0] + adj_in[0]
    changed = len(adj_out[0])
    visited = set(S)

    while S:
      node = S.pop()

      for outn in adj_out[node]:
        if outn not in visited:
          visited.add(outn)
          changed += 1
          S.append(outn)

      for inn in adj_in[node]:
        if inn not in visited:
          visited.add(inn)
          S.append(inn)

    return changed