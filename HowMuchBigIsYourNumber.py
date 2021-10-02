'''

HowMuchBigIsYourNumber (100 Marks)
For this challenge, you will take an integer input from stdin, store it in a variable and  calculate the number of digits in the number using division operator.

Input Format
A single integer value to be taken as input from stdin and stored it in a variable of your choice. 

Constraints
1 < = n < = 18

Output Format
Print the value which you will get after calculating the number of digits. 

Sample TestCase 1
Input
34567
Output
5

'''


#Method 1

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

    num = int(input())
    count = 0 

    while num > 0:
        num = num//10
        count = count + 1
    print(count)

main()




#Method 2

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

    num = int(input())

    num_str = str(num)
    print(len(num_str))

main()
