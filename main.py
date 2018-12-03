from sys import stdin

# P1.1
#
# line = stdin.readline()
# running_sum = 0
#
# while line:
#     running_sum += int(line)
#     line = stdin.readline()
#
# print running_sum

# p1.2

# running_sum = 0
# running_sum_set = set()
# first_repeated_sum = None
# lines = [int(line.strip()) for line in stdin.readlines()]
#
# while not first_repeated_sum:
#     for line in lines:
#         running_sum += line
#         # print running_sum
#         if running_sum in running_sum_set and not first_repeated_sum:
#             first_repeated_sum = running_sum
#             break
#         else:
#             running_sum_set.add(running_sum)
#
# print first_repeated_sum

# p2.1

# lines = [line.strip() for line in stdin.readlines()]
# total_count2 = 0
# total_count3 = 0
#
# for line in lines:
#     this_count = {}
#     for char in line:
#         this_count[char] = this_count.get(char, 0) + 1
#
#     already_counted2 = False
#     already_counted3 = False
#     for char, count in this_count.items():
#         if count == 2 and not already_counted2:
#             total_count2 += 1
#             already_counted2 = True
#         elif count == 3  and not already_counted3:
#             total_count3 += 1
#             already_counted3 = True
#
#
# print total_count2 * total_count3

# p2.2

# lines = [line.strip() for line in stdin.readlines()]
#
# for i, line1 in enumerate(lines):
#     for j, line2 in enumerate(lines):
#         if i == j:
#             continue
#         elif len(line1) == len(line2):
#             found_differences = 0
#             for char_index in range(len(line1)):
#                 if line1[char_index] != line2[char_index]:
#                     found_differences += 1
#             if found_differences == 1:
#                 print line1, line2

# p2.2 Code Golf

# lines = [line.strip() for line in stdin.readlines()]
# for i, line1 in enumerate(lines):
#     for line2 in lines[i:]:
#         if len([1 for char_index in range(len(line1)) if line1[char_index] != line2[char_index]]) == 1:
#             print line1, line2
#

# lines = [line.strip() for line in stdin.readlines()]
# print [[(line1, line2) for line2 in lines[i:] if len([1 for char_index in range(len(line1)) if line1[char_index] != line2[char_index]]) == 1] for i, line1 in enumerate(lines)]

# print [i for i in iter(raw_input, '')]
# print([(a, b) for a, b in zip(*[(line.strip(), line.strip()) for line in stdin.readlines()][::-1]) if sum(0 if a[i]==b[i] else 1 for i in range(0, len(a))) == 1][0])


# p3.1

# lines = [line.strip() for line in stdin.readlines()]
#
# playboard = {}
#
# for line in lines:
#     id, at, coord, size = line.split(" ")
#     x, y = coord.split(",")
#     y = y[:-1]
#     x, y = int(x), int(y)
#     height, width = size.split("x")
#     for i in range(int(height)):
#         for j in range(int(width)):
#             tup = (x+i, y+j)
#             playboard[tup] = playboard.get(tup, 0) + 1
#
#
# total_count = 0
# for tup, count in playboard.items():
#     if count > 1:
#         total_count += 1
#
# print total_count
#

# p3.2


lines = [line.strip() for line in stdin.readlines()]

playboard = {}

for line in lines:
    id, at, coord, size = line.split(" ")
    x, y = coord.split(",")
    y = y[:-1]
    x, y = int(x), int(y)
    height, width = size.split("x")
    for i in range(int(height)):
        for j in range(int(width)):
            tup = (x+i, y+j)
            playboard[tup] = playboard.get(tup, 0) + 1

for line in lines:
    id, at, coord, size = line.split(" ")
    x, y = coord.split(",")
    y = y[:-1]
    x, y = int(x), int(y)
    height, width = size.split("x")
    does_it_pass = True
    for i in range(int(height)):
        for j in range(int(width)):
            tup = (x+i, y+j)
            if playboard[tup] != 1:
                does_it_pass = False
    if does_it_pass:
        print id

#
# total_count = 0
# for tup, count in playboard.items():
#     if count > 1:
#         total_count += 1
#
# print total_count