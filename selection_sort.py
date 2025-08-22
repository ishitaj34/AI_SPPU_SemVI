arr = []
n = int(input("Enter the number of elements: "))

for i in range(n):
	element = int(input("Enter an element: "))
	arr.append(element)
	
print("\nArray before sorting: ")
print(arr)

def selection_sort():
	for i in range(0, n):
		minIndex = i
		for j in range(i + 1, n):
			if arr[j] < arr[minIndex]:
				minIndex = j
		arr[i], arr[minIndex] = arr[minIndex], arr[i]
		
selection_sort()

print("\nArray after sorting: ")
print(arr)
