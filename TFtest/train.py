# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 22:15:09 2018

@author: David
"""

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plot
from tensorflow.examples.tutorials.mnist import input_data
import pandas as pd

# 1
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv").values

# 2
x_train = train.iloc[:, 1:].values
x_train = x_train.astype(np.float)

# 3
x_train = np.multiply(x_train, 1.0 / 255.0)

# 4
image_size = x_train.shape[1]
image_width = image_height = np.ceil(np.sqrt(image_size)).astype(np.uint8)

print('Example size:(%g,%g)' % x_train.shape)
print('Dim size:{0}'.format(image_size))
print('Width:{0}\nHeight:{1}'.format(image_width, image_height))

####################################################################

# 5
# labels_flat = train[[0]].values.ravel()
labels_flat = train.iloc[:, 0].values.ravel()
labels_count = np.unique(labels_flat).shape[0]


def dense_to_one_hot(labels_dense, num_classes):
    num_labels = labels_dense.shape[0]
    index_offset = np.arange(num_labels) * num_classes
    labels_one_hot = np.zeros((num_labels, num_classes))
    labels_one_hot.flat[index_offset + labels_dense.ravel()] = 1
    return labels_one_hot


# 6
labels = dense_to_one_hot(labels_flat, labels_count)
labels = labels.astype(np.uint8)
print('Icon:({0[0]},{0[1]})'.format(labels.shape))
print('Icon example:[{0}] => {1}'.format(25, labels[25]))

####################################################################

# 7
VALIDATION_SIZE = 2000

train_images = x_train[VALIDATION_SIZE:]
train_labels = labels[VALIDATION_SIZE:]

validation_images = x_train[:VALIDATION_SIZE]
validation_labels = labels[:VALIDATION_SIZE]

# 8
batch_size = 100
n_batch = len(train_images) / batch_size

# 9
x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])


####################################################################

# 10
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


# 11
x_image = tf.reshape(x, [-1, 28, 28, 1])

####################################################################

# 12
W_conv1 = weight_variable([3, 3, 1, 32])
b_conv1 = bias_variable([32])
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

# 16
W_conv2 = weight_variable([6, 6, 32, 64])
b_conv2 = bias_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)
h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])

# 18
W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

# 19
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# 20
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2

####################################################################

# 21
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=y_conv))
train_step_1 = tf.train.AdadeltaOptimizer(learning_rate=0.1).minimize(loss)

# 23
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_conv, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

global_step = tf.Variable(0, name='global_step', trainable=False)
saver = tf.train.Saver()

init = tf.global_variables_initializer()

####################################################################

# =============================================================================
# with tf.Session() as sess:
#     sess.run(init)
#     #saver.restore(sess,"model.ckpt-12")
#     for epoch in range(1,20):
#         for batch in range(int(n_batch)):
#             batch_x = train_images[batch*batch_size:(batch+1)*batch_size]
#             batch_y = train_labels[batch*batch_size:(batch+1)*batch_size]
#
#             sess.run(train_step_1,feed_dict = {x:batch_x,y:batch_y,keep_prob:0.5})
#
#         accuracy_n = sess.run(accuracy,feed_dict={x:validation_images, y:validation_labels,keep_prob:1.0})
#         print("Num:" + str(epoch+1) +",accuracy:"+str(accuracy_n))
#
#         #30
#         global_step.assign(epoch).eval()
#         saver.save(sess,"./model.ckpt",global_step = global_step)
# =============================================================================


with tf.Session() as sess:
    sess.run(init)

    # =============================================================================
    #     module_file = tf.train.latest_checkpoint('model-1.ckpt-19') #ckpt路径抽调出来
    #     print(module_file)
    #     if module_file is not None:          # 添加一个判断语句，判断ckpt的路径文件
    #         saver.restore(sess, module_file)
    # =============================================================================
    saver.restore(sess, "model.ckpt-19")

    test_x = np.array(test, dtype=np.float32)

    conv_y_preditct = y_conv.eval(feed_dict={x: test_x[1:100, :], keep_prob: 1.0})

    conv_y_preditct_all = list()

    for i in np.arange(100, 28001, 100):
        conv_y_preditct = y_conv.eval(feed_dict={x: test_x[i - 100:i, :], keep_prob: 1.0})
        test_pred = np.argmax(conv_y_preditct, axis=1)
        conv_y_preditct_all = np.append(conv_y_preditct_all, test_pred)

    submission = pd.DataFrame({"ImageId": range(1, 28001), "Label": np.int32(conv_y_preditct_all)})
    submission.to_csv("submission.csv", index=False)

    print('end')













































