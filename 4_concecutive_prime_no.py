#prime number
num=int(input("Enter the starting point:"))
term=int(input("Enter the number of terms u want:"))

prime=[]
for a in range(num,10000):
    for b in range(2,a):
        if(a%b==0):
            break
    else:
        prime.append(a)
    if len(prime)==term:
        break
print("prime numbers are:",prime[:])
