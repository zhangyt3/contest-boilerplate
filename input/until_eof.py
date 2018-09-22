import fileinput


# Read until the file is done
for line in fileinput.input():
    # Process line
    print(line)
