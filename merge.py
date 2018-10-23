def merge_lists(left_sublist,right_sublist):
	i,j = 0,0
	result = []
	while i<len(left_sublist) and j<len(right_sublist): #iterate through both left and right sublist
		
		if left_sublist[i] <= right_sublist[j]:#if left value is lower than right then append it to the result
			result.append(left_sublist[i])
			i += 1
		else:
			
			result.append(right_sublist[j])#if right value is lower than left then append it to the result
			j += 1
	
	result += left_sublist[i:] #concatenate the rest of the left and right sublists
	result += right_sublist[j:]
	
	return result #return the result

def merge_sort(input_list):
	
	if len(input_list) <= 1: #if list contains only 1 element return it
		return input_list
	else:
		
		midpoint = int(len(input_list)/2) #split the lists into two sublists and recursively split sublists
		left_sublist = merge_sort(input_list[:midpoint])
		right_sublist = merge_sort(input_list[midpoint:])
		
		return merge_lists(left_sublist,right_sublist) #return the merged list using the merge_list function above


#test
number_list = [int(input("enter number:")) for i in range (10)]
print("the list is" ,number_list)
print("after sorting", merge_sort (number_list))
