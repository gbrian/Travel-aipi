from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import pandas as pd
import argparse
import sys,os
import tensorflow as tf

class ImageGraph():
    def __init__(self):
        labelspath = os.path.join(os.path.dirname(__file__), 'output/output_labels.txt')
        self.graph = os.path.join(os.path.dirname(__file__), 'output/output_graph.pb')
        self.input_layer = 'DecodeJpeg/contents:0'
        self.output_layer = 'final_result:0'
        self.num_top_predictions = 1
        self.labels = self.load_labels(labelspath)
        self.load_predictor()
        
    def  load_image(self, filename):
        #Read in the image_data to be classified."""
        return tf.gfile.FastGFile(filename, 'rb').read()

    def load_labels(self, filename):
        #Read in labels, one label per line."""
        return [line.rstrip() for line in tf.gfile.GFile(filename)]

    def load_graph(self, filename):
        #Unpersists graph from file as default graph."""
        with tf.gfile.FastGFile(filename, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            tf.import_graph_def(graph_def, name='')
  
    def load_predictor(self):
        self.load_graph(self.graph)
        self.sess = tf.Session()
        self.softmax_tensor=self.sess.graph.get_tensor_by_name(self.output_layer)
        
    def predict(self, path):    
        image_data=self.load_image(path)
        predictions,=self.sess.run(self.softmax_tensor, {self.input_layer: image_data})    
        # Sort to show labels in order of confidence             
        top_k = predictions.argsort()[-self.num_top_predictions:][::-1]
        node_id = top_k[0]
        predicted_label = self.labels[node_id]
        score = predictions[node_id]
        return path, predicted_label, score

    def __exit__(self):
        self.sess.close()

