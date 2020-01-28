class Tryinit:
    #function_init_defined
    def __init__(sathiya,name,age):
        sathiya.name=name;
        sathiya.age=age;
    #self_parameter_defined
    def check(sathiya):
        print(sathiya.name)
        print(sathiya.age)
#object_Defined        
i1 = Tryinit("Sangar","19")
i1.age="20"
i1.check()