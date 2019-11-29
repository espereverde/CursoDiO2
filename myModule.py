someVariable = 42

def someFunction(a, b):
    return a+b
    

class someClass:
    
    def __init__(self, value):
        
        self._value = value
        print(f'Initializing with {value}')
        
    def getValue(self):
        return value