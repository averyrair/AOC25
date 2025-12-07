def main():
    board = {}
    start_pos = (0,0)
    num_lines = 0
    with open("input07.txt", "r") as f:
        line_num = 0
        for line in f:
            for c in range(len(line)):
                if line[c] == 'S':
                    start_pos = (line_num, c)
                board[(line_num, c)] = line[c] == '^'
            line_num += 1
        num_lines = line_num
    
    beam_cols = [start_pos[1]]
    total_splits = 0
    for line_num in range(num_lines-1):
        print(f"{beam_cols}, {total_splits}")
        new_beam_cols = []
        for beam_col in beam_cols:
            if not board[(line_num+1, beam_col)]:
                new_beam_cols.append(beam_col)
            else:
                split_occured = False
                if beam_col - 1 not in new_beam_cols:
                    new_beam_cols.append(beam_col - 1)
                    split_occured = True
                if beam_col + 1 not in new_beam_cols:
                    new_beam_cols.append(beam_col + 1)
                    split_occured = True
                if split_occured:
                    total_splits += 1
        beam_cols = new_beam_cols
        beam_cols.sort()
    print(total_splits)

                 






if __name__ == "__main__":
    main()