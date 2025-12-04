def main():
    with open("input03a.txt", "r") as f:
        output = 0
        for line in f:
            batteries = [int(c) for c in line.replace("\n", "")]
            next_start = 0
            best_for_line = ""
            for i in range(12):
                max_index = max(next_start, len(batteries) - (12 - i))            
                digit = max(batteries[next_start:max_index+1])
                d_i = batteries[next_start:max_index+1].index(digit) + next_start
                next_start = d_i + 1
                best_for_line = best_for_line + str(digit)
            b = int(best_for_line)
            output += b
        print(output)

if __name__ == "__main__":
    main()