# -*- coding:UTF-8 -*-
import tensorflow as tf


sess = tf.InteractiveSession()
# t_1 = tf.linspace(1.0,5.0,2)
# # t_1 = tf.range(10)
# print(t_1.eval())
#
# t_random = tf.random_normal([3],mean=3.0,stddev=5.0,seed=10)
# print(t_random.eval())

#Tensorflow 占位符
x = tf.placeholder("float")
y = 2*x
data = tf.random_uniform([4,5],10)
print(data.eval())