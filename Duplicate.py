data=[34,25,45,34,26,23]
start=0
def add(start):
       if start<=len(data):
              for i in range(0,len(data)-1):
                     if data[start]==data[i+1]:
                            data[start]=data[start-1]+10
                            data[i+1]=data[i]+10
              start+=1
              
add(0);
print(data)
