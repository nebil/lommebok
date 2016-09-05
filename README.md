
# Lommebok

Este miniproyecto es únicamente un ejemplo de juguete
para probar [Bottle](https://bottlepy.org), que es un
[_microframework_](https://en.wikipedia.org/wiki/Microframework) web.  
El objetivo es realizar una aplicación web local que pueda
guardar _snapshots_ de billeteras que cambian en el tiempo.  
Y una “billetera” puede ser definida, simplemente, como
una entidad que almacena valor, en algún tipo de moneda. :moneybag:

## Receta

### Ingredientes

:snake: [Python] será nuestra herramienta de trabajo.  
:warning: Para evitar posibles fallas de compatibilidad,
se **deberá** usar una versión de Python superior a **3.2**.

#### Librerías de Python

La librería utilizada está resumida en la siguiente tabla.

Nombre   | Descripción                                        | Versión
-------- | -------------------------------------------------- | ----------
[bottle] | Un _microframework_ web que no tiene dependencias. | **0.12.9**

Esta librería también aparece en `requirements.txt`.
Luego, se **deberá** usar este archivo para instalarla con [pip].  
Esto nos permitirá trabajar con la misma versión,
consiguiendo instalaciones **replicables**, sin hacer esfuerzo.  
Bueno, un poco: debemos escribir...

```sh
$ pip install -r requirements.txt
```

En efecto, esto es... _as easy as **py**_. :grinning:

### Preparación

Para encender esto localmente, debes seguir los siguientes pasos.

1. :sheep:
   Clona el repositorio. Luego, accede.

   ```sh
   $ git clone https://github.com/nkawasg/lommebok.git
   $ cd lommebok
   ```

2. :wrench:
   Genera un entorno virtual de Python v3.**X** con [virtualenv].
   En este caso, se llamará `venv`.  
   No olvides que **X** debe ser: {2, 3, 4, 5}.

   ```sh
   $ virtualenv --python=python3.X venv
   ```

3. :arrow_forward:
   Activa el entorno virtual.

   ```sh
   $ source venv/bin/activate
   ```

4. :white_check_mark:
   Instala las dependencias con [pip].

   ```sh
   $ pip install -r requirements.txt
   ```

5. :floppy_disk:
   Ejecuta el _script_ para crear `lommebok.sqlite3`.

   ```sh
   $ python3 script.py
   ```

6. :rocket:
   Enciende, finalmente, el servidor web.

   ```sh
   $ python3 lommebok.py
   ```

7. :tada:
   _Voilà!_  
   La aplicación _debería_ estar escuchando en el [puerto 8080](http://localhost:8080).

[/]:# (Referencias implícitas)

[python]:     http://www.pyzo.org/_images/xkcd_python.png
[bottle]:     https://pypi.python.org/pypi/bottle

[virtualenv]: https://virtualenv.pypa.io/en/stable
[pip]:        https://pip.pypa.io/en/stable
