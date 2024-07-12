# 1

a = input().split()
lst = [int(num) for num in a]

def inversions(lst):
    len_lst = len(lst)
    inv_count = 0
    for i in range(len_lst):
        for j in range(i+1, len_lst):
            if lst[i] > lst[j]:
                inv_count += 1
    return inv_count

print(inversions(lst))

# 3

n = int(input())
def hanoi(n):
    if n == 1:
        return 1
    else:
        return 2 * hanoi(n-1) + 1

print(hanoi(n))

# 2

matrix = [
    [1, 2, 3],
    [4, -1, 6],
    [7, 8, 9]
]

start = (0, 0)
end = (2, 2)

def min_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    heap = [(0, start)]
    visited = set()
    costs = {start: 0}

    while heap:
        cost, current = min(heap, key=lambda x: x[0])
        heap.remove((cost, current))

        if current == end:
            return cost

        if current in visited:
            continue

        visited.add(current)

        for dx, dy in directions:
            x, y = current[0] + dx, current[1] + dy

            if 0 <= x < rows and 0 <= y < cols and matrix[x][y] >= 0:
                new_cost = cost + matrix[x][y]
                if (x, y) not in costs or new_cost < costs[(x, y)]:
                    costs[(x, y)] = new_cost
                    heap.append((new_cost, (x, y)))

    return "точка не достигнута"

print(min_path(matrix, start, end))