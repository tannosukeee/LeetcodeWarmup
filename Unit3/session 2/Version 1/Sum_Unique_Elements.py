def sum_of_unique_elements(lst1, lst2):
	sum = 0
	for i in range(len(lst1)):
		if i + 1 < len(lst1) and lst1[i] not in lst2 and lst1[i] != lst1[i + 1]:
			sum += lst1[i]
	return sum

lstA = [1, 2 ,3, 4] 
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]

sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1)

sum2 = sum_of_unique_elements(lstC, lstB)
print(sum2)