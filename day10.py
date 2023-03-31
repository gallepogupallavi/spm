'''#Built -in function-->60+ as of python3.x version
#print(dir(__builtins__))
#every built-in datatype is a built in function
#int(),float(),complex(),bool(),str(),list(),tuple()
#st(),dict()
a="codegnan"
#conert ti dict
b=dict.fromkeys(a)
print(b)
#print(len(b))__builtins__
#print(type(a))

#print(min(b))


#any(),all(),sorted(),reversed(),zip(),enumerate()
#any(itrable)-->checks for atleast one object
#similar to or

a=[1,2,'',[],25,3.2]
#print(len(a))
#print(any(a))
print(all(a))


a=(1,2,8,12,3,-5,6.3)
#sort the tuple
b=list(a)
#print(b)
b.sort()
print(b)

c=sorted(a)
print(c)
#print(sorted(a))
#descending order
sorted(a,reverse=True)
#print(d)
#zips(),enumerate()

#zip(*iterble)-->convers multipule collectns into
#a single iterable

a=[1,5,8,9,12];b=[1,8,12]
c=list(zip(a,b))
print(c)

data=[121,125,135,128]
names=['uma','indra','honey','eanimies']
new=dict(zip(data,names))
print(new)
#print(new)'''
'''
e=lambda x,y:x**y
print(e(5,2))

f=lambda fname,Iname:fname+''' '''+Iname
print(f("honey","harini"))

#filter()-->return a new collection after perform
#rwqd logic
a=[int(x) for x in input("enter").split(',')]
print(a)'''
'''
a






























     
