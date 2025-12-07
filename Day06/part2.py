def main():
    inp = {}
    output = 0
    with open("input06.txt", "r") as f:
        i = 0
        for line in f:
            for j in range(len(line.replace("\n", ""))):
                if not j in inp:
                    inp[j] = {}
                inp[j][i] = line[j]
            i += 1
    
    blank_line_indices = [i for i in inp.keys() if all(val == ' ' for val in inp[i].values())]
    blank_line_indices.append(max(inp.keys()) + 1)

    # each blank line marks the end of an equation
    start_point = 0
    for end_point in blank_line_indices:
        operation = inp[start_point][max(inp[start_point].keys())]
        score = 0 if operation == '+' else 1
        for c in range(start_point,end_point):
            col = inp[c]
            col.pop(max(inp[c].keys()))

            num = 0
            for i in range(max(col.keys())+1):
                if col[i] == ' ':
                    continue
                num *= 10
                num += int(col[i])
            if operation == '+':
                score += num
            else:
                score *= num
        output += score
        start_point = end_point + 1
    print(output)

if __name__ == "__main__":
    main()