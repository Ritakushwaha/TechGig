'''
Lets make a dictionary order (100 Marks)
You need to input N words one on each line and output should be lexicographically sorted i.e the words which comes as a output should be alphabetically sorted

Input Format
You will be taking an integer N from STDIN.
Following N lines contains string one on each line.

Constraints
1 < N < 10000
1 < |S| < 1000


Output Format
The words should be lexicographically sorted and should be displayed one per each line.

'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

    n = int(input())
    list_ = []
    for i in range(0,n):
        list_.append(input())
        list_ = sorted(list_)

    string = ''
    string = '\n'.join(map(str,list_))

    print(string)

main()

