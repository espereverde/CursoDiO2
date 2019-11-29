otherVariable = 42

def otherFunction(a, b):
    return a+b
    

class otherClass:
    
    def __init__(self, value):
        
        self._value = value
        print(f'Initializing with {value}')
        
    def getValue(self):
        return value