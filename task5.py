"""
===================   TASK 5   ====================
* Name: Average Value
*
* Write a function `averageval` that will take a
* integer list as an argument and return the 
* average value of the list elements.  
*
* Note: Please describe in details possible cases
* in which your solution might not work. It is not
* allowed to use built-in functions.
*
* Use main() function to test your solution.
===================================================
"""
def averageval(numlist):
    numberOfElements = len(numlist)
    i = 0
    sum = 0
    while i < len(numlist):
        sum = sum + numlist[i]
        i = i + 1
    return sum / numberOfElements

def main():
    numlist = [1, 2, 3, 4, 5]
    avg = averageval(numlist)
    print("Average val is: ", avg)
main()