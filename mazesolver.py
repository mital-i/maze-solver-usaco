row, col = 5, 7

graph = ['#######', 
        '#F..#...#', 
        '#.#.....#', 
        '#......S#',
        '#######']   
        
def dfs(r, c, graph, visited, stack, path):
    visited.append([r, c])
    stack.append([r, c])
    while(graph[r][c]!='F'): 
        #print(r, c)
        #print(path)
        if [r+1, c] not in visited and graph[r+1][c]!='#':
            path[0]+='D'
            stack.append([r+1, c])
        if [r-1, c] not in visited and graph[r-1][c]!='#':
            path[0]+='U'
            stack.append([r-1, c])
        if [r, c+1] not in visited and graph[r][c+1]!='#':
            path[0]+='R'
            stack.append([r, c+1])
        if [r, c-1] not in visited and graph[r][c-1]!='#':
            path[0]+='L'
            stack.append([r, c-1])
        r, c = stack.pop(-1)
        visited.append([r, c])
    
    return path
path = ['']
visited = []
stack = []

#find the coordinates for the starting point
def find_start(graph, row, col): 
    for i in range(row): 
        for j in range(col): 
            if graph[i][j] == 'S': 
                return [i, j]

start_coord = find_start(graph, row, col)

#start the dfs from the starting point
dfs(start_coord[0], start_coord[1], graph, visited, stack, path)
print(path[0])
