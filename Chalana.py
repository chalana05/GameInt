import random

# entry
name = str(input("\nPlease enter your name: "))
print("\nHi", name, )
print(
    "-----------------------------------------------Welcome to GameInt------------------------------------------------------\n")


# create and initializing variable (1)
def main():
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    num3 = random.randint(1, 6)
    num4 = random.randint(1, 6)

    numlist = (num1, num2, num3, num4)

    print(
        "Number to guess - X X X X            Color Mapping : 1 - White, 2 - Blue, 3 - Red, 4 - Yellow, 5 - Green, 6 - Purple")
    print("\n* Please only input Numbers")
    print("* Please enter a value between 1 and 6")
    print("\n-----------------------------------------------------------------------------------------------------------------------")
    attempt = 1
    points = 800
    while attempt < 9:
       

        valid = 0
        while not valid:
            try:
                input1 = int(input("ENTER THE NUMBER:        "))
                valid = 1
            except ValueError:
                print('!!!Please only input Number!!!')
        while input1 > 6:
            input1 = int(input("!!!Please enter a value between 1 and 6!!!"))

        valid = 0
        while not valid:
            try:
                input2 = int(input("ENTER THE NUMBER:        "))
                valid = 1
            except ValueError:
                print('!!!Please only input Number!!!')
        while input2 > 6:
            input2 = int(input("!!!Please enter a value between 1 and 6!!!"))

        valid = 0
        while not valid:
            try:
                input3 = int(input("ENTER THE NUMBER:        "))
                valid = 1
            except ValueError:
                print('!!!Please only input Number!!!')
        while input3 > 6:
            input3 = int(input("!!!Please enter a value between 1 and 6!!!"))

        valid = 0
        while not valid:
            try:
                input4 = int(input("ENTER THE NUMBER:        "))
                valid = 1
            except ValueError:
                print('!!!Please only input Number!!!')
        while input4 > 6:
            input4 = int(input("!!!Please enter a value between 1 and 6!!!"))

        print(
            "\n-------------------------------------------------------------")
        print("Attempt no  ", "      Guess  ", "      ""       Result  ")

     
        a = False
        b = False
        c = False
        d = False
        if input1 == num1:
            a = '1'
        else:
            a = '.'
        if input2 == num2:
            b = '1'
        else:
            b = '.'
        if input3 == num3:
            c = '1'
        else:
            c = '.'
        if input4 == num4:
            d = '1'
        else:
            d = '.'

        print(attempt, "               ", input1, input2, input3, input4, "               ",        a, b,)
        print("                                         ",        c, d)
        inputlist = (input1, input2, input3, input4)

       
        if inputlist == (0, 0, 0, 0):
            print("\nGoodbye!!!")
            exit()

        if inputlist == numlist:
            print("\nCONGRATULATIONS!!! You have won the game...")
            print("\nYour have scored:", points)
            attempt = attempt + 8


        else:
            print("\nWRONG ANSWER!!!")
            print("Your have scored:", points)
            points = points - 100
            attempt = attempt + 1
        print(
            "-------------------------------------------------------------")
    if attempt == 8:
        print("\nGAME OVER.\n")

    answer = input("\nDo you want to play another game? (Yes/No) ").lower()
    if answer == "yes":
        main()
    else:
        print("\nGame over!!!")
        exit("0 0 0 0")


main()
