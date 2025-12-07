def main():
    with open("input05.txt", "r") as f:
        ranges = []
        score = 0
        for line in f:
            l = line.replace("\n", "")
            dash_index = l.find('-')
            if dash_index != -1:
                ranges.append((int(l[:dash_index]), int(l[dash_index+1:])))
            elif len(l) != 0:
                id = int(l)
                for r in ranges:
                    if id >= r[0] and id <= r[1]:
                        score += 1
                        break
        print(score)

if __name__ == "__main__":
    main()