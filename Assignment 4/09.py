class pair:

	def __init__(self,array,target):

		self.array=array
		self.target=target

	def findpairs(self):

		length=len(array)

		for i in range(length):

			for j in range(i+1,length):

				if self.array[i]+self.array[j]==self.target:

					print("Indices Found Of Target : ",i,j)


array=[1,2,3,4,5]
target=6
p1=pair(array,target)

p1.findpairs()