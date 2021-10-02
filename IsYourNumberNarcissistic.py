'''
Is Your Number Narcissistic? (110 Marks)
For this challenge, you will take an integer input and store it in a variable and checks whether the input number is a Narcissistic number or not. If it is, then print 'True' else print 'False'.


Input Format
A single integer value to be taken as input from stdin and stored it in a variable of your choice. 

Constraints
1 < = n < = 18

Output Format
print 'True' if your number is Narcissistic otherwise print 'False' to the stdout. 
'''

#Method 1

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

num = int(input())

def main(num):
    num_str = str(num)
    n = len(num_str)
    sum_ = 0

    for i in num_str:
        sum_ = sum_ + int(i)**n
        print(sum_)

    if num == sum_:
        print('True')
    else:
        print('False')

main(num)





#Method 2
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

num = int(input())

def main(num):
    return num == sum([int(x) ** len(str(num)) for x in str(num)])

print(main(num))
