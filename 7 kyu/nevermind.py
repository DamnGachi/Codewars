import time
from operator import itemgetter

list1 = list()
list2 = list()
origlist = list()
for i in range (1,5000000):
        t = (i, 2*i)
        origlist.append(t)

print ("Using zip")
starttime = time.time()
list1, list2 = map(list, zip(*origlist))
elapsed = time.time()-starttime
print( elapsed)

print ("Using itemgetter")
starttime = time.time()
list1 = map(itemgetter(0),origlist)
list2 = map(itemgetter(1),origlist)
elapsed = time.time()-starttime
print (elapsed)
print ("Using sorted")
starttime = time.time()
s=sorted([list(a) for a in zip(list1,list2)])
elapsed = time.time()-starttime
print (elapsed)
print ("Using map")
starttime = time.time()
s1=sorted(list(map(list,zip(list1,list2))))
elapsed = time.time()-starttime
print (elapsed)
