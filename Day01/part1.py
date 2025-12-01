def main():
    with open("input01a.txt", "r") as f:
        # dial starts at 50
        dial = 50
        score = 0
        for line in f:
            mul = 1 if line[0] == 'R' else -1
            # set the new dial value, going up for R and down for L
            # mod at the end to account for loop arounds
            dial = (dial + mul * int(line[1:])) % 100
            # add to the score if the dial lands on 0
            if dial == 0:
                score += 1
        print(score)

if __name__ == "__main__":
    main()