# get and print the string in X format

for row in range(7):
       for col in range(7):
              if row==0 and col==0 or row==0 and col==6:
                     print("a",end="")
              elif row==1 and col==1 or row==1 and col==5:
                     print("n",end="")
              elif row==2 and col==2 or row==2 and col==4:
                     print("d",end="")
              elif row==3 and col==3:
                     print("r",end="")
              elif row==4 and col==2 or row==4 and col==4:
                     print("o",end="")
              elif row==5 and col==1 or row==5 and col==5:
                     print("i",end="")
              elif row==6 and col==0 or row==6 and col==6:
                     print("d",end="")
              else:
                     print(end="")
       print()
