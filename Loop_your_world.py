'''

Loop your world

For this challenge, you need to take an integer value as input from stdin, calculate its factorial and print the result to the stdout. 1

Input Format
A single integer value to be taken as input from stdin and stored it in a variable of your choice. 

Constraints
1 < = n < = 15

Output Format
Print the value which you will get after calculating the factorial of the input. 
'''

'''Method 1'''

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import math

def main():

    num = int(input())
    print(math.factorial(num))

main()



'''Method 2'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

num = int(input())

def fac(num):
    if num>0:
        return 1 if (num==0 or num==1) else num*fac(num-1)

print(fac(num))
