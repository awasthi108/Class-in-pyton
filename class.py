class A:
   def feature1(self):
      print("Feature 1 is working")


   def feature2(self):
      print("Feature 2 is working")

class B:
   def feature3(self):
      print("Feature 3 is working")
   def feature4(self):
      print("4 is also working")

class C(A,B):
   def function(self):
      print("5 is working")

a1=A()
a1.feature1()
a1.feature2()

b=B()
b.feature3()
b.feature4()


c=C()
c.function()

   
