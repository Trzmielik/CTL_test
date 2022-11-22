from random import random
import matplotlib.pyplot as plt

def my_distribution(x,y):
    if x > -1.25 and x < 1.25:
        if y<=1:
            return x

    elif x > -1 and x < 1:
        if y<=0.25: 
            return x
        else: return -1


def mean(values):
    m=0
    if len(values) == 0: return 0
    for i in values:
       m=m+i 
    return m/len(values)
    
def list_of_random_in_distribution(n):
    lst = []
    while n>0:
        while True:
            x=(random()-0.5)*1.25
            y=random()
            val=my_distribution(x,y)
            if val!=-1:
                lst.append(val)
                break
            print(val)
        n=n-1
    return lst


sequence=list_of_random_in_distribution(10000)
means_2=[]
means_5=[]
means_10=[]
n=0
while n<len(sequence):
    means_2.append(mean(sequence[n:n+1]))
    n=n+2
n=0
while n<len(sequence):
    means_5.append(mean(sequence[n:n+4]))
    n=n+5
n=0
while n<len(sequence):
    means_10.append(mean(sequence[n:n+9]))
    n=n+10
plt.hist(means_2)
plt.hist(means_5)
plt.hist(means_10)
plt.show()
