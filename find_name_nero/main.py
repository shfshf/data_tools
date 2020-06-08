import tensorflow as tf

with tf.Session() as sess:
    sm = tf.saved_model.load(
        sess, [tf.saved_model.tag_constants.SERVING], "./deliverable_model/asset/model/tensorflow_saved_model/1589881567"
    )

    graph = tf.get_default_graph()
    tvc = graph.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES)
    print(tvc)
