import random, inspect, copy
from collections import defaultdict

### ARRAY FUNCTIONS ###

def each (array, func):
	map(array, func)
	return array

def map(array, func):
	# Func has arguments(element, index, array), 
	# The last two are optional
	def helper(accum, elem, index, array):
		numArgs = len(inspect.getargspec(func).args)
		if (numArgs==1):
			args = (elem,)
		elif (numArgs==2):
			args = (elem, index)
		elif (numArgs==3):
			args = (elem, index, array)
		else:
			raise ValueError("Function has wrong number of parameters")
		return accum + [func(*args)]

	return reduce(array, helper, [])

def reduce(array, func, initial=None):
	# Func has arguments(accumulatedResult, elem, index, array)
	# The last two are optional

	numArgs = len(inspect.getargspec(func).args)

	if (initial == None):
		accum = array[0]
		newArray = array[1:]
	else:
		accum = initial
		newArray = array

	for i, elem in enumerate(newArray):
		if (numArgs==2):
			args = (accum, elem)
		elif (numArgs==3):
			args = (accum, elem, i)
		elif (numArgs==4):
			args = (accum, elem, i, newArray)
		else:
			raise ValueError("Function has wrong number of parameters")
		accum = func(*args)

	return accum
		 
def reduceRight(array, func, initial=None):
	# Func has arguments(accumulatedResult, elem)
	backwards = reduce(array, lambda a,x:[x]+a, [])
	return reduce(backwards, func, initial)

def find (array, test):
	if array: 
		if (test(array[0])): # element passes truth test 
			return array[0]
		else: # recursive case
			return find(array[1:], test)

def filter (array, test):
	return reduce(array, lambda a,x: a+[x] if test(x) else a, [])

def where (array, properties):
	return filter(array, lambda record: filter(properties.items(), lambda x: \
		x[0] in record and record[x[0]] == x[1]) == properties.items())

def findWhere (array, properties):
	return find(array, lambda record: filter(properties.items(), lambda x: \
		x[0] in record and record[x[0]] == x[1]) == properties.items())

def reject (array, test):
	return reduce(array,lambda a,x: a+[x] if not test(x) else a, [])

def every(array, test):
	return reduce(array, lambda a,x: a and test(x), True)

def some(array, test):
	return reduce(array, lambda a,x: a or test(x), False)

def contains(array, value, from_index = 0):
	return reduce(array[from_index:], lambda a,x: a or x==value, False)

def invoke(array, func, *args, **kwargs):
	return map(array, lambda x:func(x,*args, **kwargs))

def pluck(array, property_name):
	return map(array, lambda x:x.get(property_name))

def max(array, criteria = lambda x:x):
	return reduce(array, lambda a,x: a if criteria(a)>criteria(x) else x)

def min(array, criteria = lambda x:x):
	return reduce(array, lambda a,x: x if criteria(a)>criteria(x) else a)

def sortBy(array, criteria = lambda x:x):
	if (len(array) == 1):
		return array
	middle = len(array)/2
	left  = sortBy(array[:middle], criteria)
	right = sortBy(array[middle:], criteria)
	def merge(left, right, criteria):
		if len(left)  == 0:
			return right
		if len(right) == 0:
			return left
		if criteria(left[0]) <= criteria(right[0]):
			return [left[0]] + merge(left[1:], right, criteria)
		if criteria(right[0]) < criteria(left[0]):
			return [right[0]] + merge(left, right[1:], criteria)

	return merge(left, right, criteria)

def groupBy(array, criteria):
	def grouper(a,x):
		key = criteria(x)
		a[key].append(x)
		return a
	return reduce(array, grouper, defaultdict(list))

def countBy(array, criteria):
	def counter(a,x):
		key = criteria(x)
		if a.get(key)==None:
			a[key]=0
		else:
			a[key]+=1
		return a
	return reduce(array, counter, {})

def shuffle(array, index=0):
	if index==len(array):
		return array

	copied = copy.deepcopy(array)
	swapWith = random.randint(index, len(array)-1)

	temp = copied[swapWith]
	copied[swapWith] = copied[index]
	copied[index] = temp

	return shuffle(copied, index+1)

def sample(array, n):
	if len(array) < n:
		return []
	elif n==0:
		return []
	else:
		picked_index = random.randint(0, len(array)-1)
		picked = [array[picked_index]]
		cleaned_array = array[0:picked_index] + array[picked_index+1:]
		return picked + sample(cleaned_array, n-1)

def size(array):
	return len(array)

def partition(array, test):
	return [filter(array, test),filter(array, negate(test))]

### HIGHER ORDER FUNCTIONS ###
 
def wrap(func, wrapper):
	return lambda : wrapper(func)

def negate(test):
	return lambda x: not test(x)

def compose(*funcs):
	def returning(a, f):
		def inner(*args, **kwargs):
			return f(a(*args, **kwargs))
		return inner

	if not funcs:
		return lambda *args: args
	else:
		return reduceRight(funcs[:-1], returning, funcs[-1])

### FOR FUN ###

def reduceRecursive(array, func, initial=None):
	# Func has arguments(accumulatedResult, elem)
	if not array:
		return initial
	elif len(array)==1 and initial==None:
		return array[0]
	else:
		return func(reduceRecursive(array[:-1], func, initial), array[-1])

def reduceRightRecursive (array, func, initial=None):
	# Func has arguments(accumulatedResult, elem)
	if not array:
		return initial
	elif len(array)==1 and initial==None:
		return array[0]
	else:
		return func(reduceRightRecursive(array[1:], func, initial), array[0])

