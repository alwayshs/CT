def solution(n, roads, sources, destination):
    distance = [[] for _ in range(n + 1)]
    for a, b in roads:
        distance[a].append(b)
        distance[b].append(a)

    visited = [-1] * (n + 1)
    visited[destination] = 0

    current_node = [destination]
    
    while current_node:
        next_node = []

        for node in current_node:
            for near_node in distance[node]:
                if visited[near_node] == -1:
                    visited[near_node] = visited[node] + 1
                    next_node.append(near_node)
                
        current_node = next_node
    

    answer = []

    for i in sources:
        dist = visited[i]
        answer.append(dist)
        
    return answer