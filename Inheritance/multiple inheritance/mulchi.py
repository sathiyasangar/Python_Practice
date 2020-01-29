from mulpar1 import Parent1
from mulpar2 import Parent2

class Child(Parent1, Parent2):  
    pass
ob = Child("Parent1 Success..!")
ob.show()
obs = Child("Parent2 Success..!")
obs.shown()
