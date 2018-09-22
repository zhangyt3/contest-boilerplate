import fileinput


# First line is some integer n
inp = fileinput.input()  # If no file is specified, reads from standard input
n = int(inp.readline())

# Read the next n lines of input
for i in range(n):
    line = inp.readline().strip()

    # Process line
    print(line)
