import os  
#path=input("enter valid path")  
#while(True):  
#    if(os.path.isdir(path)):  
#      break  
#    else:  
#      print("please enter a valid path ") 
path="/Users/maheritc/python"
for root,dirs,files in os.walk(path):  
 for name in files:  
  filename=os.path.join(root,name)  
  if os.stat(filename).st_size==0:  
   print(" Removing ",filename)  
   os.remove(filename) 
