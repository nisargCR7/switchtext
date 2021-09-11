def swapFileData():
  
  f1=input('data from')   
  with open(f1,'r') as a1:
      data_a=a1.read()
  
  f2=input('data to')   
  with open(f2,'r') as a2:
        data_b=a2.read()

  with open(f1,'w') as a1:
      a1.write(data_b)
    
  with open(f2,'w') as a2:
      a2.write(data_a)
        
  print('done')

swapFileData()