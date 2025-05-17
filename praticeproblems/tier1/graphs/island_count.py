def getNumberOfIslands(binaryMatrix):
    if not binaryMatrix or not binaryMatrix[0]:
        return 0

    rows, cols = len(binaryMatrix), len(binaryMatrix[0])
    visited = set()

    def dfs(r, c):
        # Base case: out of bounds or water or already visited
        if (r < 0 or r >= rows or
            c < 0 or c >= cols or
            binaryMatrix[r][c] == 0 or
            (r, c) in visited):
            return

        visited.add((r, c))

        # Explore 4-directionally
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    island_count = 0

    for r in range(rows):
        for c in range(cols):
            if binaryMatrix[r][c] == 1 and (r, c) not in visited:
                dfs(r, c)
                island_count += 1

    return island_count

if __name__=="__main__":
    binaryMatrix = [
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1]]
    print(getNumberOfIslands(binaryMatrix))