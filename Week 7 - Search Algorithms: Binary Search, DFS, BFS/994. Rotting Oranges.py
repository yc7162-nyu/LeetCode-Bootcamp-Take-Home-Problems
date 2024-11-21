class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        fresh = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        minutes = 0
        while q and fresh > 0:
            # q contains coordinates of all rotten oranges
            # in current minute
            qlen = len(q)

            nd = [[-1, 0], [0, 1], [1, 0], [0, -1]]

            # For every rotten orange
            # add all the oranges it affects to the queue
            for i in range(qlen):
                node = q.popleft()

                r, c = node

                # Infect other oranges
                for nr, nc in nd:
                    # Check valid coordinates
                    if min(r + nr, c + nc) < 0 or (r + nr) >= ROWS or (c + nc) >= COLS:
                        continue

                    if grid[r + nr][c + nc] == 1:
                        grid[r + nr][c + nc] = 2
                        q.append((r + nr, c + nc))
                        fresh -= 1
            
            minutes += 1                   
        
        # There may still be non rotten oranges (e.g. if fresh oranges was isolated)
        if fresh:
            return -1
        
        return minutes

    # Time Complexity: O(nm)
    # Space Complexity: O(nm)