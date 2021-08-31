# BotTestMultiPhone
Pruebas de software automatizadas usando granjas de dispositivos moviles
info pytest https://www.tutorialspoint.com/pytest

## Activar ambiente virtual

- instalar pip3
- instalar virtualenv
- configurar ambiente 
- activar ambiente
  
  ```source pytest_env/bin/activate```

## Ejecucion de pruebas con pytest generando html

- en consola digitar lo siguiente
  * ```pytest TestSuite/Test/"Nombre del test o * para todos" --html=Target/reports/report.html --self-contained-html```
  * para ejecutar pruebas simultaneas con pytest solo agregar al final de la sentencia de ejecucion -n y la cantidad de pruebas simultaneas deseadas ejemplo `-n 3` esto ejecuta tres pruebas simultaneamente
  * Ejemplo con toda la sentencia 
    
    `pytest POMSimple/TestSuite/*Login*  --html=Target/reports/report.html --self-contained-html -n 2`
  * Ejecutar pruebas especificas por el alguna palabra que este dentro del nombre de la prueba usamos `-k palabra_clave`
  * Si queremnos ejecutar por marcación del test usamos `-m pañabra_clave` aqui la palabra claves es la que se uso en `@pytest.mark.<markername>` en el metodo del test
  * Ejemplo con toda la sentencia
  
    `pytest POMSimple/TestSuite/*Login* -m loginIncorrecto  --html=Target/reports/report.html --self-contained-html -n 2`
- tomado de https://docs.pytest.org/en/stable/mark.html 


## Instalar pytest

- ejecutar el comando 

```pip3 install pytest```

## crear archivo de dependencias

- nombre del archivo **requirements.txt**
- dijitar las librerias a utilizar
  * Aqui las mas importantes

```
Appium-Python-Client==1.1.0
pytest-html==3.1.1
```

## Instalar librerias

- usar el comando siguente para instalar las librerias que estan en el archivo **requirements.txt** 
  * ```pip install -r requirements.txt```

## Usar PyCharm como ide

- Te ayudara codificar mucho mas facil con python
- Tiene varios plugins para python que te ayudan a organizar el proyecto

### Informacion de nombrado de variables
- http://recursospython.com/pep8es.pdf

- Clases
  * Los nombres de clase deben ser sustantivos en ```Upper CamelCase```, con la primera letra de cada palabra en mayúscula. Use palabras completas - evitar acrónimos y abreviaturas (a menos que la abreviatura es mucho más extendido que el de la forma larga, como la dirección URL o HTML).
    * ```class Raster```
    * ```class ImageSprite```
  
- Métodos
  * Los métodos deben ser verbos en ```lower_case_with_underscores``` o un conjunto de varias palabras todas en minúscula separada por guiones bajos    
    * ```run()```
    * ```run_fast()```
    * ```get_background()```
- Variables
  * Las variables locales, variables de instancia y variables de clase también se escriben en ```lower_case_with_underscores``` o un conjunto de varias palabras todas en minúscula separada por guiones bajos    * ```int i```
    * ```str c```
    * ```float my_width```
- Constantes
  * Los nombres de las constantes se deben escribir en mayúsculas separadas por guiones bajos. Los nombres de constantes pueden contener dígitos, pero no como primer carácter.
    * ```global MAX_PARTICIPANTS = 10```
  
- Archivos
  * El archivo .py sé nombra con ```lower CamelCase```  o un conjunto de varias palabras que comienza con un verbo en minúsculas; es decir, con la primera letra en minúscula y la primera letra de las palabras siguientes en mayúsculas.
    * testLogin
    * login
  
- Carpetas
  * Las carpetas se nombras con ```Upper CamelCase``` , con la primera letra de cada palabra en mayúscula. Use palabras completas - evitar acrónimos y abreviaturas.
    * PageInvoice
    * Pages



## Patron POM

* APP objeto de pruebas
    > App objeto de prueba
  * Tests
     > pruebas que usan las clases Page Object
    * Page Object
      > Clase heredada de la clase Base Page Object (Localizadores y acciones) 
      * Base Page Object
        > Aisla el resto de codigo de los comandos de Selenium


# Conectando dispositivo local
* Instalar adb https://www.xda-developers.com/install-adb-windows-macos-linux/
* Instalar java jdk

  ## Comandos para conectarse al dispositivo
  
  * Conectar el dispositivo a el usb
  * Activar la depuracion por usb en el dispositivo
  * Listar los dispositivos con el comando ``` adb devices -l ```
    * muestra la lista de dispositivos asi:
    
     ```List of devices attached ```
    
     ```ZE2229S9MH             device usb:1-3 product:astro_retail model:motorola_one_fusion device:astro transport_id:5 ```
  ## Conectarse al dispositivo por red

  * El dispositivo debe estar conectado por usb
  * Ejecutar comando ```adb usb```
  * Luego ejecutar ```adb tcpip 5555```
    * en caso de que genere mensaje siguiente ``` error: no devices/emulators found ```
    * ejecutar este comando ```adb kill-server``` para que reinicie el servidor
    * luego ejecutar nuevamente ```adb tcpip 5555```
    * debe mostras esto ```restarting in TCP mode port: 5555```
  * Luego ejecutar el siguiente conmando para conectar el dispositivo ```adb connect 192.168.0.14``` debes indicar la ip de tu dispositivo
    * Mostrara ```connected to 192.168.0.14:5555```
  * Desconecta el dispositivo de la usb
    * y ejecuta este comando para verificar que quedo conectado ``` adb devices -l ```
    * debe mostrar lo siquiente
    
    ```List of devices attached ```
    
     ```192.168.0.13:5555      device product:astro_retail model:motorola_one_fusion device:astro transport_id:3```

# Como iniciar el servidor de appium
  * Descargar el servidor de appium
    * se puede descargar un ejecutable para iniciar appium
      * El ejecutable muestra en linus una interfas grafica para interactuar con el dispositivo
      * versiones desktop https://github.com/appium/appium-desktop/releases
    * Seguir este tutorias para instalar https://appium.io/docs/en/about-appium/getting-started/?lang=en
  