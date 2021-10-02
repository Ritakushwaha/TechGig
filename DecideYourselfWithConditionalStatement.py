'''

Decide yourself with conditional statement


For this challenge, you need to read a integer value(default name - age) from stdin, store it in a variable and then compare that value with the conditions given below -
    - if age is less than 10, then print 'I am happy as having no responsibilities.' to the stdout.
    - if age is equal to or greater than 10 but less than 18, then print 'I am still happy but starts feeling pressure of life.' to the stdout.
    - if age is equal to or greater than 18, then print 'I am very much happy as i handled the pressure very well.' to the stdout. 

Input Format
A single line to be taken as input and save it into a variable of your choice(Default name - age). 

Constraints
1 < = age < = 100 

Output Format
Print the sentence according to the value of the integer which you had taken as an input. 
'''

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

    age = int(input())
    if age>=18:
        print('I am very much happy as i handled the pressure very well.')
    elif age>=10:
        print('I am still happy but starts feeling pressure of life.')
    else:
        print('I am happy as having no responsibilities.')

main()

