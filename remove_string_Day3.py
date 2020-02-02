#remove vowels

def remove(string):
       vowels=('a','e','i','o','u')
       for a in string.lower():
              if a in vowels:
                     str=string.replace(a,"")
       print(str)
str=input("Enter a string")
remove(str)
