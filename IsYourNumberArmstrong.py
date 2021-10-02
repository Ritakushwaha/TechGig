'''

Is your Number Armstrong? (100 Marks)
For this challenge, you need to take an integer input and store it in a variable of your choice and checks whether this number is an Armstrong number or not. If yes print 'True' else print 'False'.

Input Format
A single integer value to be taken as input from stdin and stored it in a variable. 

Constraints
1 < = n < = 18

Output Format
print 'True' if your number is Armstrong otherwise print 'False' to the stdout. 

'''

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

num = int(input())

def main(num):
    num_str = str(num)
    n = len(num_str)
    sum_ = 0

    for i in num_str:
        sum_ = sum_ + (int(i)**n)

    if num == sum_:
        print('True')
    else:
        print('False')

main(num)

