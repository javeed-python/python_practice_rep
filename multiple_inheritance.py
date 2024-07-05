class A:
    # define properties
    a_prop_1 = "a_val1"
    a_prop_2 = "a_val2"

    def __init__(self):
        print("class A object created")

    # define methods
    def a_method_1(self):
        print("this is a_method_1")

    def a_method_2(self):
        print("this is a_method_2")

    def details(self):
        print(f"details of class A: {self.a_prop_1}, {self.a_prop_2}")


class B:
    # define properties
    b_prop_1 = "b_val1"
    b_prop_2 = "b_val2"

    def __init__(self):
        print("class B object created")

    # define methods
    def b_method_1(self):
        print("this is b_method_1")

    def b_method_2(self):
        print("this is b_method_2")

    def details(self):
        print(f"details of class B: {self.b_prop_1}, {self.b_prop_2}")


class C(A, B):
    # define properties
    c_prop_1 = "c_val1"
    c_prop_2 = "c_val2"

    def __init__(self):
        print("class C object created")

    # define methods
    def c_method_1(self):
        print("this is c_method_1")

    def c_method_2(self):
        print("this is c_method_2")

    def details(self):
        print(f"details of class C: {self.c_prop_1}, {self.c_prop_2}")

# object of class C should be able to access all the members of class A & B parent classes
c_obj = C()
print("accessing properties with c_obj:", c_obj.a_prop_1, c_obj.a_prop_2, c_obj.b_prop_1, c_obj.b_prop_2,
      c_obj.c_prop_1, c_obj.c_prop_2)
print("accessing methods with c_obj")
c_obj.a_method_1()
c_obj.b_method_1()
c_obj.c_method_1()

# when parent class methods are same as derived class,
# then derived member will be called, i.e C class details() method is called
c_obj.details()

