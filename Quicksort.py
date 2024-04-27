# This function takes first element as pivot, the function
# places the pivot element(first element) on its sorted
# position and all the element lesser than pivot will placed
# left to it, and all the element greater than pivot placed
# right to it.
def partition(array, low, high):

	# First Element as pivot
	pivot = array[low]
	
	# st points to the starting of array
	start = low + 1
	
	# end points to the ending of the array
	end = high

	while True:
		# It indicates we have already moved all the elements to their correct side of the pivot
		while start <= end and array[end] >= pivot:
			end = end - 1

		# Opposite process
		while start <= end and array[start] <= pivot:
			start = start + 1

		# Case in which we will exit the loop
		if start <= end:
			array[start], array[end] = array[end], array[start]
			# The loop continues
		else:
			# We exit out of the loop
			break

	array[low], array[end] = array[end], array[low]
	# As we got pivot element index is end
	# now pivot element is at its sorted position
	# return pivot element index (end)
	return end

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index
def quick_sort(array, start, end):

	# If low is lesser than high
	if start < end:
	
		# idx is index of pivot element which is at its
		# sorted position
		idx = partition(array, start, end)
		
		# Separately sort elements before
		# partition and after partition
		quick_sort(array, start, idx-1)
		quick_sort(array, idx+1, end)

# Function to print an array
def print_arr(arr, n):
	for i in range(n):
		print(arr[i], end=" ")
	print()

# Driver Code
arr1 = [7, 6, 10, 5, 9, 2, 1, 15, 7]
quick_sort(arr1, 0, len(arr1)-1)
print_arr(arr1, len(arr1))

# This code is contributed by Aditya Sharma
