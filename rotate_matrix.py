'''Rotate matrix
Given an image represented by an NxN matrix write a method to rotate the image by 90 degrees
'''
import numpy

theMatrix = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(theMatrix)

def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::1])
    return [list(elem) for elem in list_of_tuples]
    # return map(list, list_of_tuples)

print(numpy.array(rotated(theMatrix)))


#print(theMatrix)
def rotate_image(array):
	newMatrix = numpy.array([])
	#newMatrix.shape = (3, 3)	
	j = 0
	for i in array:

		newMatrix = numpy.insert(newMatrix, 0, list(i), axis = 0)
		newMatrix.tolist()

	return newMatrix
print(rotate_image(theMatrix))

print('-----------')

print(theMatrix.transpose())

