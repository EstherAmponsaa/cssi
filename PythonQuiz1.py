 #1
 (a)
 x = int(raw_input("Enter a number "))
 y = int(raw_input("Enter another number "))

(b)
print("{0} + {1} = {2}".format(x,y,x+y))

(c)
print(str(x)+ "-" + str(y) + "=" +str(x-y))

(d)
print x,"*",y,"=",x*y

(e)
if y!=0:
    print "%s / %s = %s" %(x,y,x/y)

(f)
if y!=0:
    print "{o} % {1} = {2}".format(x,y,x%y)

#2
for i in range(1,101,1):
    if i % 3==0 and i % 5 ==0:
        print('FizzBuzz')
    elif i % 5==0:
        print('Buzz')
    elif i % 3==0:
        print('Fizz')
    else:
        print(i)            
