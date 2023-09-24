#This game ask multiple choice question . The game will also keep track of the score and it is going to print it at the end.

import time

#Welcome the user
print("Welcome to the Simple Quiz Game!")
time.sleep(1)

#Chances
chances = 1
print("You will have", chances, "chance to answer correctly. \nPlease put the alphabet of the answer\n")
time.sleep(2)

#Score
score = 0

#question number 1
question_1 = print("1) What day is Canada Day?\n(a) July 4\n(b) July 2\n(c) July 1\n(d) July 3\n\n ")
answer_1 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_1, "\n\n")

time.sleep(2)


#question number 2
question_2 = print("2) What is the capital of France?\n(a)Paris\n(b)London\n(c)Berlin\n(d)New York\n\n")
answer_2 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_2):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_2, "\n\n")

time.sleep(2)

    
#question number 3
question_3 = print("3) What is the largest city of Canada?\n(a) Quebec\n(b) Toronto\n(c) Vancouver\n(d) Winnipeg\n(e) Edmonton\n(f) Montreal\n\n ")
answer_3 = "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_3, "\n\n")

time.sleep(2)


#question number 4
question_4 = print("4) What is the largest planet in our solar system ?\n(a)Earth\n(b)Jupiter\n(c)Mars\n(d)Mercury\n\n ")
answer_4 = "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_4, "\n\n")

time.sleep(2)


#question number 5
question_5 = print("5) What is Canada's national animal?\n(a) Beaver\n(b) Canadian Horse\n(c) Moose\n(d) Goose\n\n ")
answer_5 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_5):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_5, "\n\n")

time.sleep(2)


#question number 6
question_6   =print("6) Who painted the Mona Lisa?\n(a)Micheal\n(b)Ronaldo\n(c)Geenie lorque\n(d)Leonardo da Vinci\n\n")
answer_6 = "d"                                  

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_6):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_6, "\n\n")

time.sleep(2)


#question number 7
question_7 = print("7) What is correct extension of the Python file?\n(a) .python\n(b) .pi\n(c) .py\n(d) .p\n\n ")
answer_7 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_7):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_7, "\n\n")

time.sleep(2)


#question number 8
question_8 = print("8) Which built-in function can get information from the user?\n(a)get\n(b)input\n(c)print\n(d)write\n\n ")
answer_8 = "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_8):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_8, "\n\n")

time.sleep(2)


#question number 9
question_9 = print("9)What's the purpose of the built-in zip() function?\n(a)To combine several strings into one\n(b)To compress several files into one archive\n(c)To iterate over two or more sequences at the same time\n(d)To get information from the user\n\n ")
answer_9 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_9):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_9, "\n\n")

time.sleep(2)


#question number 10
question_10= print("10) Which keyword do you use to loop over a given list of elements?\n(a)for\n(b)while\n)(c)each\n(d)loop n\n ")
answer_10 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_10):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_10, "\n\n")

time.sleep(2)

#question number 11
question_11= print("11) Which planet is known as the Red Planet?\n(a)Earth\n(b)Jupiter\n(c)Venus\n(d)Mars \n\n ")
answer_11 = "d"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_11):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_11, "\n\n")

time.sleep(2)


#question number 12
question_12= print("12)What is the largest mammal in the world ?\n(a)Elephant\n(b)Giraffe\n(c)Blue Whale\n(d)Lion \n\n ")
answer_12 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_12):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_12, "\n\n")

time.sleep(2)


#question number 13
question_13= print("13) What is the capital of Canada?\n(a) Toronto\n(b) Montreal\n(c) Vancouver\n(d) Ottawa\n\n ")
answer_13 = "d"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_13):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_13, "\n\n")

time.sleep(2)


#question number 14
question_14= print("14) what isthe capital of Queensland?\n(a) Toronto\n(b) Brisbane\n(c) Vancouver\n(d) Noosa\n\n ")
answer_14 = "b"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_14):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_14, "\n\n")

time.sleep(2)


#question number 15
question_15= print("15) what state is Birdsville found?\n(a) NSW\n(b) SA\n(c) QLD\n(d) DS\n\n ")
answer_15 = "c"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_15):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_15, "\n\n")

time.sleep(2)


#question number 16
question_16= print("16) When is Gourmet in Gundy held?\n(a) August\n(b) September\n(c) October\n(d) November\n\n ")
answer_16 = "b"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_16):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_16, "\n\n")

time.sleep(2)


#question number 17
question_17= print("17) IsPython case sensitive when dealing with Identifiers?\n(a)Yes \n(b) No\n(c) Machine dependent\n(d) None\n\n ")
answer_17 = "a"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_17):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_17, "\n\n")

time.sleep(2)


#question number 18
question_18= print("18) Which type of Programming does Python support?\n(a)object-oriented programming\n(b) structured programming\n(c) functional programming\n(d) all of the above\n\n ")
answer_18 = "d"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_18):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_18, "\n\n")

time.sleep(2)


#question number 19
question_19= print("19) Which of the following is not a keyword?\n(a)eval \n(b) assert\n(c) local\n(d) pass\n\n ")
answer_19 = "a"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_19):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_19, "\n\n")

time.sleep(2)


#question number 20
question_20= print("20) Which one of these is floor division ?\n(a)/ \n(b)//\n(c)%\n(d) None\n\n ")
answer_20 = "b"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_20):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_20, "\n\n")

time.sleep(2)


#question number 21
question_21= print("21) Which Keyword is used for function in Python language? \n(a)function\n(b)def\n(c)define\n(d)none\n\n ")
answer_21= "b"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_21):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_21, "\n\n")

time.sleep(2)


#question number 22
question_22= print("22) Who created Python? \n(a)Guido van Rossum\n(b)Elon Musk\n(c)Bill Gates\n(d) Mark Zuckerburg\n\n ")
answer_22= "a"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_22):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_22, "\n\n")

time.sleep(2)


#question number 23
question_23= print("23) What year was Python created ? \n(a)1989\n(b)1991\n(c)2000\n(d)2016\n\n ")
answer_23= "b"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_23):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_23, "\n\n")

time.sleep(2)


#question number 24
question_24= print("24) Python is tributed to which comedy group? \n(a)Lonely Island\n(b)Smosh\n(c)Monty Python\n(d)SNL\n\n ")
answer_24= "c"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_24):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_24, "\n\n")

time.sleep(2)


#question number 25
question_25= print("25) Is Earth round? \n(a)True\n(b)False\n(c)Sometimes\n(d)None\n\n ")
answer_25= "a"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_25):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_25, "\n\n")

time.sleep(2)


#question number 26
question_26= print("26) Who developed Yahoo? \n(a)Dennis Richie & Ken Thompson\n(b)David Filo & Jerry Yang\n(c)Vint Cerf & Robert Kahn\n(d)Steve Case & Jeff Bezos9i\n\n ")
answer_26= "b"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_26):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_26, "\n\n")

time.sleep(2)


#question number 27
question_27= print("27) What does WWW stand for? \n(a)World Wide Web\n(b)Wide Webpage Web\n(c)World Webinar Web\n(d)None\n\n ")
answer_27= "a"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_27):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_27, "\n\n")

time.sleep(2)


#question number 28
question_28= print("28) Python supports the creation of anonymous functions at runtime,using a construct called? \n(a)pi\n(b)anonymous\n(c)lambda\n(d)none\n\n ")
answer_28= "c"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_28):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_28, "\n\n")

time.sleep(2)


#question number 29
question_29= print("29) What does pip stands for Python? \n(a)Pip Installs Python\n(b)Pip Installs Packages\n(c)Preferred Installed Program\n(d)none\n\n ")
answer_29= "c"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_29):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_29, "\n\n")

time.sleep(2)


#question number 30
question_30= print("30) What is output of print(math.pow(3,2))? \n(a)9.0\n(b)4.0\n(c)9\n(d)none\n\n ")
answer_30= "a"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_30):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.3)
        print("The correct answer is", answer_30, "\n\n")

time.sleep(1)

#print the score
while score >= 4:
    print("Well done! Your score was", score)
    break

while score <= 3:
    print("Better luck next time! Your score was", score)
    break
#Goodbye message
print("Thank you for playing the Simple Quiz Game!")