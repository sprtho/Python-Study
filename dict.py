from collections import defaultdict

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"], ["ICN", "AAA"]]

graph = defaultdict(list)

route = dict()

for start, end in tickets:
    graph[start].append(end)

for start, end in tickets:
    if start in route:
        route[start].append(end)
    else:
        route[start] = [end]

for r in route.keys():
    route[r].sort(reverse = True)        

route["HND"].pop()

print(route)



print(graph)