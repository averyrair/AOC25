def main():
    with open("input03a.txt", "r") as f:
        output = 0
        for line in f:
            batteries = [int(c) for c in line.replace("\n", "")]
            first = max(batteries[:-1])
            f_i = batteries.index(first)
            second = max(batteries[f_i+1:])
            value = int(str(first) + str(second))
            output += value
        print(output)

if __name__ == "__main__":
    main()