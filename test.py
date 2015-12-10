from underscore import *

data = [1,2,3,4,5]
data_arrays = [[2,1,3,4],[4,2,5],[1,2,1]]

records = [{'country':'Canada', 'capital': 'Ottawa'}, {'country':'USA', 'capital': 'DC', 'continent':'NA'}]
properties = {'country':'Canada', 'capital': 'Ottawa'}
func1 = lambda x: x<10
func2 = lambda x: x==3
func3 = lambda x: x%2 ==0
func4 = lambda x: x>10
func5 = lambda x,y: x+y

def extraparam (x,a,b):
	return x+a-b
	
wrapper = lambda func: func()+"hello"
#result = find(data, filter_func)
#print (result)

greet    = lambda name:"hi: " + name
exclaim  = lambda statement: statement.upper() + "!"
welcome = compose(greet, exclaim);
welcome('moe');


negFunc1 = negate(func1)
negFunc1(data)