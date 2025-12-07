def main():
    with open("input05.txt", "r") as f:
        ranges = []
        score = 0
        for line in f:
            l = line.replace("\n", "")
            dash_index = l.find('-')
            if dash_index != -1:
                range_start = int(l[:dash_index])
                range_end = int(l[dash_index+1:])
                merged = False
                for r in ranges:
                    merged_range = merge_ranges(r, [range_start, range_end])
                    if merged_range is not None:
                        r[0] = merged_range[0]
                        r[1] = merged_range[1]
                        merged = True
                        break
                if merged == False:
                    ranges.append([range_start, range_end]) 
            else:
                break

        merged = True
        while merged == True:
            merged = False
            for r1 in ranges:
                for r2 in ranges:
                    if r1 != r2:
                        merged_range = merge_ranges(r1, r2)
                        if merged_range is not None:
                            r1[0] = merged_range[0]
                            r1[1] = merged_range[1]
                            ranges.remove(r2)
                            merged = True
                            break
                if merged == True:
                    break
        
        for r in ranges:
            score += r[1] - r[0] + 1
        print(score)

def merge_ranges(r1, r2):
    if r1[1] < r2[0] or r2[1] < r1[0]:
        return None
    return [min(r1[0], r2[0]), max(r1[1], r2[1])]

if __name__ == "__main__":
    main()