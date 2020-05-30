# Module 7
#   Programming Assignment 10
#     Prob-3.py

# Eddy


def main():
    total = 0
    while True:
        usernumber = float(
            input("enter a number, or enter a negitve number to stop: "))
        if usernumber >= 0:
            total = total + usernumber
        else:
            break

    print("the grand total is: ", total)


main()
