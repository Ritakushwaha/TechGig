'''
Find pairs (100 Marks)
For this challenge, you need to take array and an integer as an input, check for pair in array with sum as that of an integer and if you find those two numbers in the array return true else return false.

Input Format
You need to take an integer input on first line which tells about the size of the array.Another line will have array elements separated by spaces. Last line will have an integer input that defines the number for which the pair has to be searched in the array. 

Constraints
1 < n < 10^5
1 < A[i] < 10^5

Output Format
Print 'True' if the pair found in the array element else print 'False' to the stdout. 

'''

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main(N,arr,num):
    isPresent = 0
    for i in range(N-1):
        if num == arr[i]+arr[i+1]:
            isPresent =1
            break
    if isPresent ==1:
        print("True")
    else:
        print("False")

N = int(input())
arr = list(map(int, input().split()))
num = int(input())

main(N,arr,num)
