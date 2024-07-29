# Problem: A - Forever Winter - https://codeforces.com/gym/532332/problem/A

def solve(n, m, edges):
    adj = [[] for _ in range(n + 1)]

    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    one_of_good_node = -1
    x = 0
    y = 0

    for i in range(1, n + 1):
        if len(adj[i]) == 1:
            one_of_good_node = adj[i][0]
            y = len(adj[adj[i][0]])

    for adj_node in adj[one_of_good_node]:
        k = len(adj[adj_node])
        x = max(x, k)

    print(x, y - 1)

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0]) 
    index = 1
    
    for _ in range(T):
        n, m = map(int, data[index].split())
        edges = []
        for j in range(1, m + 1):
            a, b = map(int, data[index + j].split())
            edges.append((a, b))
        solve(n, m, edges)
        index += m + 1

if __name__ == "__main__":
    main()
