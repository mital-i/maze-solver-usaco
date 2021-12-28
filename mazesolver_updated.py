def dfs (graph, visited, r, c, path, row, col): 
    visited.append([r, c])
    if graph[r][c]=='F': 
        return path
    if [r+1, c] not in visited and graph[r+1][c]!='#' and in_bound(graph, row, col, r+1, c):
        path+='D'
        path = dfs(graph, visited, r+1, c, path, row, col)
    if [r-1, c] not in visited and graph[r-1][c]!='#' and in_bound(graph, row, col, r-1, c):
        path+='U'
        path = dfs(graph, visited, r-1, c, path, row, col)
    if [r, c+1] not in visited and graph[r][c+1]!='#' and in_bound(graph, row, col, r, c+1):
        path+='R'
        path = dfs(graph, visited, r, c+1, path, row, col)
    if [r, c-1] not in visited and graph[r][c-1]!='#' and in_bound(graph, row, col, r, c-1):
        path+='L'
        path = dfs(graph, visited, r, c-1, path, row, col)
    return path
    
def in_bound(graph, num_rows, num_cols, r, c): 
    if r >= num_rows or r < 0: 
        return False
    if c >= num_cols or c < 0: 
        return False 
        
    return True
    
def find_start(graph, row, col): 
    for i in range(row): 
        for j in range(col): 
            if graph[i][j] == 'S': 
                return [i, j]
                
graph = ['#######', 
        '#F....#', 
        '#.#.###', 
        '#....S#',
        '#######']

graph = ['#######', 
        '#F#...#', 
        '#.#.#.#', 
        '#...#S#',
        '#######']

path = ""

row, col = 5, 6
start_coords = find_start(graph, row, col)
print(start_coords)
visited = []
print(dfs(graph, visited, start_coords[0], start_coords[1], path, row, col))

print()






