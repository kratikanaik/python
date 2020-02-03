#binary representation

def bin(num):
       if num>1:
              bin(num//2)
       print(num%2,end="")
if __name__=="__main__":
       print()
       bin(6)
