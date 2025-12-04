def main():
    input_data = ""
    with open("input02a.txt", "r") as f:
        input_data = f.read()
    
    output = 0
    input_data = input_data.replace("-", ",")
    r = input_data.split(",")
    ranges = [int(n) for n in r]
    for i in range(0, len(ranges), 2):
        for j in range(ranges[i], ranges[i+1] + 1):
            if isFake(j):
                output += j

    print(output)

def isFake(num):
    num_str = str(num)
    num_digits = len(num_str)
    for i in range(1, num_digits):
        base = num_str[:i]
        is_fake = True
        for j in range(0, num_digits, i):
            if num_str[j:j+i] != base:
                is_fake = False
                break
        if is_fake:
            return True
                

if __name__ == "__main__":
    main()
