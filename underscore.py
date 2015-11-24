#from pudb import set_trace; set_trace()
import random 
from IPython.lib.deepreload import reload as dreload

# building blocks: map, and find (that doesn't iterate through the whole list) 

def each (array, func):
	map(func, array)
	return array

def reduceRight (array, func, initial=None):
	if not array:
		return initial
	elif len(array)==1 and initial==None:
		return array[0]
	else:
		return func(reduceRight(array[1:], func, initial), array[0])


def find (array, func):
	if (len(array) == 0): # no more elements left in list
		return None
	elif (func(array[0])): # element passes truth test 
		return array[0]
	else: # recursive case
		return find(array[1:], func)

def filter (array, func):
	return reduce(lambda a,x: a+[x] if func(x) else a, array, [])

def where (array, properties):
	return filter(array, lambda record: filter(properties.items(), lambda x: \
		x[0] in record and record[x[0]] == x[1]) == properties.items())

def findWhere (array, properties):
	return find(array, lambda record: filter(properties.items(), lambda x: \
		x[0] in record and record[x[0]] == x[1]) == properties.items())

def reject (array, func):
	return reduce(lambda a,x: a+[x] if not func(x) else a, array, [])


def every(array, test):
	return reduce(lambda a,x: a and test(x), array, True)

def some(array, test):
	return reduce(lambda a,x: a or test(x), array, False)

def contains(array, value, from_index = 0):
	return reduce(lambda a,x: a or x==value, array[from_index:], False)

def invoke(array, func, *args):
	return map(lambda x:func(x,*args), array)

def pluck(array, property_name):
	return map(lambda x:x.get(property_name), array)

def max(array, selector):
	return reduce(lambda a,x: a if selector(a)>selector(x) else x, array)

def augmented_map(array, func):
	return map(lambda x: {'value':x, 'key': func(x)},array)

# get Mary to code view this
def groupBy(array, func):
	array_with_keys = augmented_map(array, func)
	def grouper(a,x):
		key = x.get('key')
		if a.get(key)==None:
			a[key] = []
		a[key].append(x.get('value'))
		return a

	return reduce(grouper,array_with_keys,{})

# ARRAYS###

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

# FUNCTIONS ###

def negate(test):
	return lambda x: not test(x)

def wrap(func, wrapper):
	return lambda : wrapper(func)

def compose(*funcs):
	return reduceRight(funcs[:-1], lambda a, f: lambda *args, **kwargs: f(a(*args, **kwargs)), funcs[-1]) if funcs else lambda *args: args
	'''
	def returning(a, f):
		def inner(*args, **kwargs):
			return f(a(*args, **kwargs))
		return inner

	if not funcs:
		return lambda *args: args
	else:
		return reduceRight(funcs[:-1], returning, funcs[-1])
	'''

data = [1,2,3,4,5]
data_arrays = [[2,1,3,4],[4,2,5],[1,2,1]]

records = [{'name':'Lauren', 'gender': 'f', 'age':'1'}, {'name':'Ben', 'gender': 'm', 'age':'5'},{'name':'Lauren', 'gender': 'f', 'lname': 'long', 'age':'4'} ]
properties = {'name':'Lauren', 'gender': 'f'}
func1 = lambda x: x<10
func2 = lambda x: x==3
func3 = lambda x: x%2 ==0
func4 = lambda x: x>10
func5 = lambda x,y: x+y
func6 = lambda x,y,z: x+y+z
wrapper = lambda func: func()+"hello"
#result = find(data, filter_func)
#print (result)

greet    = lambda name:"hi: " + name
exclaim  = lambda statement: statement.upper() + "!"
welcome = compose(greet, exclaim);
welcome('moe');


negFunc1 = negate(func1)
negFunc1(data)

