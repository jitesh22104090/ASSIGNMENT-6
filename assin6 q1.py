def perfnum(n):
    lst=[]
    for i in range(1,n):
        if n%i==0:
            lst.append(i)
    if n>0 and (sum(lst)==n or (sum(lst))/2==n):
        print("Perfect number")
    else:
        print("Not perfect number")
n=int(input("Enter a number: "))
perfnum(n)