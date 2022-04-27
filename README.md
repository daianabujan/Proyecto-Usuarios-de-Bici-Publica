# Proyecto Usuarios de Bici Pública:bike:
 
![descripcion](https://www.buenosaires.gob.ar/sites/gcaba/files/styles/interna_noticia/public/field/image/200_km_red_de_ciclovias_y_bicisendas_caba_2_1.jpg?itok=dwlD2rwy)

**Objetivo principal:** 
Análizar la cantidad de usuarios que utilizaron las bicicletas públicas dentro de la Ciudad Autónoma de Buenos Aires en 2021 y obtener un TOP de estaciones de origen y destino más utilizadas.:bike:

**Datos:**
Se utilizaron datos de entrada de DATOS ABIERTOS -  GCBA Link: https://data.buenosaires.gob.ar/dataset/bicicletas-publicas (no incluidos dentro del repositorio)

**Metodología**
- Se utilizo LEN para contabilizar el total de filas dentro del archivo (ya que cada fila representa el recorrido de un usuario)
- Se realizó una variable contenedora de los ORIGENES y otra de DESTINOS (ambas con duplicados)
  - La metodología aplicada se fundó en la utilización de listas - tuplas, para obtener valores únicos de las variables generadas contabilizando su cantidad de repeticiones.
  - Se generó una nueva variable de almacemiento y orden, buscando poder determinar cuales son los TOP 5 de estaciones más utilizadas
 