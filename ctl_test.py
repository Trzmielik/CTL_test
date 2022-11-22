from random import random
import matplotlib.pyplot as plt

n_bins=30
n_values=10000
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

if __name__ == "__main__":
    n_bits=input("How many bars do you want to have in histogram?")
    sequence=list_of_random_in_distribution(n_bins*n_values)
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
    plt.hist(means_2,label="of 2",bins=n_bins)
    plt.hist(means_5,label="of 5",bins=n_bins)
    plt.hist(means_10,label="of 10",bins=n_bins)
    plt.legend()
    plt.title("Histograms of means: ")
    plt.show()
