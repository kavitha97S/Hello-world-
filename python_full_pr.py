print("hello")
class a:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def display(self):
       print "value of x and y are ",self.x,self.y
ob=a(10,90)
ob.display()






def cal(x,y):
    c=x+y
    d=x-y
    e=x*y
    f=x/y
    return c,d,e,f
c,d,e,f=cal(2,4)
print "valuse ",c,d,e,f
class b(a):
    def __init__(self,x,y,z):
        a.__init__(self,x,y)
        self.z=z
    def disply(self):
        a.display(self)
        print "z value is ",self.z
ob1=b(1,2,3)
ob1.disply()

for i in range(0,10,2):
    print i 

l=["apple","mango","grape","orange"]
l.append("banana")
l.pop()
#del l
for i in l:
    print i
v=lambda a,b: a+b
print v(2,6)
l2=[i for i in l if "n" in i ]
print l2
    
