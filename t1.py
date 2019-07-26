# -*- coding:UTF-8 -*-
import tensorflow as tf

# messsage =  tf.constant("Hello World!")
# with tf.Session() as sess:
#     print(sess.run(messsage).decode())

import threading

class SimpleCreator():
    def f(self,id):
        print('綫程執行 %s \n' %id)
        return
    def  __init__(self):
        return

    def creatThread(self):
        for i in range(3):
            t = threading.Thread(target=self.f,args=(i,))#其中的逗号不能少，少了就是数组了，arg需要是元组，就会出错。
            t.start()

if __name__ == '__main__':
    sc = SimpleCreator()
    sc.creatThread()

