import random
import time

# creating 3 variables and giving them the value 0
level = 1
correct = 0
wrong = 0

# main function
"""
Get global varible level and correct
Set level to 1 and print that the level is set to 1
Set correct to 0 for each timt they enter main
Ask for the users input on what sum they would like to done
If statements to go to certain functions depending on user input
"""


def main():
    global level
    global correct

    level = 1
    correct = 0
    print("\n----------------------------------------------------")
    print("Level set to:", level)
    print("----------------------------------------------------")
    print("\nSelect one of the following options:")
    print("(1) Addition, (2) Subtraction, (3) Multiplication, (4) Divison, (5) Random sums, (6) Quit")
    num = input("Your choice: ")

    if num == "1":
        add()
    elif num == "2":
        sub()
    elif num == "3":
        mul()
    elif num == "4":
        div()
    elif num == "5":
        rand()
    elif num == "6":
        print("\nGoodbye!")
        exit()
    else:
        main()


# levels function
"""
Get global variable num1 and num2
If statement to check what level the user is on
Depending on the level it sets num1 and num2 to select numbers from random integers
Then returns back to the function
"""


def lev():

    global num1
    global num2

    if level == 1:
        rand = [1, 2, 3, 4]
        num1 = random.choice(rand)
        num2 = random.choice(rand)
        return
    elif level == 2:
        rand = [1, 2, 3, 4, 5]
        num1 = random.choice(rand)
        num2 = random.choice(rand)
        return
    elif level == 3:
        rand = [1, 2, 3, 4, 5, 6]
        num1 = random.choice(rand)
        num2 = random.choice(rand)
        return
    elif level == 4:
        rand = [1, 2, 3, 4, 5, 6, 7]
        num1 = random.choice(rand)
        num2 = random.choice(rand)
        return
    elif level == 5:
        rand = [1, 2, 3, 4, 5, 6, 7, 8]
        num1 = random.choice(rand)
        num2 = random.choice(rand)
        return
    elif level == 6:
        rand = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        num1 = random.choice(rand)
        num2 = random.choice(rand)
        return
    elif level == 7:
        rand = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        num1 = random.choice(rand)
        num2 = random.choice(rand)
        return


# addition function
"""
Go to level function to get current levels integer range
Then set result to be num1 plus num2 from random integer range of the level
Start the timer to time how long it takes the user to answer
Then set answer to be the users input
If the users input equals the result of the answer then go to correct function
Else if the user input is wrong go to the wrong function
"""


def add():
    lev()
    result = int(num1) + int(num2)

    print("\nWhat is ", num1, "+", num2, "?", sep="")
    starttime = time.time()
    ans = int(input("Answer: "))

    if ans == result:
        cor(starttime)
        add()
    else:
        wro(result, starttime)
        add()


# subtraction function
"""
While true loop to make sure the result is greater than 0 before asking the question
Go to level function to get current levels integer range
Then set result to be num1 minus num2 from random integer range of the level
If the result is greater than 0 break and ask question
Start the timer to time how long it takes the user to answer
Then set answer to be the users input
If the users input equals the result of the answer then go to correct function
Else if the user input is wrong go to the wrong function
"""


def sub():

    while True:
        lev()
        result = int(num1) - int(num2)

        if result > 0:
            break

    print("\nWhat is ", num1, "-", num2, "?", sep="")

    starttime = time.time()
    ans = int(input("Answer: "))

    if ans == result:
        cor(starttime)
        sub()
    else:
        wro(result, starttime)
        sub()


# multiplication function
"""
Go to level function to get current levels integer range
Then set result to be num1 multiplied by num2 from random integer range of the level
Start the timer to time how long it takes the user to answer
Then set answer to be the users input
If the users input equals the result of the answer then go to correct function
Else if the user input is wrong go to the wrong function
"""


def mul():
    lev()
    result = int(num1) * int(num2)

    print("\nWhat is ", num1, "x", num2, "?", sep="")
    starttime = time.time()
    ans = int(input("Answer: "))

    if ans == result:
        cor(starttime)
        mul()
    else:
        wro(result, starttime)
        mul()

# divison function


"""
While true loop to make sure the result is greater than 0 and is an integer before asking the question
Go to level function to get current levels integer range
Then set result to be num1 minus num2 from random integer range of the level
If the result is an integer break and ask question
Start the timer to time how long it takes the user to answer
Then set answer to be the users input
If the users input equals the result of the answer then go to correct function
Else if the user input is wrong go to the wrong function
"""


def div():

    while True:
        lev()
        result = float(num1) / float(num2)

        if result.is_integer():
            break

    print("\nWhat is ", num1, "/", num2, "?", sep="")
    starttime = time.time()
    ans = float(input("Answer: "))

    if ans == result:
        cor(starttime)
        div()
    else:
        wro(result, starttime)
        div()


# random sums function
"""
While true loop to make sure the result is greater than 0 and is an integer before asking the question
Go to level function to get current levels integer range
Set operator to be a random choice from the four operators
Then set result to be num1 then the operation num2 from random integer range of the level
If the result is greater than 0 and is an integer break and ask question
If the operator is multiplcation then ask the user the question with an "x" instead of "*"
Start the timer to time how long it takes the user to answer
Else if its any other operator
Then set answer to be the users input
If the users input equals the result of the answer then go to correct function
Else if the user input is wrong go to the wrong function
"""


def rand():

    while True:
        lev()
        operator = random.choice("+-/*")
        result = eval(str(num1) + operator + str(num2))

        if result > 0 and float(result).is_integer():
            break

    if operator == "*":
        print("\nWhat is ", num1, "x", num2, "?", sep="")
        starttime = time.time()
    else:
        print("\nWhat is ", num1, operator, num2, "?", sep="")
        starttime = time.time()

    ans = int(input("Answer: "))
    if ans == result:
        cor(starttime)
        rand()
    else:
        wro(result, starttime)
        rand()


# correct answer function with result and starttime parameters passed
"""
Get the global variables of wrong, correct and level
Set endtime to end and set fin to be endtime minus start time
Set varible wrong to be 0 each time you get an answer correct and enter the correct function
If level is 7 then set correct to 0 so you dont go any higher than level 6
Print that the user is correct
Print the time it took the user to the whole number
Print the level the user is on
Ask the user if they want to try another sum
Set reply to be the users input
If the reply is "Y" or "y" then return back to the method
Else if the reply is "N" or "n" then return to main function
And if the user is not at level 7
Increase the correct variable by 1
If correct is equal to 3 then increase the level and set correct back to 0
Then print the same as before
"""


def cor(starttime):

    global wrong
    global correct
    global level

    endtime = time.time()
    fin = endtime - starttime

    wrong = 0
    if level == 7:
        correct = 0

        print("\n----------------------------------------------------")
        print("It took you", "%.0f" % fin, "seconds.")
        print("\nLevel:", level)
        print("----------------------------------------------------")
        print("\nThat is correct, well done!")
        print("Press Y to try another sum or N to stop.")
        reply = input("Your choice: ")

        if reply == "Y" or reply == "y":
            return
        elif reply == "N" or reply == "n":
            main()

    else:
        correct += 1
        if correct == 3:
            level += 1
            correct = 0

        print("\n----------------------------------------------------")
        print("It took you", "%.0f" % fin, "second(s).")
        print("\nLevel:", level, "\nConsecutively Correct:", correct)
        print("----------------------------------------------------")
        print("\nThat is correct, well done!")
        print("Press Y to try another sum or N to stop.")
        reply = input("Your choice: ")

        if reply == "Y" or reply == "y":
            return
        elif reply == "N" or reply == "n":
            main()

# wrong answer function with result and starttime parameters passed


"""
Get the global variables of wrong, correct and level
Set endtime to end and set fin to be endtime minus start time
Set varible correct to be 0 each time you get an answer wrong and enter the wrong function
Increase wrong variable by 1 each time you enter the wrong function
If level is 1 then set wrong to 0 so you dont go any lower than level 1
Else if the level is greater than 1 and if wrong is 3 then decrease the level by 1 and set wrong to 0
Print that the user is wrong and print the correct answer
Print the time it took the user to the whole number
Print the level the user is on and how many correct answers they have
Ask the user if they want to try another sum
Set reply to be the users input
If the reply is "Y" or "y" then return back to the method
Else if the reply is "N" or "n" then return to main function
"""


def wro(result, starttime):

    global wrong
    global correct
    global level

    endtime = time.time()
    fin = endtime - starttime

    correct = 0
    wrong += 1

    if level == 1:
        wrong = 0

    elif level > 1 and wrong == 3:
        level -= 1
        wrong = 0

        print("\n----------------------------------------------------")
        print("It took you", "%.0f" % fin, "second(s).")
        print("\nLevel:", level, "\nConsecutively Correct:", correct)
        print("----------------------------------------------------")

    print("\nNot right, the correct answer is:", "%.0f" % result)
    print("Press Y to try another sum or N to stop.")
    reply = input("Your choice: ")
    if reply == "Y" or reply == "y":
        return
    elif reply == "N" or reply == "n":
        main()


# if statement to go straight to main method
if __name__ == "__main__":
    main()
