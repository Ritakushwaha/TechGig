'''
Roll your matrix (100 Marks)
For this challenge, you need to take a matrix as an input from the stdin , transpose it and print the resultant matrix to the stdout.

Input Format
A matrix is to be taken as input from stdin. On first line you need to tell that how many rows and columns your matrix need to have and these values should be separated by space. Below lines will represent the elements of the matrix where each line will represent the row of the matrix.

Constraints
1 < (n,m) < 100

Output Format
Print the resultant matrix to the stdout where each line should represent each row and values in the row should be separated by a space. 

Sample TestCase 1
Input
3 3
1 2 3
4 5 6
7 8 9
Output
1 4 7
2 5 8
3 6 9

'''
'''Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def inputs():
    row, col = map(int,input().split())
    matrix=[]
    for i in range(row):
        matrix.append(list(map(int, input().split())))
    return matrix


def main():

    matrix = inputs()
    t_matrix = list(zip(*matrix))

    list_str=''
    for n in t_matrix:
        list_str = list_str+' '.join(map(str, n))+'\n'
    
    print(list_str)

main()

