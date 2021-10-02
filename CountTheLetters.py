'''
Count the letters (100 Marks)
For this challenge, you need to take a string as an input from the stdin, count the number of uppercase and lowercase letters and print them to the stdout.

Input Format
A single line of string to be taken as an input and store it in a variable of your choice. 

Constraints
1 < = |s| < = 100000 

Output Format
print the number of uppercase letters on one line and number of lowercase letters on another side. 

'''

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    upper_count =0
    lower_count =0
    string = str(input())
    for i in string:
        if i.isupper():
            upper_count = upper_count+1
        elif i.islower():
            lower_count = lower_count+1
    print(upper_count)
    print(lower_count)

main()
