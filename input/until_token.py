import fileinput


TOKEN = 'XYZ'

# Read input until we get to the token
inp = fileinput.input()
line = inp.readline().strip()
while line != TOKEN:
    # Process line
    print(line)

    line = inp.readline().strip()
