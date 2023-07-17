print("Welcome to my computer quiz game!")
play = input("Do you want to play? ")
if play.lower() != "yes":
    quit()
print("Get ready!")

ans1 = input("What does AI stand for? ")
if ans1.lower() != "artificial intelligence":
    print("Sorry, that's incorrect.")
else:
    print("You are correct!")

play2 = input("Do you want to continue? ")
if play2.lower() != "yes":
    quit()
print("Here is your next question.")

ans2 = input("What does CPU stand for? ")
if ans2.lower() != "central processing unit":
    print("Sorry, that's incorrect.")
else:
    print("You are correct!")

rank = 0  # Assuming the user answered both questions incorrectly
if ans1.lower() == "artificial intelligence":
    rank += 1
if ans2.lower() == "central processing unit":
    rank += 1

print("Your rank is:", rank)
print("Thank you for your participation. Have a nice day!")

