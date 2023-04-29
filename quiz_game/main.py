print("Welcome to my computer quiz")
count = 0
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets play")

answer = input("What does CPU stand for? ")
if  answer.lower() == "central processing unit":
    print("Correct!")
    count += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if  answer.lower() == "graphics processing unit":
    print("Correct!")
    count += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if  answer.lower() == "random access memory":
    print("Correct!")
    count += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if  answer.lower() == "power supply":
    print("Correct!")
    count += 1
else:
    print("Incorrect!")


if count >= 4:
    print("Congrats you answered all my questions correctly!!!!")
else:
    print("You answered " +str(count) + " out of 4 questions correctly")