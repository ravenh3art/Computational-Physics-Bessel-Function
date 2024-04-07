from numpy import *
from math import *
from matplotlib import *
from scipy.integrate import *
from scipy.special import *
from pylab import *
print("The diffraction limit of a telescope")

a=float(input("From:"))
b=float(input("To:"))
m=int(input("M:"))
y1=int(input("y1:"))
y2=int(input("y2:"))
#allows user to customize the definite integral
if a>b:
    print("The integral will be negative")
N=int(input("Number of Slices:"))
#user inputs the slices
h=(b-a)/N
y=(y2-y1)/N
def f(x,y):
    return cos(m*x-y*sin(x))
#defines the function
inte=0
for k in range(1,N):
    inte+=f(a+h/2+k*h,y1+h/2+k*h)*h
#the coding equivalent to the sum function for the riemman sum using a for loop to iterate
xlist=linspace(-100,100,num=100)
xlist=arange(-10,10,.1)

ylist=f(xlist,y)
figure(num=0,dpi=120)
plot(xlist,ylist)
show()
print("The Diffraction Limit is:",inte*1/pi)



print("With Simpson's Rule")
#whole function with simpson's rule is calculated here
def j(m,x):

    def f(thet):
        return cos(m*thet-x*sin(thet))

    inte2=f(a)+f(b)+4*f(b-h)

    for k in range(1,N//2):
        inte2+=4*f(a+(2*k-1)*h)+2*f(a+2*k*h)
#loops to the endpoint
    intewh=h/3*inte2/pi

    return intewh

xlist2=linspace(0,30)

plot(xlist2,j(0,xlist2),label='J0')
plot(xlist2,j(1,xlist2),label='J1')
plot(xlist2,j(2,xlist2),label='J2')
show()
#parameters to make the graph
print("With integration Function")
#with sci.py integration function
fulinteg=dblquad(f,a,b,y1,y2)

print(fulinteg)

print("With Bessel Function")
#bessel function 
zetalist=linspace(a,b,N)
for t in range(1,N//2):
    plot(zetalist,jv(t,zetalist))

show()