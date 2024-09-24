print("Welcome to quiz")
play = input("Do you want to play? : ")
if play.lower() != "yes":
    quit()

print("Okay! Let's Play :)")

Score = 0

answer = input("1. Full-form of NIA: ") 
if answer.lower() == "national investigation agency":
    print("You're right!")
    Score += 1
else:
    print("Oh sorry! Incorrect")
    print("The correct answer is National Investigation Agency")

answer = input("2. Full-form of ISRO: ") 
if answer.lower() == "indian space research organisation":
    print("You're right!")
    Score += 1
else:
    print("Oh sorry! Incorrect")
    print("The correct answer is Indian Space Research Organisation")

answer = input("3. Full-form of DRDO: ") 
if answer.lower() == "defence research and development organisation":
    print("You're right!")
    Score += 1
else:
    print("Oh sorry! Incorrect")
    print("The correct answer is Defence Research and Development Organisation")

answer = input("4. Full-form of CBI: ") 
if answer.lower() == "central bureau of investigation":
    print("You're right!")
    Score += 1
else:
    print("Oh sorry! Incorrect")
    print("The correct answer is Central Bureau of Investigation")

answer = input("5. Full-form of BHEL: ") 
if answer.lower() == "bharat heavy electricals limited":
    print("You're right!")
    Score += 1
else:
    print("Oh sorry! Incorrect")
    print("The correct answer is Bharat Heavy Electricals Limited")

answer = input("6. Full-form of SAIL: ") 
if answer.lower() == "steel authority of india limited":
    print("You're right!")
    Score += 1
else:
    print("Oh sorry! Incorrect")
    print("The correct answer is Steel Authority of India Limited")

answer = input("7. Full-form of RAW: ") 
if answer.lower() == "research and analysis wing":
    print("You're right!")
    Score += 1
else:
    print("Oh sorry! Incorrect")
    print("The correct answer is Research and Analysis Wing")

answer = input("8. Full-form of NDA: ") 
if answer.lower() == "national defence academy":
    print("You're right!")
    Score += 1
else:
    print("Oh sorry! Incorrect")
    print("The correct answer is National Defence Academy")

answer = input("9. Full-form of BSF: ") 
if answer.lower() == "border security force":
    print("You're right!")
    Score += 1
else:
    print("Oh sorry! Incorrect")
    print("The correct answer is Border Security Force")

answer = input("10. Full-form of ATS: ") 
if answer.lower() == "anti terrorism squad":
    print("You're right!")
    Score += 1
else:
    print("Oh sorry! Incorrect")
    print("The correct answer is Anti Terrorism Squad")

print("You scored " + str(Score) + " questions correct!")
print("you got" + str ((Score/10)*100)+"%.")