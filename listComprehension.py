"we have a list thats needs to be modified and stored in a new list"

"Old code: "
old = [2,5,9]
new = []
for num in old:
    new_num = num + 2
    new.append(new_num)

"With list comprehension"
new2 = [item + 2 for item in old]

"Another example transferring string to list"
name = "name"
letter_list = [letter for letter in name]

"Using a range"
new_range = [num*2 for num in range(1,4)]

"Cleans up/shortens code using iterables"

"Adding conditionals"
guests = ["Bob", "Dave", "Vlad", "Reznov", "Siegfried", "Pendragon", "Gawain", "Joe"]
vip = [name for name in guests if len(name)<5] #guests w/ <5 letter names

"Follows standard modifications to variables"
vip = [name.upper() for name in vip]