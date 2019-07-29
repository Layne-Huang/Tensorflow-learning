# -*- coding:UTF-8 -*-
#简单的线性回归

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

learning_rate = 0.01

#归一化函数
def normalize(X):
    mean = np.mean(X)
    std = np.std(X)
    X = (X-mean)/std
    return X

boston = tf.contrib.learn.datasets.load_dataset('boston')
print(boston.data[0])
X_train,Y_train = boston.data,boston.target
X_train = normalize(X_train)

x = tf.placeholder(tf.float32,[None,13],name = 'X')
y = tf.placeholder(tf.float32,[None,1],name = 'Y')

with tf.name_scope("Model"):
    w = tf.Variable(tf.random_normal([13,1],stddev=0.01),tf.float64,name='w')
    b = tf.Variable(0.0,tf.float64,name='b')

    def model(x,w,b):
        return tf.matmul(x,w)+b

    pred = model(x,w,b)

loss = tf.reduce_mean(tf.pow((pred-y),2))

train_op = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

for i in range(0,100):
    for (xt,yt) in zip(X_train,Y_train):
        xt = xt.reshape(1,13)
        yt = yt.reshape(1,1)
        sess.run(train_op,feed_dict={x:xt,y:yt}) #这里的字典key值需要和前面的占位符保持一致,最好不要同名,前面是占位符，后面是训练值
        if i == 99:
            print("损失是{0}".format(sess.run(loss,feed_dict={x:xt,y:yt})))
            break

w = sess.run(w)
b = sess.run(b)
print(w,"\n",b)