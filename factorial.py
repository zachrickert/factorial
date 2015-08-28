#factorial.py
# calculates the factorial of a given number

def main():
    print("This program will calculate the factorial of a given number.")

    x = input("Enter a number: ")
    fact = 1

    for i in range(x):
        fact = fact * (i + 1)

    print(str(x) + "! = " + str(fact))

main()
