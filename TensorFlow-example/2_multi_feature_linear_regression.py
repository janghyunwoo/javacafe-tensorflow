#-*- coding: utf-8 -*-

import tensorflow as tf

# ======== 학습데이터 ========
# 학습 시간
x1_data = [54, 8, 30, 24, 46, 12, 20, 37, 40, 48]
# 해외거주(월)
x2_data = [12, 0, 12, 15, 12, 0, 36, 12, 12, 24]
# 토익점수
y_data = [800, 320, 600, 630, 700, 300, 920, 720, 700, 920]

# ======== 초기값 설정 =========
W1 = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
W2 = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

# ======== 변수 설정 ========
X1 = tf.placeholder(tf.float32)
X2 = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

# ======== Multiple Linear Regression 에서 학습될 가설 ========
hypothesis = W1 * X1 + W2 * X2 + b

# ======== Multiple Linear Regression 에서 학습될 가설의 Cost Function ========
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# ======== Gradient Descent Algorithm 에서 Step ========
learning_rate = 0.0006

# ======== 텐서플로우에 내장된 GradientDescentOptimizer ========
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

# ======== 학습 시작 ========
for step in xrange(40000):
    sess.run(optimizer, feed_dict={X1: x1_data, X2: x2_data, Y: y_data})
    if step % 100 == 0:
        print step, sess.run(cost, feed_dict={X1: x1_data, X2: x2_data, Y: y_data}), sess.run(W1), sess.run(W2), sess.run(b)

# ======== 학습된 우리의 프로그램에 예측 문의 ========

# 30 시간 공부하고 10개월 해외에서 거주했을 경우 토익점수 예측
print "30시간, 10개월 >> " + str(sess.run(hypothesis, feed_dict={X1: 30, X2: 10})) + " 점"

# 2 시간 공부하고 24개월 해외에서 거주했을 경우 토익점수 예측
print "2시간, 24개월 >> " + str(sess.run(hypothesis, feed_dict={X1: 2, X2: 24})) + " 점"
