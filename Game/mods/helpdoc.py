


with open("help.txt", 'r') as f:
    file = f.read()
print(file)
running_total = 0
for line in file:
    if line.isnumeric():
        running_total += int(line)
print(running_total)