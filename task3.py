"""
===================   TASK 3   ====================
* Name: Convert to Octal
*
* Write a function `dec2oct` that will convert
* positive integer number passed as argument into
* the octal based number. 
*
* Note: Please describe in details possible cases
* in which your solution might not work. It is not
* allowed to use built-in functions.
*
* Use main() function to test your solution.
===================================================
"""
def octal(a):
    res = ""
    while a > 0:
        rem = a % 8
        res = res + str(rem)
        a = a // 8
    res = res[::-1]
    print("Octal based number of ", a, " is: ", res)

def main():
    a = 22
    octal(a)

main()