def minIndex( a , i , j ):
	if i == j:
		return i
	k = minIndex(a, i + 1, j)
	
	return (i if a[i] < a[k] else k)
	
def recurSelectionSort(a, n, index = 0):

	if index == n:
		return -1
		
	k = minIndex(a, index, n-1)
	
	if k != index:
		a[k], a[index] = a[index], a[k]
		
	recurSelectionSort(a, n, index + 1)
	
arr = [3, 1, 5, 2, 7, 0]
n = len(arr)

recurSelectionSort(arr, n)

for i in arr:
	print(i, end = ' ')
	