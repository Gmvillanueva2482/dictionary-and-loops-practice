# this is what we will use for the video intro to dictionaries

# dictionary = a collection of {key:value} pairs 
# ordered and changeable, No duplicates

capitals = {"USA":"Washington D.C.","India":"New Delhi","China":"Beijing", "Russia":"Moscow"}

# print(dir(capitals))
# print(help(capitals))

print(capitals.get("India"))
print(capitals.get("USA"))

if capitals.get("Japan"):
    print("The captial exist")
else:
    print("The captial doesn't exist")


if capitals.get("Russia"):
    print("The captial exist")
else:
    print("The captial doesn't exist")

# capitals.update ({"Germany":"Berlin"})
# capitals.update ({"USA", "Detroit"})
# capitals.update ("China")
#capitals.popitem()      get rid of latest one
#capitals.clear()

keys = capitals.keys()

print(keys)

# for key in capitals.keys():
#    print(key)

# values = capitals.values()
# for value in capitals.values():
#    print(values)

items = capitals.item()
for key, value in capitals.items():
    print(f"{key}: {value}")