class A:
    # define properties
    a_prop_2 = "a_val2"

    def __init__(self, val1):
        self.a_prop_1 = val1
        print("class A object created")

    # define methods
    def a_method_1(self):
        print("this is a_method_1")

    def details(self):
        print(f"details of class A: {self.a_prop_1}, {self.a_prop_2}")
class B:
    # define properties
    b_prop_2 = "b_val2"

    def __init__(self, val1):
        self.b_prop_1 = val1
        print("class B object created")

    # define methods
    def b_method_1(self):
        print("this is b_method_1")

    def details(self):
        print(f"details of class B: {self.b_prop_1}, {self.b_prop_2}")

class C(A,B):
    # define properties
    c_prop_1 = "c_val1"
    c_prop_2 = "c_val2"

    def __init__(self, a, b, c):
        self.c_prop_1 = c
        super().__init__(a)  # calls left most parent class constructor method
        print("class C object created")

    # define methods
    def c_method_1(self):
        print("this is c_method_1")

    def details(self):
        super().details()  # calls left most parent class details method
        print(f"details of class C: {self.c_prop_1}, {self.c_prop_2}")


print("going to create object for class C inherited from A & B")
c_obj = C(100, 200, 300)
print("accessing details() method with c_obj, where method definition is availabe classes in A, B & C")
c_obj.details()
print(C.__mro__)
