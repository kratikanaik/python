
data={500:'Sony',450:'Sanddisk',550:'Hp'}
price=0

print(data)
def delete(start=0):
       price=int(input("enter the price u want to delete"))
       if data.get(price,"not exists"):
              del data[price]
              print(data)
              start+=1;
              if start>len(data)-1:
                     return
              delete()
       else:
              print("Doesnot exists")
              return
                     
delete()
