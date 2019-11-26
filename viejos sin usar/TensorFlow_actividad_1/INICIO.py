# TensorFlow e tf.keras
import tensorflow as tf
from tensorflow import keras

# Bibliotecas de ajuda
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#NOTACION A USAR *son las variables q no son pertinentes en el estudio
#*    1. survival -- the number of months patient survived (has survived,
#		  if patient is still alive).  
#*    2. still-alive -- a binary variable.  0=dead at end of survival period,
#		     1 means still alive 
#INP: 3. age-at-heart-attack -- age in years when heart attack occurred
#INP: 4. pericardial-effusion -- binary. Pericardial effusion is fluid
#			      around the heart.  0=no fluid, 1=fluid
#INP: 5. fractional-shortening -- a measure of contracility around the heart
#			       lower numbers are increasingly abnormal
#INP: 6. epss -- E-point septal separation, another measure of contractility.  
#	      Larger numbers are increasingly abnormal.
#INP: 7. lvdd -- left ventricular end-diastolic dimension.  This is
#	      a measure of the size of the heart at end-diastole.
#	      Large hearts tend to be sick hearts.
#*    8. wall-motion-score -- a measure of how the segments of the left
#			   ventricle are moving
#INP: 9. wall-motion-index -- equals wall-motion-score divided by number of
#			   segments seen.  Usually 12-13 segments are seen
#			   in an echocardiogram.  Use this variable INSTEAD
#			   of the wall motion score.
#*    10. mult -- a derivate var which can be ignored
#*    11. name -- the name of the patient (I have replaced them with "name")
#*    12. group -- meaningless, ignore it
#OUT: 13. alive-at-1 -- Boolean-valued. Derived from the first two attributes.
#                     0 means patient was either dead after 1 year or had
#                     been followed for less than 1 year.  1 means patient 
#                     was alive at 1 year.
# NOTACION DE LAS VARIABLES 
label_total=["survival", "still_alive", "age-at-heart-attack",
       "pericardial-effusion","fractional-shortening", 
       "epss", "lvdd","wall-motion-score","wall-motion-index",
       "mult" , "group", "alive-at-1"];
# ENTRAR LA INFORMACION DESDE UN ARCHIVO INTERNO
data = pd.DataFrame(np.genfromtxt('echocardiogram.data', delimiter=','), columns= label_total)
label_user=["age-at-heart-attack", "pericardial-effusion","fractional-shortening", "epss",
            "lvdd","wall-motion-index", "alive-at-1"];
## FILTRAR LAS VARIABLES QUE SE UTILIZARAN EN EL ENTRENAMIENTO DE ML
select_data=data[label_user];#DATOS ORIGINALES SIN FILTRAR, COLUMNAS DE INTERES
#ARREGLAR LA COLUMNA DE alive-at-1"];
alive= np.zeros(len(select_data));
for j in range(len(alive)):
    if   data[label_total[0]][j] > 12:#MAS DE 12 MESES
         select_data["alive-at-1"].values[j] = 1; #CUMPLE EL REQUISITO
    elif data[label_total[0]][j] == 12 and data[label_total[1]][j] == 1:#12 MESES Y VIVE
         select_data["alive-at-1"].values[j] = 1; #CUMPLE EL REQUISITO
    elif data[label_total[0]][j] < 12 and data[label_total[1]][j] == 1:# MENOS DE 12 MESES Y VIVE
         select_data["alive-at-1"].values[j] = -1; #NO CUMPLE EL REQUISITO
#select_data["alive-at-1"].values[j] =alive;  
    
##MATRIX LOGICA DE DATOS ELIMINAR LO DESCONOCIDO
for i in range(len(label_user)):
    if i==0:
        log=select_data[label_user[i]] !=-1;#print(i);
    else:
        log= np.logical_and(select_data[label_user[i]] !=-1,log)
select_data=select_data[log]; #IGUALAR EN MIS DATOS PARA FILTRAR LOS DESCONOCIDOS           
    
#VALORES QUE SE UTILIZARAN PARA ENTRENARSE CORRECTAMENTE
input_data=select_data[{"age-at-heart-attack", "pericardial-effusion",
                "fractional-shortening", "epss", "lvdd",
                "wall-motion-index"}];
output_data=select_data[{"alive-at-1"}];

#PREPARAR EL ENTRENAMIENTO 
n_input = np.int64(len(label_user)-1)   # input layer
n_hidden = np.int64(np.round(np.sqrt(len(label_user)))) # 1st hidden layer
n_output = np.int64(1)   # output 

learning_rate = 1e-4;   n_iterations = 100
batch_size = 3;         dropout = 0.5

X = tf.compat.v1.placeholder("float", [None, n_input]);
Y = tf.compat.v1.placeholder("float", [None, n_output])
keep_prob = tf.placeholder(tf.float32) 

weights = {
    'w1': tf.Variable(tf.random.normal([n_input, n_hidden])),
    'out': tf.Variable(tf.random.normal([n_hidden, n_output]))
    }

biases = {
    'b1': tf.Variable(tf.constant(0.1, shape=[n_hidden])),
    'out': tf.Variable(tf.constant(0.1, shape=[n_output]))
}

layer_1 = tf.add(tf.matmul(X, weights['w1']), biases['b1'])
layer_drop = tf.nn.dropout(layer_1, keep_prob)
output_layer = tf.matmul(layer_1, weights['out']) + biases['out']

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=Y, logits=output_layer))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

correct_pred = tf.equal(tf.argmax(output_layer, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

init = tf.global_variables_initializer()
sess = tf.compat.v1.Session()
sess.run(init)


cost_summary = tf.compat.v1.summary.scalar("cost",cross_entropy)
acc_summary = tf.compat.v1.summary.scalar("accuracy",accuracy)
# Merge all summaries 
all_summary = tf.compat.v1.summary.merge_all()
# Summary writer

for i in range(n_iterations):
#    batch_x, batch_y = mnist.train.next_batch(batch_size)
    sess.run(train_step, feed_dict={X: input_data.values, Y: output_data.values})
    # print loss and accuracy (per minibatch)
    #if i%100==0:
    #    print(i)
    if i % 10 == 0:
            summary_results, loss, acc = sess.run([all_summary, cross_entropy, accuracy], 
                                                  feed_dict={X: x_train, Y: y_train})
            print(f"Iteration {i} \t| Loss = {loss:7.5f} \t| Accuracy = {acc:7.5f}")
            writer.add_summary(summary_results, i)


#    summary_results, minibatch_loss, minibatch_accuracy = sess.run([all_summary, cost_summary , acc_summary], feed_dict={X: input_data.values, Y: output_data.values})
#    print("Iteraciones", str(i), "\t| Loss =", str(minibatch_loss), "\t| Accuracy =", str(minibatch_accuracy))
        
 #       writer.add_summary(summary_results,i)
        
#    test_accuracy= sess.run(accuracy, feed_dict={X: input_data.values, Y: output_data.values, keep_prob:1.0})
#    print("\nAccuracy on test set:", test_accuracy)
    #print(out)
#    if test_accuracy==1:
#        break
#    correct_prediction = tf.equal(y_pred_cls, y_true_cls)

















