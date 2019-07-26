# -*- coding:UTF-8 -*-

import tensorflow as tf

sees = tf.InteractiveSession()

#单位矩阵
I_matrix = tf.eye(5)
print(I_matrix.eval())

X = tf.Variable(tf.eye(10))
X.initializer.run()
print(X.eval())

A = tf.Variable(tf.random_normal([5,10]))
A.initializer.run()

#将矩阵相乘
product = tf.matmul(A,X)

b = tf.Variable(tf.random_uniform([5,10],0,2,dtype=tf.int32))
b.initializer.run()
print(b.eval())
b_new = tf.cast(b,dtype=tf.float32)#cast函数是将b转换为指定的数据类型

t_sum = tf.add(product,b_new)
t_sub = product - b_new
print("A*X _b\n",t_sum.eval())
print("A*X _b\n",t_sub.eval())
