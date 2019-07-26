# -*- coding:UTF-8 -*-

#TF可视化数据流图
import tensorflow as tf

# loss = tf...
# tf.summary.scalar('loss',loss)

a = tf.constant(4, name="input_a")

b = tf.constant(2, name="input_b")
c = tf.multiply(a, b, name="mul_c")
d = tf.add(a, b, name="add_d")
e = tf.add(c, d, name="add_e")

with tf.Session() as sess:
    print(sess.run(e))
    writer = tf.summary.FileWriter('./my_graph',sess.graph)
