#reverse number
n=int(input("Enter a number:"))
r=0
while(n>0):
    num=n%10
    r=(r*10)+num
    n//10
    print("Reverse of the given number :",r)
