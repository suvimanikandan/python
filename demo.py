

#f=open('mydata','r')

#print(f.read())

#print(f.readlines())

#print(f.readline())

#f1=open('abc','w')
#f1.write("laptop")

f=open('6.jpg','rb')

f1=open('mypic.jpg','wb')

for i in f:
    f1.write(i)
