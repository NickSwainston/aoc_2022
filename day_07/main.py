import os

current_dir = ""
dir_sizes = {"/": 0}
with open('input.txt') as data_file:
    for line in data_file:
        line = line[:-1]
        if line.startswith("$ cd"):
            new_dir = line.split("$ cd ")[-1]
            current_dir = os.path.normpath(os.path.join(current_dir, new_dir))
        elif line.startswith("$ ls"):
            continue
        else:
            if line.startswith("dir"):
                new_dir = line.split("dir ")[-1]
                dir_sizes[os.path.join(current_dir, new_dir)] = 0
            else:
                dir_sizes[current_dir] += int(line.split()[0])

# find deepest dir num
most = []
for dir_key in dir_sizes.keys():
    most.append(dir_key.count("/"))

# loop over the deepest dirs then move backwards
for depth in range(max(most)-1, 0, -1):
    print(depth)
    for dir_key in dir_sizes.keys():
        if dir_key.count("/") == depth and dir_key != "/":
            print(dir_key)
            # Write depth so find all that are one deeper
            for deeper_key in dir_sizes.keys():
                if deeper_key.count("/") == depth + 1 and dir_key in deeper_key:
                    print(deeper_key)
                    # Update the size
                    dir_sizes[dir_key] += dir_sizes[deeper_key]
# do one more loop for outermost
for dir_key in dir_sizes.keys():
    if dir_key.count("/") == 1 and dir_key != "/":
        # Update the size
        dir_sizes["/"] += dir_sizes[dir_key]
print(dir_sizes)

part1_sum = 0
for dir_key in dir_sizes.keys():
    if dir_sizes[dir_key] < 100000:
        part1_sum += dir_sizes[dir_key]
print(f"Part 1: {part1_sum}")

size_needed = 30000000 - (70000000 - dir_sizes["/"])
sorted_dir_sizes = sorted(dir_sizes.items(), key=lambda x:x[1])
print(sorted_dir_sizes)
print(size_needed)
for dir_name, size in sorted_dir_sizes:
    if size > size_needed:
        print(f"Part 2: {size}")
        break