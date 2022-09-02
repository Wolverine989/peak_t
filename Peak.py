from PIL import Image
from numpy import asarray
import numpy as np
import matplotlib.pyplot as plt
import math


img = Image.open(r"25.jpg")

left = 270
top = 241
right = 415
bottom = 270

img = img.crop((left, top, right, bottom)) 
img = img.convert('L')
#img.show()

numpydata = asarray(img)
a_data = np.average(numpydata, axis=0)
img.close()

#Pull to zero
min_value = min(a_data)
for i in range(len(a_data)):
    a_data[i] -= min_value

#fixx slope
leng = len(a_data)
left  = min(a_data[0:40])
right = min(a_data[-50:-1])
fixer = (left-right)/len(a_data)
fixer = [i*fixer for i in range(len(a_data))]
fixer.reverse()

for i in range(len(a_data)):
    a_data[i] -= fixer[i]
   
# smooothen 
for i in range(20):
    for i in range(len(a_data)-1):
        if i:
            avg = (a_data[i-1]+a_data[i+1])/2
            a_data[i] += avg
            a_data[i] /= 2

    # for i in range(len(data)): data[i]-=10

print(a_data)

    # clip_value = 20
clip_value = 10
clip = [20 for i in range(len(a_data))]
for i in range(len(a_data)):
    if a_data[i]>clip_value:
        clip[i] = 50

    ##
dervi = [0 for i in range(len(clip))]
for i in range(len(clip)):
    if i:
        dervi[i] = clip[i]-clip[i-1]
get_indexes = lambda x, xs : [i for (y,i) in zip(xs, range(len(xs))) if x==y ]
get_width = lambda x: str(float(5/300)*x)+" mm"

max_ = max(dervi)
max_c = dervi.count(max_)
max_ = get_indexes(max_, dervi)

if max_c == 1 :
    plt.plot(a_data)
        # plt.plot(clip, label = "clip at 20")
        # plt.plot(dervi, label ="der")
        # plt.plot(endu, label="final")

        # plt.plot(smooth(a_data))
    plt.legend()
    plt.show()
    print("one line only")
        #return False 

min_ = min(dervi)
min_c = dervi.count(min_)
min_ = get_indexes(min_ , dervi)

## 300px = 5mm aprox
w_c = min_[0]-max_[0]
w_t = min_[1]-max_[1]

w_c = get_width(w_c)
w_t = get_width(w_t)

print(w_c)
print(w_t)

dist = ((max_[1]+min_[1])/2) - ((max_[0]+min_[0])/2)
dist = get_width(dist)

print(dist)
endu = [0 for i in range(len(a_data))]

local_max_c = max(a_data[max_[0]: min_[0]])
local_max_t = max(a_data[max_[1]: min_[1]])

for i in range (max_[0],min_[0]):
    endu[i]= local_max_c
for i in range (max_[1],min_[1]):
    endu[i]= local_max_t
    

    # x = [ i for i in range(len(a_data))]
data_graph= img + "\n C  : " + w_c + "\n T  : " + w_t + "\n C-T : " + dist+ "\n "+ str(local_max_t)
    # plt.plot(a_data)
plt.plot(a_data, label=data_graph)
    # plt.plot(clip, label = "clip at 20")
    # plt.plot(dervi, label ="der")
plt.plot(endu, label="final")

    # plt.plot(smooth(a_data))
plt.legend()
plt.show()
print( local_max_t)
    



