#crud mechanism for list type
#create
a=[2,233,"dinesh"]
b=list(range(9))
c="hii surya".split()
d=eval(input("enter list"))
e=["surya","surya","puli","pulli",["thar"],"puli","surya"]
g=["surya","puli","puli","thar","surya","surya"]
print(a)
print(b)
print(c)
print(d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
#read///
print(a)
print(a[2])#index
print(a[2:])#slice operator
for x in a:#fo loop
      print(x)
      
i=0
while i<=len(b)-1: #while loop
     print(b[i])
     i=i+1
a.reverse()#reverse
print(a)
      
print(e.count('puli'))#count rtuns no of occurencies of a specid element
print(e.count('thar'))
print(e.count('surya'))
      
f=e.copy()#copy
print(f)
      
g.sort()#sort
print(g)
      
print(len(g))
      
print(g.index("thar")) #it gives what is position of the value
      
      
#updatelist///
a.append(23)#append add element at end of the list
print(a)
      
a.insert(1,33)#insert method inserts elements at specifid position
print(a)
a.extend(g)#extent() mthod adds the specified list lements to end of current list
print(a)
     
      #delete list///
      
a.remove(233)#remov an element from list
print(a)
      
g.pop(2)#pop
print(g)
      
a.clear()#clear it delete all the elements in the list
print(a)
print(g)
del g#it gives rror because list dekted successfully
#print(g)
      
      
      
