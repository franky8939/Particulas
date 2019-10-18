import tensorflow as tf
import numpy as np 
from matplotlib import pyplot as plt
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
alive= np.ones(len(select_data))*0;
for j in range(len(alive)):
    if data[label_total[0]][j] > 12:#MAS DE 12 MESES
        alive[j] = 1; #CUMPLE EL REQUISITO
    elif data[label_total[0]][j] == 12 and data[label_total[1]][j] == 1:#12 MESES Y VIVE
        alive[j] = 1; #CUMPLE EL REQUISITO
    elif data[label_total[0]][j] < 12 and data[label_total[1]][j] == 1:# MENOS DE 12 MESES Y VIVE
        alive[j] = -1; #NO CUMPLE EL REQUISITO
select_data["alive-at-1"]=alive;  
    
#alive = data[label_total[0]] > 12;# VIVO, SI VIVIERON MAS DE 12 MESES
#alive= ##MATRIX LOGICA DE DATOS ELIMINAR LO DESCONOCIDO
for i in range(len(label_user)):
    if i==0:
        log=select_data[label_user[i]] !=-1;#print(i);
    else:
        log= np.logical_and(select_data[label_user[i]] !=-1,log)
        
select_data=select_data[log];#IGUALAR EN MIS DATOS PARA FILTRAR LOS DESCONOCIDOS           
    
    #print(label_user[i]);

#logic=(select_data["age-at-heart-attack"] !=-1) and (select_data["pericardial-effusion"] !=-1) and 
#        [select_data["fractional-shortening"] !=-1] and [select_data["epss"] !=-1] and 
#        [select_data["lvdd"] !=-1] and [select_data["wall-motion-index"] !=-1] and 
#        [select_data["alive-at-1"] !=-1]];
#select_data=select_data.loc[logic];#FILTRAR COLUMNAS CON -1 EN TODOS MIS DATOS
input_data=select_data[{"age-at-heart-attack", "pericardial-effusion",
                "fractional-shortening", "epss", "lvdd",
                "wall-motion-index"}];
output_data=select_data["alive-at-1"];
#print(len(label))#,label[1])
#print(data.loc[data["survival"]!=-1])
#print(data[[1,:]])
#print(data)#label[1])

#Colum={}
#a.label="survival"
#print(data<0)









