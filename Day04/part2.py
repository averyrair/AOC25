def main():
    with open("input04.txt", "r") as f:
        grid = []
        output = 0
        for line in f:
            grid.append([c == '@' for c in line.replace('\n', '')])
        grid.insert(0, [False for _ in range(len(grid[0]))])
        grid.append([False for _ in range(len(grid[0]))])        
        for row in grid:
            row.insert(0, False)
            row.append(False)
        while True:
            total_removed = 0
            for r in range(1, len(grid) - 1):
                for c in range(1, len(grid[0]) - 1):
                    if not grid[r][c]:
                        continue
                    filled_cells = 0
                    filled_cells += grid[r-1][c-1:c+2].count(True)
                    filled_cells += grid[r+1][c-1:c+2].count(True)
                    if grid[r][c-1]:
                        filled_cells += 1
                    if grid[r][c+1]:
                        filled_cells += 1
                    if filled_cells < 4:
                        total_removed += 1
                        grid[r][c] = False
            if total_removed == 0:
                break
            output += total_removed
        print(output)

                    


if __name__ == "__main__":
    main()