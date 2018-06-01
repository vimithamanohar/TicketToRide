import os
from numpy import array
from skimage import transform 
from loadDatas import load_data_labels

path = '/home/ubuntu/ttr/TicketToRide'
labelfilename='threeTestSegment.txt'
[images,labels]=load_data_labels(path,labelfilename)
print(images.ndim)
print(images.size)
print(images[0])

print("labels")

 #Print the `labels` dimensions
print(labels.ndim)

 #Print the number of `labels`'s elements
print(labels.size)

 ##Count the number of labels
print(len(set(labels)))
print(labels)

images28 = [transform.resize(image, (28, 28)) for image in images]
