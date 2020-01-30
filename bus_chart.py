#Bus chart
chart=""
for row in range(1,8):
       for seat in range(1,5):
              amt=int(input("Tell us the amount u have"))
              if(amt>=500):
                     print("Ur seat is confirmed i.e row:",row,"and seat",seat)
                     chart+='$'
              else:
                     print("sorry ur seat is not booked")
                     chart+='%'
       chart+='\n'
print(chart)
