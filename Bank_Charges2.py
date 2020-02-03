#Bank charges with 20rs fee after 5 debit
money=0
count=1
for trans in range(1,11):
       decision=input("Enter what operation you want to perform withdraw or deposit:")
       if decision=="deposit":
              deposit=int(input("Enter the amount you want to deposit"))
              money+=deposit
              print("Current balance:",money)
       else:
              if money!=0:
                     if count<=5:
                            withdraw=int(input("Enter the amount you wish to withdraw"))
                            if withdraw<(money):
                                   money-=withdraw
                                   print("Current balance:",money)
                            else:
                                   print("U are collecting the entire amount i.e",money,"rs")
                                   money=0
                                   print("Current Balance:",money)
                            count+=1
                     
                     else:
                            print("Due to more than 5 times of withdraw ur charged with 20 rs")
                            withdraw=int(input("Enter the amount you want to withdraw"))
                            if withdraw<(money+20):
                                   money-=withdraw+20
                                   print("Current balance:",money)
                            elif withdraw==(money+20):
                                   print("U are collecting the entire amount i.e",money,"rs")
                                   money=0
                                   print("Current Balance:",money)
                            else:
                                   print("No cash left hence lien charge")
                            count+=1

              else:
                     print("Sorry your account has no balance so u cannot perform withdraw operation")


