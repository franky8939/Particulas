import tensorflow as tf
import random
from tensorflow import keras
 # Bibliotecas de ayuda
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import gaussian
 # Biblioteca para datos de entrenamiento
from sklearn.model_selection import train_test_split
import h5py as h # manipular extensiones

## CLASE DE LOS VALORES A TENER EN CUENTA
class CONFIG():
    def __init__(self, v_input , v_output , n_capas  , exp  , learning_rate , 
                 cross_entropy , n_iterations , dropout ):
        self.n_capas  = 2
        self.n_capas  = 2
        self.v_input  = v_input
        self.v_output = 2
        self.exp      = 1
        #self.matrix_neuronas
        self.learning_rate = 1e-4
        self.cross_entropy = 1
        self.n_iterations  = 3000
        self.dropout       = 0.5



## DEFINICION DE LOS MODOS DE ELECCION DE CAPAS OCULTAS Y NUMEROS DE NEURONAS
def neuronas( dD ): #v_input, v_output, n_capas = 2, exp = 1,  modo = 'poly' ):
    CONFIG = Dd()
    x = np.ones(CONFIG.n_capas + 2)
    #print(x)
    if  CONFIG.exp >= 1: #modo == 'poly':
        for i in range(CONFIG.n_capas + 2):
            x[len(x)-i-1] = round(( CONFIG.v_input - CONFIG.v_output )*pow(i/(CONFIG.n_capas + 1 ), CONFIG.exp) + CONFIG.v_output)
            #print(x[i])
            #print(i)
    elif CONFIG.exp < 1:
        for i in range(CONFIG.n_capas + 2):
            x[len(x)-i-1] = round(( CONFIG.v_input - CONFIG.v_output )*pow(i/( CONFIG.n_capas + 1 ), -1/CONFIG.exp) + CONFIG.v_output)
            #print(x[i])
            #print(i)
    CONFIG.matrix_neuronas = np.int64(x)
    return CONFIG


## ORGANIZACION DE LA ESTRUCTURA INTERNA DE ENTRENAMIENTO ##
def estructura( INPUT_LINEAL, INPUT_LINEAL_TEST, OUTPUT_LINEAL , OUTPUT_LINEAL_TEST , CONFIG):
    #salida = tf.compat.v1.placeholder(tf.int32, [None])
    
    CONFIG = neuronas( CONFIG )
    
    X = tf.compat.v1.placeholder("float", [None, CONFIG.matrix_neuronas[0]] , name="X_estructura"); # Estructura de la entrada
    
    #proceso iteractivo dinamico 
    for i in range(len(CONFIG.matrix_neuronas)-1):

        weights = tf.Variable(tf.truncated_normal([CONFIG.matrix_neuronas[i], CONFIG.matrix_neuronas[i+1]], stddev=0.1) , name=f"w{i}")
        biases = tf.Variable(tf.constant(0.1, shape=[CONFIG.matrix_neuronas[i+1]]) , name=f"b{i}" )
        
        if  i == 0: # CONDICION INICIAL
            layer = tf.add(tf.matmul(X, weights), biases , name=f"layer{i}" )
        else: # VALORES INTERNMEDIOS
            layer = tf.add(tf.matmul(layer, weights), biases , name=f"layer{i}" )
    
    # PARAMETROS FINALES PARA CARACTERIZACION 
    Y = tf.compat.v1.placeholder( "float" , [None, CONFIG.matrix_neuronas[-1]] , name="Y_estructura") #Estructura de la salida
    
    CONFIG.cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=Y, logits=layer))
    CONFIG.train_step    = tf.compat.v1.train.AdamOptimizer( CONFIG.learning_rate ).minimize( CONFIG.cross_entropy )
    CONFIG.correct_pred  = tf.equal(tf.argmax(layer, 1), tf.argmax(Y, 1))
    CONFIG.accuracy      = tf.reduce_mean(tf.cast( CONFIG.correct_pred  , tf.float32))
    
    # INICIALIZACION DE LOS PARAMETROS DE NUESTRO PROCESO A CALCULAR
    init = tf.compat.v1.global_variables_initializer()

    CONFIG.cost_summary  = tf.compat.v1.summary.scalar("Cost", CONFIG.cross_entropy)
    CONFIG.acc_summary   = tf.compat.v1.summary.scalar("Accuracy", CONFIG.accuracy)
    CONFIG.all_summary   = tf.compat.v1.summary.merge_all()
    
    # COMENZAR EL PROCESO DE ENTRENAMIENTO
    with tf.Session() as sess:
        writer = tf.summary.FileWriter("Tensorboard", sess.graph)
        #print(sess)
        sess.run(init)
        #saver.save(sess, 'modelo')
        for i in range(CONFIG.n_iterations):
            sess.run(CONFIG.train_step, feed_dict={X: INPUT_LINEAL, Y:OUTPUT_LINEAL}) # CORRIDA
            
            CONFIG.summary_results, CONFIG.loss, CONFIG.acc = sess.run([ CONFIG.all_summary, CONFIG.cross_entropy, CONFIG.accuracy], 
                                                  feed_dict={X: INPUT_LINEAL, Y: OUTPUT_LINEAL})
            writer.add_summary(CONFIG.summary_results, i)
            if (i)%10 == 0:
                print("Iteration", str(i), "\t| Loss =", str(CONFIG.loss), "\t| Accuracy =", str(CONFIG.acc))
        
            if CONFIG.acc>.999:
                print("Iteration", str(i), "\t| Loss =", str(CONFIG.loss), "\t| Accuracy =", str(CONFIG.acc))
                break
        CONFIG.test_accuracy = sess.run( CONFIG.accuracy , feed_dict={X: INPUT_LINEAL_TEST, Y: OUTPUT_LINEAL_TEST})
        print("\nAccuracy on test set:", CONFIG.test_accuracy )
    
    return CONFIG
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
