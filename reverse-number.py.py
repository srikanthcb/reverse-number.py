n=int(input())
if n>=0:
    while n>0:
        print(n%10,end='')
        n//=10
else:
    print('-',end='')
    n=n*-1
    while n>0:
        print(n%10,end='')
        n//=10