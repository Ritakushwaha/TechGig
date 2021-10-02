'''
Patch Up Two Matrices (100 Marks)
For this challenge, you need to take 2 matrices as an input from the stdin , add them and print the resultant matrix to the stdout.

Input Format
Two matrices to be taken as an input. 
For each matrix, on first line you need to tell that how many rows and columns your matrix need to have and these values should be separated by space. 
Then after that, each line will represent will represent each row and you need to enter numbers which each rows should have separated by a space. 

Constraints
1 <  (n,m) < 100
1 <  (p,q) < 100

Output Format
Print the resultant matrix to the stdout where each each line should represent 
Note : Please do not include space after the numbers which are in the last column as it will affect your submission and you will not get marks. 
each row and values in the row should be separated by a space. 
'''

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

   
def inputs():
    row, col = map(int,input().split())
    matrix=[]
    for i in range(row):
        matrix.append(list(map(int, input().split())))
    return matrix

def main():
    matrix1 = inputs()
    matrix2 = inputs()
    matrix3=[]

    for t in zip(matrix1,matrix2):
        matrix3.append(list(map(lambda x,y:x+y,  t[0],t[1]))) 

    listToStr=''
    for n in matrix3:
        listToStr = listToStr+' '.join(map(str, n)) +'\n'
    
    print(listToStr)

main()

