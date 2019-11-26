# importamos todas las paqueterias necesarias para poder trabajar
import numpy as np #Arreglos y distribuciones
import matplotlib.pyplot as plt # para poder graficar
#import pandas as pd #
import per 
per.perceptron()
#PARAMETROS INICIALIZADORES
ancho_caja=1;#ANCHO DE LA CAJA QUE CONTIENE LOS PUNTOS
largo_caja=1#LARGO DE LA CAJA QUE CONTIENE LOS PUNTOS
m_recta=1#PENDIENTE ECUACION DE LA RECTA IMAGINARIA DIVISORIA DE LA PROPIEDADES DE LOS PUNTOS
n_recta=0#INTERCEPTO ECUACION DE LA RECTA IMAGINARIA DIVISORIA DE LA PROPIEDADES DE LOS PUNTOS
pp=0#P. CARACTERIZA LA PROB. DE DISP. FUERA DE LA RECTA DIVISORIA 0 (CONTENIDOS LOS PUNTOS); 1 (PUEDEN GENERARSE EN CUALQUIER LUGAR DEL ESPACIO)
num=100#numeros de puntos a generar

#PARAMETROS DEL ENTRENAMIENTO DE LOS DATOS
ini_pesos=0 #VALOR INICIAL DE LOS PESOS ALEATORIOS ESCOGIDOS AL INICIO DE LAS EPOCAS
fin_pesos=1 #VALOR FINAL DE LOS PESOS ALEATORIOS ESCOGIDOS AL INICIO DE LAS EPOCAS
ep=100 #MAXIMO DE EPOCAS
learg=.01 #LEARNING RATE
resl_ml=.00001 #RESOLUCION DE MI MACHINE LEARNING
ite_limit_min=num/100 #cantidad de corridas donde no se ha encontrado un mejor resultado
error_tot_final=2*num#*ancho_caja*largo_caja

# DECLARA LA REGION EN QUE ESTAN LOS PUNTOS
def REGION(m_recta,n_recta,X,Y):
    return np.sign(m_recta*X + n_recta - Y)

#funcion para generar los puntos
def GENERADOR(num,ancho_caja=1,largo_caja=1,m_recta=1,n_recta=0,pp=1):
    #datos_experimentales = pd.DataFrame(columns=['X','Y','sig'])
    datos_experimentalesX = np.random.uniform(0, ancho_caja, num)
    datos_experimentalesY = np.random.uniform(0, largo_caja, num)
    datos_experimentales  = np.concatenate(([datos_experimentalesX],[datos_experimentalesY],[np.zeros(num)]), axis=0)
    #print(datos_experimentalesX.size)#print(datos_experimentales[1,1]) 
    for i in range(num): # generar las asignaciones -1 y 1 segun correspondan
        #print(i)
        if (np.random.uniform(0,1) > pp/2): # caracterizar la probabilidad de dispersion
            datos_experimentales[2,i] = -REGION(m_recta,n_recta,datos_experimentales[0,i],datos_experimentales[1,i])
        else:
            #print(datos_experimentales)
            datos_experimentales[2,i] = REGION(m_recta,n_recta,datos_experimentales[0,i],datos_experimentales[1,i])
    #print(datos_experimentales)#-1 si esta por debajo del grafico, 1 para lo contrario
    return datos_experimentales
## GRAFICAR LOS DATOS
dat_exp=GENERADOR(num,ancho_caja,largo_caja,m_recta,n_recta,pp) # datos originales
plt.scatter(dat_exp[0,:],dat_exp[1,:],c=dat_exp[2,:], cmap='cividis') # GRAFICAR
plt.legend(loc='best'); plt.xlim(0.,1.); plt.ylim(0.,1.) # PROPIEDADES DE LOS GRAFICOS
plt.title("Datos de entrenamiento");

## ENTRENAR MIS PESOS RESPECTIVOS
W_final=np.random.uniform(ini_pesos,fin_pesos,3)
W=W_final
#b=np.random.uniform(ini_pesos,fin_pesos)
t=0 #contador de ciclos en los que no se ha enccontrado mejor resultados
for _ in range(ep): # CORRIDA POR LAS EPOCAS
    #VALORES INICIALES PARA COMENZAR
    error_tot=0 #REINICIAR ESTE VALOR
    
    for i in range(num):
        error = dat_exp[2,i] - np.sign( W[1]*dat_exp[0,i] + W[2]*dat_exp[1,i] + W[0] )
        error_tot = error_tot + abs(error)
        W[0] = W[0] + error*learg ; W[1] = W[1] + error*learg*dat_exp[0,i] ; W[2] = W[2] + error*learg*dat_exp[1,i]
        #W[0] = W[0] + error*learg ; 
        #W[1:3] = W[1:3] + error*learg*dat_exp[:,i] ; W[2] = W[2] + error*learg*dat_exp[1,i]
    
    # asegurarse de buscar el mejor resultado posible   
    if error_tot<error_tot_final:
        W_final = W ; error_tot_final=error_tot
        t=0 #reiniciar el contador
    else:
        t=t+1
    
    # parar la simulacion por cuestion de convergencia alrededor de un valor
    if t>ite_limit_min:
        break#
    
    #GRAFICAR LOS ERRORES Q SE ESTAN TENIENDO PARA HACERLE EL SEGUIMIENTO
    print(error_tot/(2*num),t)

## ERROR TOTAL 

print(W_final,error_tot_final)    
        
        























        
    