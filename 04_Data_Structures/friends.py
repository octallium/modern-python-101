"""

List:
-----
Louis has been making good progress in Zortan and has made
new friends. All of them are meeting today and Louis wants
to write a program that can greet all of them.

In Zortan, people greet with saying "Zola"

Info:
-----
Lists are mutable data structures, that means the data inside can be mutated.
Index always starts from 0.
"""

# It's convenient to group all friends together using a `List`
# and them greet them
friends: list[str] = ["Cece", "Roko", "Chiko", "Niko"]
# List with Index No [   0,      1,       2,      3  ]

print(f"Friends: {friends}")

# ---------------------------------------------------------------------
# Time to greet friends using a for-in loop
# ---------------------------------------------------------------------

for friend in friends:
    print(f"Zola {friend}!")

# ---------------------------------------------------------------------
# Louis wants to count his number of friends
# ---------------------------------------------------------------------

print(f"Friends Count: {len(friends)}")

# ---------------------------------------------------------------------
# Louis had a fight with Niko and wants to unfriend him
# ---------------------------------------------------------------------

unfriend = friends.pop()
print(f"Unfriend: {unfriend}")
print(f"Friends: {friends}")


# ---------------------------------------------------------------------
# Louis makes a new friend "Ziko"
# ---------------------------------------------------------------------

friends.append("Ziko")
print(f"Friends: {friends}")

# ---------------------------------------------------------------------
# Louis wants to check who is 3rd in this friends list
# ---------------------------------------------------------------------

print(friends[2])
# ------------^ Remember since List starts from index 0, we use 2 here

# ---------------------------------------------------------------------
# Oh-no Louis again had a fight, this time with Roko
# ---------------------------------------------------------------------

friends.remove("Roko")
print(f"Friends: {friends}")

# ---------------------------------------------------------------------
# Louis and Roko become friends again!
# ---------------------------------------------------------------------

friends.insert(1, "Roko")
print(f"Friends: {friends}")

# ---------------------------------------------------------------------
# Louis wants to confirm if Roko is in friends list
# ---------------------------------------------------------------------

if "Roko" in friends:
    print("Yay, Roko is in the friend list")
else:
    print("Oh no, Roko is not your friend")

# ---------------------------------------------------------------------
# Louis patches up with Niko as well and he becomes his no. 1 friend
# ---------------------------------------------------------------------

friends.insert(0, "Niko")
print(f"Friends: {friends}")

# ---------------------------------------------------------------------
# Louis wants to sort his friends in alphabetical order
# ---------------------------------------------------------------------

friends.sort()
print(f"Friends: {friends}")

# ---------------------------------------------------------------------
# Na, Louis doesn't like this ordering and wants to reverse the order
# ---------------------------------------------------------------------

friends.reverse()
print(f"Friends: {friends}")

# ---------------------------------------------------------------------
# What's this!! Louis again had a fight with Niko
# ---------------------------------------------------------------------

unfriend = friends.pop(2)
print(f"Unfriend: {unfriend}")
print(f"Friends: {friends}")
