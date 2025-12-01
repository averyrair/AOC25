def main():
    with open("input01a.txt", "r") as f:
        # dial starts at 50 still
        dial = 50
        score = 0
        for line in f:
            mul = 1 if line[0] == 'R' else -1
            # need to keep track of the previous position to catch the case where the dial was already on 0 and then went left
            prev_dial = dial
            # don't mod it this time. we need the information about how many times it looped
            dial = (dial + mul * int(line[1:]))
            loops = abs(dial // 100)
            # accounts for the fact that abs(-100n // 100) == n, but really there were n+1 crossings of 0
            if dial % 100 == 0 and dial <= 0:
                loops += 1
            # accounts for the fact that starting on 0 and going left double counts the initial 0
            if prev_dial == 0 and dial < 0:
                loops -= 1
            score += loops
            dial = dial % 100

        print(score)

if __name__ == "__main__":
    main()