#IMPORTACION DE LAS LIBRERIAS NECESARIAS:
 
   
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
    

#CARGA Y REVICION DE LOS DATOS:
    
Crudo = pd.read_csv('31_Datos_JDSG_crudos.csv', index_col='Id')

print('\nEstos son los primeros 10 datos del archivo crudo\n')
print(Crudo.head(10))

print('\nEstos son los ultimos 10 del archivo crudo\n')
print(Crudo.tail(10))
    
Estadisticas_Crudo = Crudo.describe()
print('\nEstas son las estadisticas del archivo crudo\n')
print(Estadisticas_Crudo)


#CONOCER LA ESTRUCUTURA DEL DATAFRAME:
    
Columnas_Crudo = len(Crudo.columns)
print('\nEL numero de columnas del crudo es: ', Columnas_Crudo)
print('Los nombres del las columnas son: \n')
for nombres in Crudo.columns:
    print(' >', nombres)
    
Registros_Crudo = len(Crudo.index)
print('\nEL numero de registros del crudo es: ', Registros_Crudo)

print('\nTipo de dato en cada columna: \n', Crudo.dtypes)

Registros_Completos_Crudo = Crudo.count()
print('\nEl numero de resgistros completos por variable es: \n', Registros_Completos_Crudo)

Registros_Completos_Crudo_2 = len(Crudo.dropna())
print('\nEl numero de registros completos es:  ', Registros_Completos_Crudo_2)

Registros_faltantes_Crudo_ = (Registros_Crudo - Registros_Completos_Crudo)
print('\nEl numero de registros faltantes por variable es:  \n', Registros_faltantes_Crudo_)

print('\nEl numero de registros con errores por variable es: \n')
Registros_error_Crudo = np.zeros(Columnas_Crudo, dtype='int32')
for i in range(Registros_Crudo):
    for j in range(2, Columnas_Crudo):
        if Crudo.iloc[i, j] < 0:
            Registros_error_Crudo[j] += 1
for j in range(Columnas_Crudo):
    print(Crudo.columns[j].ljust(20), Registros_error_Crudo[j])
  

#DEPURACION DEL DATAFRAME:
    
Procesado = Crudo.fillna({'Temperatura': 17.4782, 'Direccion': 171.951, 'Presion': 569.172,
                          'Humedad': 80.03})

Procesado = Procesado.fillna({'Velocidad': 0.0})

Procesado = Procesado.fillna(method='ffill')

for i in range(Registros_Crudo):
    for j in range(2, Columnas_Crudo):
        if Procesado.iloc[i, j] < 0:
            Procesado.iloc[i, j] = 0
            

print('\nEl numero de registros faltantantes por variable tras la depuracion es: \n')
Registros_procesado = len(Procesado.index)
Registros_completos_procesado = Procesado.count()
registros_faltantes_procesado = (Registros_procesado - Registros_completos_procesado)
print(registros_faltantes_procesado)


#PROCESAMIENTO DE DATOS:
    
def FechaHora(Fila):
    Concatenado = Fila['Fecha'] + ' ' + Fila['Hora']
    Fecha_Hora = pd.to_datetime(Concatenado, dayfirst=True)
    return Fecha_Hora
Procesado['Fecha y Hora'] = Procesado.apply(FechaHora, axis = 1)

Procesado['Tiempo'] = Procesado.iloc[:, 10] - pd.to_datetime('2005-06-01 00:00:00')
Procesado['Tiempo en dias'] = Procesado.loc[:, 'Tiempo']/np.timedelta64(1, 'D')
Procesado['Intervalo de Medicion'] = pd.Series(Procesado.iloc[0:Registros_Crudo, 11]) - pd.Series(Procesado.iloc[0:Registros_Crudo, 11].shift(1))
Procesado.loc[1, 'Intervalo de Medicion'] = Procesado.loc[1,'Tiempo']

Procesado['Intervalo de Medicion'] = Procesado.loc[:, 'Intervalo de Medicion'] / np.timedelta64(1, 's')
Estadisticas_Intervalo_Medicion = Procesado['Intervalo de Medicion'].describe()

print('\nEl promedio del intervalo de medicion es: 299.965')
print('La desviacion estandar del tiempo es: 3.22749')

def Datofecha(Fecha):
    d = Fecha.split('/')
    for i in range(2):
        d[i] = d[i].zfill(2)
    d = d[::-1]
    d = ''.join(d)
    return d

Procesado['Fecha en Indice'] = Crudo['Fecha'].apply(Datofecha)
Procesado_Dias = Procesado.groupby('Fecha en Indice').agg({'Temperatura': 'mean',
                                                            'Velocidad': 'max', 
                                                            'Direccion': 'mean',
                                                            'Presion': 'mean',
                                                            'Humedad': 'mean',
                                                            'Precipitacion': 'max',
                                                            'Radiacion': 'mean',
                                                            'Evapotranspiracion': 'max'})


#PRESENTAR DATOS:
    
t = Procesado['Tiempo en dias']
y1 = Procesado['Temperatura']
y2 = Procesado['Velocidad']
y3 = Procesado['Direccion']
y4 = Procesado['Presion']
y5 = Procesado['Humedad']
y6 = Procesado['Precipitacion']
y7 = Procesado['Radiacion']
y8 = Procesado['Evapotranspiracion']


plt.subplot(3, 3, 1)
plt.plot(t, y1, lw = '0.75', color= '#C0392B')
plt.title('Temperatura')
plt.ylabel('Temperatura [°]')
plt.xlabel('Tiempo [dias]')
plt.xlim([0, 31])

plt.subplot(3, 3, 2)
plt.plot(t, y2, lw = '0.75', color= '#9B59B6')
plt.title('Velocidad del viento')
plt.ylabel('Velocidad [m/s]')
plt.xlabel('Tiempo [dias]')
plt.xlim([0, 31])

plt.subplot(3, 3, 3)
plt.plot(t, y3, lw = '0.75', color= '#2980B9')
plt.title('Dirección del viento')
plt.ylabel('Dirección [°]')
plt.xlabel('Tiempo [dias]')
plt.xlim([0, 31])

plt.subplot(3, 3,4)
plt.plot(t, y4, lw = '0.75', color= '#1ABC9C')
plt.title('Presión atmosferica')
plt.ylabel('Presión [mmHg]')
plt.xlabel('Tiempo [dias]')
plt.xlim([0, 31])

plt.subplot(3, 3,5)
plt.plot(t, y5, lw = '0.75', color= '#F1C40F')
plt.title('Humedad Relativa')
plt.ylabel('HR [%]')
plt.xlabel('Tiempo [dias]')
plt.xlim([0, 31])

plt.subplot(3, 3,6)
plt.plot(t, y6, lw = '0.75', color='#E67E22')
plt.title('Precipitación')
plt.ylabel('Precipitación [mm]')
plt.xlabel('Tiempo [dias]')
plt.xlim([0, 31])

plt.subplot(3, 3,7)
plt.plot(t, y7, lw = '0.75', color= '#34495E')
plt.title('Radiación Solar')
plt.ylabel('Radiación [W/m^2]')
plt.xlabel('Tiempo [dias]')
plt.xlim([0, 31])

plt.subplot(3, 3,8)
plt.plot(t, y8, lw = '0.75', color= '#95A5A6')
plt.title('Evapotranspiración')
plt.ylabel('Evapotranspiración [mm]')
plt.xlabel('Tiempo [dias]')
plt.xlim([0, 31])
plt.show()


Procesado_Dias.plot(kind="bar", y="Temperatura", color='#C0392B')
plt.title('Temperatura')
plt.xlabel('día')
plt.ylabel('Temperatura [°]')
plt.show()

Procesado_Dias.plot(kind="bar", y="Velocidad", color='#9B59B6')
plt.title('Velocidad del viento')
plt.xlabel('día')
plt.ylabel('Velocidad [m/s]')
plt.show()

Procesado_Dias.plot(kind="bar", y="Direccion", color='#2980B9')
plt.title('Dirección del viento')
plt.xlabel('día')
plt.ylabel('Dirección [°]')
plt.show()

Procesado_Dias.plot(kind="bar", y="Presion", color='#1ABC9C')
plt.title('Presión atmosferica')
plt.xlabel('día')
plt.ylabel('Presión [mmHg]')
plt.show()

Procesado_Dias.plot(kind="bar", y="Humedad", color='#F1C40F')
plt.title('Humedad Relativa')
plt.xlabel('día')
plt.ylabel('HR[%]')
plt.show()

Procesado_Dias.plot(kind="bar", y="Precipitacion", color='#E67E22')
plt.title('Precipitación')
plt.xlabel('día')
plt.ylabel('Precipitación [mm]')
plt.show()

Procesado_Dias.plot(kind="bar", y="Radiacion", color='#34495E')
plt.title('Radiación Solar')
plt.xlabel('día')
plt.ylabel('Radiación [W/m^(2)]')
plt.show()

Procesado_Dias.plot(kind="bar", y="Evapotranspiracion", color='#95A5A6')
plt.title('Evapotranspiración')
plt.xlabel('día')
plt.ylabel('Evapotranspitación [mm]')
plt.show()


#GUARDAR DATOS EN ARCHIVO PROCESADO:
    
Crudo.to_csv('31_Datos_JDSG_procesados')
    

#FIN DEL PROGRAMA:
    
print('\nEl programa ha finalizado con exito')