#Example of writing decorator function inside class.
class A():
    def __init__(self,a=10):
        self.a=a
    
    ##Standalone function inside. The function can be just outside as well. 
    def _decorate(func):
        def wrapper(*args,**kwargs):
            print(args)
            print(kwargs)
            if kwargs.get('t') == 'egg':
                kwargs['t']='Omlette'
            return func(*args,**kwargs)
            
        return wrapper
        
    @_decorate
    def showA(self,b,t="GGG"):
        return [self.a*b,t]
        
        
a=A()
##Egg will change to 'Omlette' 
print(a.showA(12,t="egg"))



