"""
===================   TASK 4   ====================
* Name: Can String Be Float
*
* Write a script that will take integer number as
* user input and return the product of digits. 
* The script should be able to handle incorrect
* input, as well as the negative integer numbers.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""
def product_digits(num):
    if(num[0] == '-'):
        num = num[1:]

    if (num.isdigit()):
        num = int(num)
    else:
        print("Wrong parameter")
        return -1

    prod = 1

    while num > 0:
        digit = num % 10
        prod = prod * digit
        num = num // 10
    return prod

def main():
    num = input ("Insert a number: ")
    print("Sum of digits is: ", product_digits(num))

main()