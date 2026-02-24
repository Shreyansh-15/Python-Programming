"""Basic Arithmatic Operations."""

class basic():
    def __init__(self,a,b):
        self.a = a
        self.b = b 

    def add(self):
        return(self.a + self.b)
    
    # def add(a, b):
    #     return a+b
    
    def sub(self):
        return(self.a - self.b)
    
    # def sub(a, b):
    #     return a-b
    
    def mul(self):
        return(self.a * self.b)
    
    def div(self):
        return(self.a / self.b)