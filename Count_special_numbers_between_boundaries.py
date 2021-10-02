'''

Count special numbers between boundaries (100 Marks)
For this challenge, you are given a range and you need to find how many prime numbers lying between the given range.

Input Format
For this challenge, you need to take two integers on separate lines. These numbers defines the range. 

Constraints
1 < = ( a , b ) < = 100000

Output Format
output will be the single number which tells how many prime numbers are there between given range.

'''

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

    start = int(input())
    end = int(input())
    count = 0

    for i in range(start, end+1):
      if i>1:
        for j in range(2,i):
            if(i % j==0):
                break
        else:
            count = count+1
    print(count)

main()

