def plainFunc(a,b,c):
	print "a: %s"% a
	print "b: %s"% b
	print "c: %s"% c

def variableArgs(*args, **kwargs):
    for value in args:
        print "%s" % value
    for key, value in kwargs.iteritems():
        print "%s == %s" %(key,value)