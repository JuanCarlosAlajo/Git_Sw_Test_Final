**Prueba Final**

**Tema:** Servicio Web para consulta de Información

1. **OBJETIVO**

El desarrollo de la práctica tiene como objeto aplicar los conocimientos recibidos en la asignatura de “TRATAMIENTO DE DATOS”, aplicando a la implementación de un servicio web para consulta de información registrada en una base de datos Mongo DB.

2. **DESCRIPCIÓN DE LA SOLUCIÓN**

- Uso de librerías para implementación de servicios web (Flask)
- Ejecutar procesos de consulta de todos los registros de una colección de datos.
- Ejecutar procesos de consulta individual, enviando como parámetro en nombre de la institución.
- Uso de la herramienta Postman, para pruebas y consultas de resultados del servicio web.
- Identificar registros de tipo colección.
- Respaldar la solución o desarrollo en un repositorio GitHub.

3. **DISEÑO DE LA SOLUCION**

    3.1. **DIAGRAMA DE ARQUITECTURA**

![arquitectura_ws.PNG](Graficos%2Farquitectura_ws.PNG)

3.2. **DICCIONARIO DE DATOS**
- Motor de Base de datos MongoDB
- Base de Datos: pry\_test\_fin\_tratam\_datos
- Colección: REGISTROS_TEST-FINAL
- Campo 1: INSTITUCION
- Campo 2: AVALUO
- Campo 3: FECHA\_REGISTRO

3.3. **DIAGRAMA DE FLUJO**

![Diagrama_Flujo_ws.PNG](Graficos%2FDiagrama_Flujo_ws.PNG)

4. **DESARROLLO**

Para desarrollar el proyecto, se sigue los siguientes pasos:

- Como primer paso, se crea un repositorio GitHub público (Git\_Sw\_Test\_Final), para respaldar y controlar los versionamientos del proyecto.
- Se establece una conexión a la base de datos mongoDB
- Se implementa las siguientes librerías en el ambiente de desarrollo PyChar, mediante la inclusión en el archivo “requirements.txt”
  - Flask
  - Pymongo
  - Requests

- Se implementa el archivo cnx\_base\_datos, mismo que contiene la clase MongoDriver con sus atributos y métodos a ser consumidos en otros procesos. Cabe señalar que el constructor de esta clase contiene la cadena de conexión hacia la base de datos MongoDB
- Se crea el archivo servicio\_web.py, mismo que ejecuta las consultas total y por institución, para extraer la información (colección de registros) de la base de datos mongoDB.

5. **CONCLUSIONES**
- El conocimiento recibido es de gran ayuda para solventar nuevos retos en los desarrollos tecnológicos.
- Optimización de recursos, mediante uso de herramientas libres.


6. **REFERENCIAS**

[**https://www.postman.com/**](https://www.postman.com/)

[**https://www.youtube.com/watch?v=GsCCyN3fRoI**](https://www.youtube.com/watch?v=GsCCyN3fRoI)






