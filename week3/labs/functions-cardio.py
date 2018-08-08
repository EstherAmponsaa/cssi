def longest_word(w1,w2,w3):
    l1 = len(w1)
    l2 = len(w2)
    l3 = len(w3)
    if l1 > l2 and l1 > l3:
        print l1
    elif l2 > l1 and l2 > l3:
        print l2
    else:
        print l3

longest_word('hello','pie','do')



aword = "hello!"
def reverse_string(aword):
    s = ""
    for i in range(len(aword),0,-1):
        s =s + aword[i-1]
    print s

reverse_string(aword)

def sum_to_n(n):
    total = 0
    for i in range(1,n+1):
        total = total + i
    return total
def is_triangle(a,b,c):
    sabc = a+b > c
    sacb = a+c > b
    sbca = b+c > a
    if sabc and sacb and sbca:
        return True
    else:
        return False    
