def main():
    nums = []
    output = 0
    with open("input06.txt", "r") as f:
        for line in f:
            line_nums = line.replace("\n", "")
            line_nums = line_nums.split(" ")
            line_nums = [item for item in line_nums if item != ""]
            nums.append(line_nums)
    for col in range(len(nums[0])):
        if nums[4][col] == '*':
            output += int(nums[0][col]) * int(nums[1][col]) * int(nums[2][col]) * int(nums[3][col]) 
        if nums[4][col] == '+':
            output += int(nums[0][col]) + int(nums[1][col]) + int(nums[2][col]) + int(nums[3][col]) 
    
    print(output)



if __name__ == "__main__":
    main()