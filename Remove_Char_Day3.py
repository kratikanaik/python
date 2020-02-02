def remove(str,start,num):
       str3=""
       str1=list(str)
       for all in range(0,num):
              for each in range(0,len(str)):
                     if each==start:
                            del str1[each]
                            break
       for i in str1:
              str3+=i
       print(str3)
str2=input("Enter the string:")
num=int(input("Enter the number of characters to be removed:"))
begin=int(input("enter the start point:"))
remove(str2,begin,num)
