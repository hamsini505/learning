#sum = 0
#sum1 = 0
#for i in range(1,1000):
#	if(i % 3 == 0 or i % 5 == 0):
#	   sum = sum + i
#print(sum)	  

 
limit = 1000	   
li = (set(range(3,limit,3)) | set(range(5,limit,5)))	   
print(sum(li))
