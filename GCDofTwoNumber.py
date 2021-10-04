'''
GCD of two numbers (100 Marks)
For this challenge, you need to take input of two numbers , calculate their greatest common divisor (GCD) and print it to the stdout.

Input Format
You need to take two integers as an input which are separated by a single space. 

Constraints
1 < (a,b) < 10^5

Output Format
Print the single integer result to the stdout. 

'''
#Method 1
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

import math

def main(a,b):
    return math.gcd(a,b)

a ,b = list(map(int, input().split()))

print(main(a,b))



#Method 2
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

# Recursive function to return gcd of a and b
def gcd(a, b):
    if (a == 0):
        return b
    if (b == 0):
        return a
    if (a == b):
        return a
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)

a,b = list(map(int,input().split()))
print(gcd(a, b))

#MEthod 3
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

# Recursive function to return gcd of a and b

def gcd(a, b):
	if(b == 0):
		return a
	else:
		return gcd(b, a % b)

a,b = list(map(int, input().split()))
print(gcd(a,b))
