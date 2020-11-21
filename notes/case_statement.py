''' What is Python's answer to the case-statement '''

def handle_keyerror(e):
	print 'Handling keyerror'

	
def handle_indexerror(e):
	print 'Handling indexerror'

	
def handle_valueerror(e):
	print 'Handling valueerror'
	
dispatch = {
	KeyError: handle_keyerror,
	IndexError: handle_indexerror,
	ValueError: handle_valueerror,
}

try:
	raise KeyError
except (KeyError, IndexError, ValueError) as e:
	dispatch[e.__class__](e)

	
Handling keyerror
try:
	raise IndexError
except (KeyError, IndexError, ValueError) as e:
	dispatch[e.__class__](e)

	
