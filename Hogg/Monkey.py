import numpy as np

n=100000
Vec=np.zeros(n)
for i in range(0,n):
    Elise = np.random.randint(1,31)
    Map = np.random.randint(Elise,31)
    Monkey = np.random.randint(Map,31)
    #print Monkey
    Vec[i]=Monkey
print np.average(Vec)
