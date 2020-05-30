# Module 7
#   Programming Assignment 10
#     Prob-1.py

# Eddy
# Write a program that asks the user for numbers, and provides the sum of the numbers when finished.

# Valid numbers are non-negative. The user signals the end of the list by entering a negative number.
# not for its while loop
# if number is less then 0 exit the loop


def main():
    total = 0
    usernumber = float(input("lets start by entering a number: "))

    while True:
        if usernumber >= 0:
            total = total + usernumber
            usernumber = float(
                input("now enter another number, or enter a negitve number to stop: "))
        else:
            break

    print("the grand total is: ", total)


main()
