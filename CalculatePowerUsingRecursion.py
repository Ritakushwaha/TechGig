'''
Calculate power using Recursion (100 Marks)
This program takes two integers from user ( base number and a exponent) and calculates the power. Instead of using loops to calculate power, this program uses recursion to calculate the power of a number.

Input Format
For this challenge, you need to take 2 integer inputs from stdin which are separated by a single space. 

Constraints
1 < N < 50
0 <= P <= 12

Output Format
You will print the answer to the stdout. 
'''

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

base, exponent = map(int,input().split())

def power_func(base, exponent):
    if exponent==0 :
        return 1
    elif exponent == 1:
        return base
    else:
        return (base*power_func(base,(exponent-1)))

print(power_func(base,exponent))
