
# read input file
with open('.\Day 1\day1 Input.txt') as file:
    lines = file.readlines()
    file.close()

elfs_items = {}

calories_sum = 0
elf_count = 0

for line in lines:
    if line != "\n":
        calories_sum += int(line)
    else:
        elf_count += 1
        elfs_items[f"elf {elf_count}"] = calories_sum
        calories_sum = 0

max_calories = max(elfs_items.values())
max_elf = max(elfs_items, key=elfs_items.get)

print(elfs_items)

print (f"The elf with the most calories is {max_elf}, with {max_calories} calories")

top_3_calories = 0

for i in range(0,3):
    top_3_calories += elfs_items.pop(max(elfs_items, key=elfs_items.get))

print(top_3_calories)