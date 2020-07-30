print("Q1")
print()

names = []

with open("names.txt") as txt_file:
    for line in txt_file:
        line = line.strip()
        names.append(line)

for index, name in enumerate(names):
    print(f"{index+1}.  {name}")

print()

print("Q2.1")
print()

import csv

colours = []

with open("exercise_data/colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours.append(line)

for codes in colours:
    print(f"{codes[1].strip():<18} {codes[2].strip():<18} {codes[4].strip()}")

print()

print("Q2.2")
print()

colours = []

with open("exercise_data/colours_213.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours.append(line)

for codes in colours:
    print(f"{codes[1].strip():<18} {codes[2].strip():<18} {codes[4].strip()}")

print()
print("Q3.1")
print()

colours = []

with open("exercise_data/colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours.append(line)

Red = 0
Green = 0
Blue = 0

for english_name in colours:
    if "red" in english_name[4]:
        Red += 1
    
    if "green" in english_name[4]:
        Green +=1

    if "blue" in english_name[4]:
        Blue += 1
    # print(english_name[4])

print(f"Red: {Red}")
print(f"Green: {Green}")
print(f"Blue: {Blue}")

print()

print("Q3.2")
print()

colours = []

with open("exercise_data/colours_213.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours.append(line)

Red = 0
Green = 0
Blue = 0

for english_name in colours:
    if "red" in english_name[4]:
        Red += 1
    
    if "green" in english_name[4]:
        Green +=1

    if "blue" in english_name[4]:
        Blue += 1
    # print(english_name[4])

print(f"Red: {Red}")
print(f"Green: {Green}")
print(f"Blue: {Blue}")


