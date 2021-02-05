# Wirbot


El codígo esta sobre MIT más las imagenes no, son para uso no lucrativo y el crédito va a sus respectivos autores.

Para correr el bot se necesita python3.5 o mayor asi como tener la libreria del API de discord la cual se puede instalar de esta manera
`pip install discord.py` O `pip3 install discord.py` asi como la librería llamada Pillow que se tiene que instalar [como marca la documentación](https://pillow.readthedocs.io/en/latest/installation.html)

Para instalar todos los paquetes, corre `pip install -r requirements.txt`

Para correr el bot es de la siguente manera
`python wirbot2.0.py` O  `python3 wirbot2.0.py`

Si necesitas que corra en el fondo: `python3 wirbot2.0.py &`
Tambien puedes correr el archivo `.sh`

Si quieres saber más sobre el API de discord puede checar su documentación [aquí](https://discordpy.readthedocs.io/en/latest/#).

Lo que incluye esta nueva versión que escribí, es la habilidad de montar/desmontar modulos sin necesidad de desconectar el bot aplicando los comandos `&load <nombre del módulo>` y 
`&unload <nombre del módulo>`. Esto permite modificar los archivos de los módulos de manera más eficiente sin perder otras funcionalidades del bot así como tener las cosas mejor organizadas.

Todos los comandos son modificables tanto en nombre como en funcionalidad así como el prefijo para comandos del bot el cual esta en el el archivo `wirbot2.0.py` representado por las siguentes lineas:

```py
prefix = '&'
bot = commands.Bot(command_prefix = prefix)
```

Estos módulos se encuentran en el directorio de Cogs.

## Consideraciones

Si el modulo de voz no funciona, probablemente le falte la siguente libreria:

* PyNaCl

Para eso, tenadras quie instalar las siguentes librerias:
* ibffi-dev (o libffi-devel en algunos sistemas)
* python-dev (e.g. python3.6-dev para Python 3.6)
