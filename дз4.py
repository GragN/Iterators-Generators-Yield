nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


class FlatIterator:

	def __init__(self, list1, n=0, n1=-1):
		self.list1 = list1
		self.n = n
		self.n1 = n1

	def __iter__(self):
		return self

	def __next__(self):
		if len(nested_list[self.n])-1 != self.n1:
			self.n1 += 1
			return nested_list[self.n][self.n1]
		elif len(nested_list) - 1 == self.n:
			raise StopIteration
		else:
			self.n1 = 0
			self.n += 1
			return nested_list[self.n][self.n1]


for item in FlatIterator(nested_list):
	print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)


def flat_generator():
	for i in nested_list:
		for j in i:
			yield j


for i in flat_generator():
	print(i)