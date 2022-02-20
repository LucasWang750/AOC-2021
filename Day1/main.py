def part1():
    incr_count = 0
    file = open("c:\\dev\\Github\\AOC-2021\\Day1\\input.txt", "r")
    #first line
    last_num = int(file.readline())
    for line in file:
        curr_num = int(line)
        if curr_num > last_num:
            incr_count += 1
        last_num = curr_num
    print(incr_count)
    file.close()

def part2():
    incr_count = 0
    with open("c:\\dev\\Github\\AOC-2021\\Day1\\demo.txt", "r") as file:
        f = file.readlines()
        f = list(map(conv_to_int, f))
        for i in range(len(f)-3):
            if f[i+1] + f[i+2] + f[i+3] > f[i] + f[i+1] + f[i+2]:
                incr_count += 1
        print(incr_count)

def conv_to_int(line):
    return int(line.strip())

def main():
    part2()


if __name__ == "__main__":
    main()