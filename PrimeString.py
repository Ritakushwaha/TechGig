'''
A string S of lowercase letters will be provided and you have to figure out if the given string is Prime String or not.
Prime String: A string is considered a prime string only if the absolute difference between the sum of odd indexed letters and even indexed letters is completely divisible by any of the odd prime numbers less than 10.
Note: For calculations, consider the ASCII value of lowercase letters.
'''

n = int(input())

for i in range(n):
    s = input()
    i = 0
    even = 0
    odd = 0
    for char in s:
        if i % 2 == 0:
            even+=ord(char)
        else:
            odd+=ord(char)
        i+=1
            
    diff = abs(even-odd)
    
    if diff % 3 == 0 or diff % 5 == 0 or diff % 7 == 0:
        print("Prime String")
    else:
        print("Casual String")
