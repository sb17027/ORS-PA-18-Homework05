"""
===================   TASK 1   ====================
* Name: Power to the Number
*
* Write a function `numpower()` that will for the
* passed based number `num` and exponent `expo`
* return the value of the number `num` raised to
* the power of `expo`.
*
* Note: Please describe in details possible cases
* in which your solution might not work. It is not
* allowed to use built-in operators and functions
* for this task.
*
* Use main() function to test your solution.
===================================================
"""

import numbers

def numpower(num, expo):
    i = 1
    res = 1
    """ Making generic while loop so we multiply num with itself the precise number of times """
    """ pom expo helps variable for storing the original value - we need to handle both negative and positive ecpos """
    pom_expo = abs(expo)
    while i <= pom_expo:
        res = res * num
        i = i + 1
    """ In cases that we have negative exponent """
    if expo < 0:
        res = 1 / res

    return res

def main():
    num = 2
    expo = -4
    res = numpower(num, expo)
    print("Exponent of a number: ", res)

main()