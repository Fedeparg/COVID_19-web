# COVID-19 Web

Este es el repositorio que contiene el código fuente para la web <https://covid-19-models-web-le6bgcbupa-ey.a.run.app/>, la cual está ligada a mi TFM.
Con ella es posible probar los modelos que he desarrollado en mi trabajo.

En caso de que la web no este disponible, debido a que se ejecuta sobre una prueba gratuita de Google Cloud (la cual tiene fecha de caducidad el día 6 de septiembre de 2021), es posible seguir probando la web mediante un contenedor docker.

## Setup de la web offline

Es necesario tener instalado y ejecutando Docker para el funcionamiento de la web.

A continuación, se abre una terminal en el directorio descargado de github y se ejecuta el siguiente comando:

```docker build -t covid19 .```

Docker comenzará a cargar las librerías necesarias y creará la imagen **covid19**.
A continuación, basta con ejecutar la siguiente línea para que la web empiece a funcionar.

```docker run -it --name covid19 --rm -p 8080:8080 covid19```

En la propia terminal aparecerá la URL en la que se ha levantado el proceso.
Por defecto estará en 0.0.0.0:8080. Accediendo a esta dirección desde cualquier navegador es posible probar los modelos con los ficheros de ejemplo incluidos en el repositorio.
