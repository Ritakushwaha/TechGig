''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    p = float(input())
    r = int(input())
    t = int(input())

    simple_interest = (p*t*r)/100
    print(round(simple_interest))

main()
