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
    
    beam_cols = {start_pos[1]: 1}
    for line_num in range(num_lines-1):
        new_beam_cols = {}
        for beam_col in beam_cols.keys():
            instances = beam_cols[beam_col]
            if not board[(line_num+1, beam_col)]:
                if beam_col not in new_beam_cols:
                    new_beam_cols[beam_col] = instances
                else:
                    new_beam_cols[beam_col] += instances
            else:
                if beam_col+1 not in new_beam_cols:
                    new_beam_cols[beam_col+1] = instances
                else:
                    new_beam_cols[beam_col+1] += instances
                if beam_col-1 not in new_beam_cols:
                    new_beam_cols[beam_col-1] = instances
                else:
                    new_beam_cols[beam_col-1] += instances
        beam_cols = new_beam_cols
    print(sum(beam_cols.values()))

                 






if __name__ == "__main__":
    main()