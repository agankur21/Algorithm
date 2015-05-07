import sys

def sortAndCountInversion(input):
	if (len(input) == 1):
		return  (input,0)
	else:
		middle = int(len(input)/2) ;
		(leftSortInput,lCount) = sortAndCountInversion(input[:middle])	
		(rightSortInput,rCount) = sortAndCountInversion(input[middle:])
		(mergedArray, splitInversionCount) = mergeAndCountInversion(leftSortInput,rightSortInput)
		return ((mergedArray, lCount+ rCount + splitInversionCount))

def mergeAndCountInversion(leftSortInput,rightSortInput):
	mergedArray = []
	leftIndex,rightIndex,numInversions = 0,0,0
	totalLength = len(leftSortInput) + len(rightSortInput)
	for i in range(totalLength):	
		if (((leftIndex < len(leftSortInput) and (rightIndex < len(rightSortInput))) and (leftSortInput[leftIndex] <= rightSortInput[rightIndex])) or (rightIndex >= len(rightSortInput))):
			mergedArray.append(leftSortInput[leftIndex])
			leftIndex += 1
		elif (((leftIndex < len(leftSortInput) and (rightIndex < len(rightSortInput))) and (leftSortInput[leftIndex] > rightSortInput[rightIndex])) or (leftIndex >= len(leftSortInput))):
			mergedArray.append(rightSortInput[rightIndex])
			rightIndex += 1
			numInversions  += (len(leftSortInput) - leftIndex)
	return (mergedArray,numInversions)			
			
	
if __name__ == "__main__":
	inputArray =  sys.argv[1:]
	(sortedArray,numInversions) = sortAndCountInversion(inputArray)
	print("Number of Inversion: %s" %numInversions)		
	print("Sorted Array : " + str(sortedArray))
			



