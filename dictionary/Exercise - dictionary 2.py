# Create a dictionary of favorite food for some of your friend
favorite_foods = {
  "Bob": "tommy",
  "Sally": "bob",
  "Tommy": "sally"
}

# Ask the user to enter the name of a friend
friend_name = input("Enter the name of a friend: ")

# Check if the friend is in the dictionary and print their favorite food if they are
if friend_name in favorite_foods:
  print(f"{friend_name}'s favorite food is {favorite_foods[friend_name]}!")
else:
  print(f"Sorry, {friend_name} is not in our list of friend.")

# Hints:
# 1. This is the thing that people like to eat
# 2. These are the people whose favorite foods we are storing in the dictionary
# 3. Bob's favorite food is ___3___
# 4. Sally's favorite food is ___4___
# 5. Tommy's favorite food is ___5___
