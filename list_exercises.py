print("Q1")
foods = [
    "orange",
    "apple",
    "banana",
    "strawberry",
    "grape",
    "blueberry",
    ["carrot", "cauliflower", "pumpkin"],
    "passionfruit",
    "mango",
    "kiwifruit"
]
print(foods)
print("1. The first item in the list.")
print(foods[0])
print()
print("2. The third item in the list.")
print(foods[2])
print()
print("3. The last item in the list.")
print(foods[-1])
print()
print("4. The first three items in the list.")
print(foods[0:3])
print()
print("5. The last three items in the list.")
print(foods[-3:])
print()
print("6. The last item in the sublist.")
print(foods[6][-1])
print()
print("Q2")
mailing_list = [
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Biscuit", "biscuit@whippies.park"],
    ["Rory", "rory@whippies.park"]
]
print(f"{mailing_list[0][0]}: {mailing_list[0][1]}")
print(f"{mailing_list[1][0]}: {mailing_list[1][1]}")
print(f"{mailing_list[2][0]}: {mailing_list[2][1]}")
print(f"{mailing_list[3][0]}: {mailing_list[3][1]}")
print(f"{mailing_list[4][0]}: {mailing_list[4][1]}")
print()
print("Q3")
names = []
print(names)
name = input("What is your name? ")
names.append(name)
# print(names)
friend = input("What is your friend's name? ")
names.append(friend)
# print(names)
pet = input("What is your pet's name? ")
names.append(pet)
print(names)
print()

print("Q4")
print("1. Enter a string")
quote_string = []
quote = input("What is your favourite quote? ")
print(quote)
print()
print("2. Split the string")
quote_string = quote.split()
print(quote_string)
print()
print("3. Convert the string to a list of characters")
quote_characters = list(quote)
print(quote_characters)
print()
print("4. How many items in the list?")
print(f"{len(quote_string)} {quote_string}")
print(f"{len(quote_characters)} {quote_characters}")
print()