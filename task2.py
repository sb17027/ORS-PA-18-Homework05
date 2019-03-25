"""
===================   TASK 2   ====================
* Name: Most Frequent Letter
*
* Write a script that takes the stirng as user
* input and displays which letter has the most
* occurences and how many. If two or more letters
* have the same number of occurences print any.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
===================================================
"""

def char_occurences(str):
    most_char = ""
    i = 0
    j = 0
    current_occurences = 0
    most_occurences = 0
    while i < len(str):
        while j < len(str):
            if str[i] == str[j]:
                current_occurences = current_occurences + 1
            j = j + 1
        if (current_occurences > most_occurences):
            most_occurences = current_occurences
            most_char = str[i]
        i = i + 1
        j = 0
    print("Char with the most occurences: ", most_char)

def main():
    str = input("Insret string: ")
    char_occurences(str)
main()