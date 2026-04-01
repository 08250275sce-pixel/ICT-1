age =int(input ("Enter your age"))
if age >= 18:
    registered_voter = input("Are you registered voter(true/False):")
    registered_voter =registered_voter.lower()
    if registered_voter == "true":
        print("you are eligiblefor vote")
    else:
        print("you need to register to vote")
else:
    print("You are noteligible to vote")
