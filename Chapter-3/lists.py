# 3-1. Names: Store the names of a few of your friends in a list called names Print
# each person’s name by accessing each element in the list, one at a time

names = ["Saad Abdullah", "Maaz", "Ibrahim", "Sikandar", "Umer Sher Khan"]

message = 'Hello my friend, '
print(message + names[0])
print(message + names[1])
print(message + names[2])
print(message + names[3])
print(message + names[4])

# list.pop() will remove the last element and we can store that element in a variable 
# list.pop(0) will remove item from the very start of the array

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner Then use your list to print a message to each person, inviting
# them to dinner

invited_people = ["Haris", "Nabeel", "Hassaan"]

print("Hello Mr." + invited_people[0] + ", it will be a pleasure if you join us for dinner tonight at 9pm")
print("\n")
print("Hello Mr." + invited_people[1] + ", it will be a pleasure if you join us for dinner tonight at 9pm")
print("\n")
print("Hello Mr." + invited_people[2] + ", it will be a pleasure if you join us for dinner tonight at 9pm")
print("\n")

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations You’ll have to think of
# someone else to invite
# • Start with your program from Exercise 3-4 Add a print statement at the
# end of your program stating the name of the guest who can’t make it
# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting
# • Print a second set of invitation messages, one for each person who is still
# in your list

print("Unfortunately Mr." + invited_people[0] + ", will not be able to join us for the dinner today")
print("\n")
invited_people[0] = "Umer"
print("Hello Mr." + invited_people[0] + ", it will be a pleasure if you join us for dinner tonight at 9pm")
print("\n")
print("Hello Mr." + invited_people[1] + ", it will be a pleasure if you join us for dinner tonight at 9pm")
print("\n")
print("Hello Mr." + invited_people[2] + ", it will be a pleasure if you join us for dinner tonight at 9pm")
print("\n")

# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available Think of three more guests to invite to dinner
# • Start with your program from Exercise 3-4 or Exercise 3-5 Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table
# • Use insert() to add one new guest to the beginning of your list
# • Use insert() to add one new guest to the middle of your list
# • Use append() to add one new guest to the end of your list
# • Print a new set of invitation messages, one for each person in your list

print("\n")
print("We just found a bigger table to accommodate more guests")
print("\n")
invited_people.insert(0, "Saad Abdullah")
invited_people.insert(1, "Maaz Khan")
invited_people.append("Ibrahim")

for person in invited_people:
    print("Hello Mr." + person + ", it will be a pleasure if you join us for dinner tonight at 9pm\n")
