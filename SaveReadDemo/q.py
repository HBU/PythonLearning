import tensorflow as tf


# save to file
W = tf.Variable([[1, 2, 3], [4, 5, 6]], dtype=tf.float32, name='weight')
b = tf.Variable([[1, 2, 3]], dtype=tf.float32, name='biases')

init = tf.initialize_all_variables()
saver = tf.train.Saver()
with tf.Session() as sess:
    sess.run(init)
    save_path = saver.save(sess, "my_net/save_net.ckpt")
    print("save to path:", save_path)