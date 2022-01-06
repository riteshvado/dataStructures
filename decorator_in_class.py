#Example of writing decorator function inside class.
class A():
    def __init__(self,a=10):
        self.a=a
    
    ##Standalone function inside. The function can be just outside as well. 
    def _decorate(func):
        ##See below how decorator is manipulating instance variable . This can be needed in some cases. 
        def wrapper(*args,**kwargs):
            ##args[0] will get you value self 
            ##args[1] will get you self
            
            print(args)
            ##Getting instance var value 
            print(args[0].a)
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



