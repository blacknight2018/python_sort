#Python 学习第二天 18-10-10 冒泡排序
def swap(va,var,var2):
	va[var]  = va[var]+va[var2]
	va[var2] = va[var]-va[var2]
	va[var]  = va[var]-va[var2]
	return
list = [3,6,2,7,3,6,999,1,-2]
 

len = list.__len__()
print(list)
for k in range(0,len-1):
	for x in range(0,len-1):
		if(list[x]>list[x+1]):
			swap(list,x,x+1)
		 
print(list)
print("end")
