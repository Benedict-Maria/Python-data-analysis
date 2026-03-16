import numpy as np
import matplotlib.pyplot as plt

arr=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr,"\n")

#size=total number of elements
print("Size:",arr.size,"\n")

#shape=rows and columns
print("Shape:",arr.shape,"\n")

#dtype=datatype of the elements
print("datatype:",arr.dtype,"\n")

#Transpose = elements in rows and columns are interchanged
print("Transpose:\n",arr.transpose())
print("Transpose Shape:\n",arr.transpose().shape)

#np.empty((rows,cols),dtype)
print("\nEmpty(int):",np.empty((5,5),dtype=int))
print("\nEmpty(string):",np.empty((5,5),dtype=str))
print("\nEmpty(boolean):",np.empty((5,5),dtype=bool=))

#np.ones
print("\nOnes:",np.ones(6))
print("\nOnes(int):",np.ones((3,5),dtype=int))
print("\nOnes(string):",np.ones((3,5),dtype=str))
print("\nOnes(boolean):",np.ones((3,5),dtype=bool))

#np.zerosprint("\nZeros:",np.zeros(3))
print("\nZeros(int):",np.zeros((2,4),dtype=int))
print("\nZeros(string):",np.zeros((2,4),dtype=str))
print("\nZeros(boolean):",np.zeros((2,4),dtype=bool))

#np.arange(start,end,step)
a=np.arange(1,20)
print("\narange(without step):",a)
a=np.arange(2,20,2)
print("\narange(with step):",a)

#arr.reshape((rows,cols))
a=a.reshape((3,3))
print("\nReshape:",a)
b=np.arange(1,100,2)
print("\narange:",b)
b=b.reshape((10,5))
print("\nReshape:",b)

#arr.flatten()--->return copy of the original array, if you modify the array , the value of original array not changes
print("\nFlatten:",b.flatten())

#arr.ravel()--->return only reference/view of original array. if you modify the array , the value of original array also changes
print("\nRavel:",a.ravel())

#slicing
a=np.arange(1,51)
a=a.reshape(10,5)
print("\na=",a)

print("\na[0]:",a[0])
print("\na[2]:",a[2])
print("\na[0,0]:",a[0,0])
print("\na[3,4]:",a[3,4])

print("\na[2:4]:",a[2:4])
print("\na[:,4]:",a[:,4])
print("\na[0:2,4]:",a[0:2,4])
print("\na[:,:]=",a[:,:])
print("\na[:,1:3]=",a[:,1:3])
print("\na[:,:].dtype()=",a[:,:].dtype)

#MATHEMATICAL OPERATIONS
a=np.arange(0,18).reshape((6,3))
b=np.arange(20,38).reshape((6,3))
print("\na=",a)
print("\nb=",b)

print("\na+b=",a+b)  #or np.add(a,b)
print("\na-b=",a-b)  #np.subtract(a,b)
print("\na*b=",a*b)  #np.multiply(a,b)
print("\na/b=",a/b)  #np.divide(a,b)

b=b.reshape((3,6))    #to perfom dot product , column of 1st matrix and row of 2nd matrix should be identical
print("\na@b=",a@b)     #dot product           or a.dot(b)
print("\nMax of b:",b.max())
print("\nMin of a:",a.min())
print("\nargmax():",b.argmax())    #argmax()---> gives index of max element of the array
print("\nSum:",b.sum())
print("\n",np.sum(b,axis=1))     # axis=1-->specifies rows     axis=0---->specifies columns
print("\n",np.sum(b,axis=0))
print("\nMean:",np.mean(a))
print("\nSquare root:",np.sqrt(b))
print("\nStandard Deviation:",np.std(b))
print("\nLogarithm:",np.log(b))

#TRIGNOMETRY FUNCTIONS
print("\nnp.pi:",np.pi)
print("\nnp.sin()=",np.sin(np.pi/2))   #90 degrees
print("\n",np.sin(np.pi/6))     #30 degrees
print("\nnp.cos():",np.cos(np.pi/2))
print("\n",np.cos(np.pi/6))
print("\nnp.tan():",np.tan(np.pi/2))
print("\n",np.tan(0))

#random() operaations
print("\nRandom:",np.random.random(1))
print("\nRandom:",np.random.random(2))
print("\nRandom:",np.random.random((2,2)))

print("\nRandint:",np.random.randint(1,10))
print("\nRandint:",np.random.randint(1,10,(2,2)))
print("\nRandint:",np.random.randint(1,20,(3,3,3)))

print("\nRand:",np.random.rand(1,2))
print("\nRandn:",np.random.randn(2,3))   #randn()-->negative values too

a=np.arange(1,11)
print("\na=",a)
print("\nchoice():",np.random.choice(a))

#STRING OPERATIONS
s1='Mani is my pet. '
s2='Mani is very Cute'
print("\nConcatenate:",np.char.add(s1,s2))
print("\nUpper:",np.char.upper(s1))
print("\nLower:",np.char.lower(s2))
print("\nSplit:",np.char.split(s1))

s3='Mani is\nmy pet. '
print("\nSplitlines:",np.char.splitlines(s3))
print("\nReplace:",np.char.replace(s1,'pet','friend'))
print("\n",np.char.center('THANK YOU',125,'-'))

#USING MATPLOTLIB WITH NUMPY
plt.style.use('dark_background')
x=np.arange(1,11)
y=np.arange(10,110,10)
plt.figure(figsize=(6,6))
plt.plot(x,y,'g--')
plt.show()

#plotting trignometric curves
x_sin=np.arange(0,2*np.pi,0.1)
y_sin=np.sin(x_sin)
print("\ny=",y_sin)
plt.figure(figsize=(6,6))
plt.plot(x_sin,y_sin)
plt.title("Sine Curve")
plt.show()

x_cos=np.arange(0,2*np.pi,0.1)
y_cos=np.cos(x_cos)
print("\ny=",y_cos)
plt.figure(figsize=(6,6))
plt.plot(x_cos,y_cos)
plt.title("Cosine Curve")
plt.show()

x_tan=np.arange(0,2*np.pi,0.1)
y_tan=np.tan(x_tan)
print("\ny=",y_tan)
plt.figure(figsize=(6,6))
plt.plot(x_tan,y_tan)
plt.title("Tangent Curve")
plt.show()

x_cot=np.arange(0,2*np.pi,0.1)
y_cot=1/np.tan(x_cot)
print("\ny=",y_cot)
plt.figure(figsize=(6,6))
plt.plot(x_cot,y_cot)
plt.title("Cot Curve")
plt.show()

#SUBPLOTS
plt.figure(figsize=(6,6))

plt.subplot(2,2,1)
plt.plot(x_sin,y_sin,'r-')
plt.title("Sine Curve")

plt.subplot(2,2,2)
plt.plot(x_cos,y_cos,'b-')
plt.title("Cosine Curve")

plt.subplot(2,2,3)
plt.plot(x_tan,y_tan,'g-')
plt.title("Tangent Curve")

plt.subplot(2,2,4)
plt.plot(x_cot,y_cot,'w-')
plt.title("Cot Curve")

plt.show()

























