import random
a=int(input("Value of a coefficient: " ))
b=int(input("Value of b coefficient: " ))
c=int(input("Value of c coefficient: " ))
d=b*b-4*c*a
if(d == 0):
    xans=-b/(2*a)
    print("The solution is: "+ str(xans))
if(d > 0):
    xansone=(-b-(b^2-4*a*c)^1/2)/(2*a)
    xanstwo = (-b + (b ^ 2 - 4 * a * c) ^ 1 / 2) / (2 * a)
    print("The solution are: "+ str(xansone)+ " and " + str(xanstwo) )

#sortowanie
arr=range(0,50)
for k in range(0,50):
    arr[k]=random.randrange(1,100)
for i in range(0,50):
    for j in range(0,50-i-1):
        if(arr[j]<arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp



#Wektory iloczyn
a=[1,2,12,4]
b=[2,4,2,8]
c=range(0,4)
for m in range(0,4):
    c[m]=a[m]*b[m]
print(c)

#macierze
k=[[0 for x in range(128)] for y in range(128)]
w=[[0 for x in range(128)] for y in range(128)]
d=[[0 for x in range(128)] for y in range(128)]
for i in range(0,128):
    for j in range(0,128):
        k[j][i]=random.randrange(1,100)
        w[j][i]=random.randrange(1,100)
        d[j][i]=k[j][i]+w[j][i]

#multiplication of matrixes
x=int(input("Number of rows of A matrix: "))
y=int(input("Number of columns of A matrix: "))
z=int(input("Number of columns of B matrix: "))
k=[[random.randrange(1,10) for q in range(x)] for l in range(y)]
w=[[random.randrange(1,10) for e in range(y)] for h in range(z)]
d=[[0 for o in range(y)] for u in range(y)]
for i in range(0,len(k)):
    for j in range(0,len(w[0])):
        for q in range(0,len(w)):
            d[i][j]+=k[i][q]*w[q][j]
print(k)
print(w)
print(d)






#Determinant
A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
npDet = numpy.linalg.det(A)








