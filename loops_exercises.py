print("Q1")
numbers_list = []
numbers = input("Enter a number: ")
while numbers != "":
    numbers_list.append(int(numbers))
    numbers = input("Enter another number, or press enter: ")
else:
    total = sum(numbers_list)
    print(total)

print()

print("Q2")
mailing_list = [
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Biscuit", "biscuit@whippies.park"],
    ["Rory", "rory@whippies.park"]
]

for details in mailing_list:
    print(f"{details[0]}: {details[1]}")

print()

print("Q3")
names_list = []
count = 0

while count < 3:
    name = input("Enter a friend's name: ")
    names_list.append(name)
    count += 1
else:
    for friend in names_list:
        print(friend)

print()

print("Q4")
groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

total_cost = 0

for items in groceries:
    quantity = input(f"How many {items[0]} did you buy? ")
    items[1] *= int(quantity)
    total_cost += float(items[1])
print()

total_cost = f"${total_cost:.2f}"
# print(total_cost)

print()

print("====Izzy's Food Emporium====")
for items in groceries:
    print(f"{items[0]:<17} ${items[1]:.2f}")
print("============================")
print(f"{total_cost:>24}")
print()