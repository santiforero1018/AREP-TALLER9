# TALLER 9, LLM CON PYTHON

## DESCRIPCION

Para este trabajo, se realizara una conexión al API de OPENAI con el objetivo de, a travez de codigo, podamos preguntar cualquier cosa a la IA implementada con GPT. 
Cabe aclarar que se requiere de una llave de OPENAI para poder acceder a su API y realizar dichas peticiones.

## PREREQUISISTOS

 - [Python 3.8 o superior](https://www.python.org/downloads/) - Lenguaje de programación empleado para el desarrollo
 - [pip 24](https://pypi.org/project/pip/) - Gestor de paquetes para los programas python
 - [OPENAI API KEY](https://openai.com/) - llave para reemplazar y realizar consultas

## INSTALACION

Para poder iniciar el proyecto, clonamos el repositorio con el siguiente comando

```bash
git clone https://github.com/santiforero1018/AREP-TALLER9
```

cuando se haya clonado, nos movemos dentro del repositorio y se ejecuta el siguiente comando para instalar las librerias correspondientes para el funcionamiento del proyecto

```bash
pip install -r .\requirements.txt
```

si tiene problemas por ejecución de acuerdo a los permisos de usuario, puede usar el siguiente comando

```bash
pip install --user -r .\requirements.txt
```

Preferiblemente, se uso el IDE de [PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows) para correr los programas en mención, por lo que se recomienda el uso de este para la ejecución del proyecto

### Algunos problemas de instalación

Puede que experimente problemas de instalación, en especial con la libreria de chromadb, por lo que se sugiere hacer lo siguiente:

1. dirigirse al [Visual Studio](https://visualstudio.microsoft.com/es/visual-cpp-build-tools/) y descargar el conjunto de herramientas
2. Al descargar, ejecutar el instalador y luego dirigirse a la sección "Desktop development with C++" seleccionarla y luego dar click en instalar
3. Despues de la instalación, ejecutar el siguiente comando `pip install uvicorn chromadb fastapi`

Con esto deberia resolver (en caso de presetnarse este rpoblema instalando chromadb) el problema de instalación generado

## DISEÑO Y PRUEBAS

El diseño consta de 3 archivos:

  1. firstProgram: Este programa realiza una petición sencilla a la API de OPENAI y devuelve una respuesta tal cual fuera preguntarle a CHATGPT
  2. InMemoryPetition: Se utiliza como contexto la información de un repositorio de GitHub para luego con esa información hacer una consulta a ChatGPT para obtener un resultado personalizado.
  3. PineCone: Se usa el archivo "result.txt" copiando el contenido del mismo para crear una base de datos vectorizada en Pinecone, para luego consultar sus vectores y obtener ese contenido como respuesta a la consulta "who is cristiano ronaldo".

Debido a numerosos problemas con la API KEY de OPENAI, no se pudieron tomar las evidencias correspondientes para ilustrar el funcionamiento del codigo, por lo que se le sugiere que si dispone de un API Key, la puede reemplazar en los espacios correspondientes y realizar la ejecución.

## AUTOR
 * Santiago Forero Yate - [santiforero1018](https://github.com/santiforero1018) mi perfil en GitHub
## AGRADECIMIENTOS
 * Especial Agradecimiento al profesor [Luis Daniel Benavides Navarro](https://ldbn.is.escuelaing.edu.co/) por brindar el conocimiento necesario en la realización de este trabajo
