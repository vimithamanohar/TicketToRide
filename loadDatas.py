import os
from numpy import array
from skimage import data

def load_data(path):
    #print('file_name: ',path)
    images = []
    #file_names = sorted(os.listdir(path)) 
    file_names = sorted(os.listdir(path),key=lambda x: int(os.path.splitext(x)[0]))
    for f in file_names:
        #print('Image_file_name: ',f)
        images.append(data.imread(os.path.join(path, f)))
    return images

def load_label(filename):    
    labels = []
    file = open(filename, 'r') 
    for line in file:
        #print(line)
        labels.append(line.strip('\n'))
    print('label_file_name written: ',filename)
    file.close()
    return labels
    

def load_data_labels(path,labelfilename):
    train_data_directory=os.path.join(path,'Just3')
    labelfile=os.path.join(path,labelfilename)
    
    images = load_data(train_data_directory)
    labels=load_label(labelfile)

    images = array( images )
    labels= array( labels )
    return [images,labels]

