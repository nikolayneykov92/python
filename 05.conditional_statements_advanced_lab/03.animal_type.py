animal = input()

is_mammal = animal == "dog"
is_reptile = animal == "crocodile" or animal == "tortoise" or animal == "snake"

if is_mammal:
    print("mammal")
elif is_reptile:
    print("reptile")
else:
    print("unknown")
