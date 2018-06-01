import os
from numpy import array
from skimage import transform 
from loadDatas import load_data_labels
from sklearn.model_selection import train_test_split

# Import `tensorflow` 
import tensorflow as tf
import matplotlib.pyplot as plt
import random

path = '/home/ubuntu/ttr/TicketToRide'
labelfilename='threeTestSegment.txt'
[images,labels]=load_data_labels(path,labelfilename)
X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.33, random_state=42)
##print(images.ndim)
##print(images.size)
##print(images[0])
##
##print("labels")
##
## #Print the `labels` dimensions
##print(labels.ndim)
##
## #Print the number of `labels`'s elements
##print(labels.size)
##
## ##Count the number of labels
##print(len(set(labels)))
##print(labels)

images28 = [transform.resize(image, (28, 28)) for image in X_train]

images28 = array(images28)

# Initialize placeholders 
x = tf.placeholder(dtype = tf.float32, shape = [None, 28, 28])
y = tf.placeholder(dtype = tf.int32, shape = [None])

# Flatten the input data
images_flat = tf.contrib.layers.flatten(x)

# Fully connected layer 
logits = tf.contrib.layers.fully_connected(images_flat, 62, tf.nn.relu)

# Define a loss function
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels = y, 
                                                                    logits = logits))
# Define an optimizer 
train_op = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)

# Convert logits to label indexes
correct_pred = tf.argmax(logits, 1)

# Define an accuracy metric
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

tf.set_random_seed(1234)
sess = tf.Session()

sess.run(tf.global_variables_initializer())

for i in range(201):
        print('EPOCH', i)
        _, accuracy_val = sess.run([train_op, accuracy], feed_dict={x: images28, y: y_train})
        if i % 10 == 0:
            print("Loss: ", loss)
        print('DONE WITH EPOCH')

sess.close()

# Pick 10 random images
sample_indexes = random.sample(range(len(images28)), 10)
sample_images = [images28[i] for i in sample_indexes]
sample_labels = [y_train[i] for i in sample_indexes]

# Run the "correct_pred" operation
predicted = sess.run([correct_pred], feed_dict={x: sample_images})[0]
                        
# Print the real and predicted labels
print(sample_labels)
print(predicted)

# Display the predictions and the ground truth visually.
fig = plt.figure(figsize=(10, 10))
for i in range(len(sample_images)):
    truth = sample_labels[i]
    prediction = predicted[i]
    plt.subplot(5, 2,1+i)
    plt.axis('off')
    color='green' if truth == prediction else 'red'
    plt.text(40, 10, "Truth:        {0}\nPrediction: {1}".format(truth, prediction), 
             fontsize=12, color=color)
    plt.imshow(sample_images[i],  cmap="gray")

plt.show()
