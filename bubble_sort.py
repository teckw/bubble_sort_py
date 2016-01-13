arr = []
import random

for num in range(0, 10):	# for loop for an array with 10 values
	random_num = round(random.random() * 10000) #random_num will generate random numbers * 10 to get whole values
	arr.append(random_num)	#add the random_num generated above to the array

for x in range(len(arr)):
	for i in range(len(arr)-1):					
		if arr[i] > arr[i + 1]:
				(arr[i], arr[i+1]) = (arr[i+1], arr[i]) # (a, b) = (b, a)	

print arr