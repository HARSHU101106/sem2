#1.
''import sys
a=[1,2,3,4,5]
ref=sys.getrefcount(a)
print("reference count=",ref)

import sys
a=[]  #count==2
b=a #now count--3
c=b # now count==4
ref=sys.getrefcount(a)
print("reference count=",ref)

import gc
gc.enable()
gc.disable()
l1=[1,2,3]
d1={'a':1,'b':2}
s1="Garbage Collection"
del l1
del d1
del s1
gc.set_threshold(100,5,5)  #100-- short lived 5--medium lived 5--lived for long time
print('current threshold is :',gc.set_threshold())
collected=gc.collect()
print(f"Garbage Collector collected {collected} objects")