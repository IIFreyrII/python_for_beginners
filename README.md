# Aprendizaje de Python: De Cero a Intermedio

Este repositorio contiene una ruta estructurada para aprender Python desde cero. El propósito es explorar el lenguaje paso a paso, construyendo una base sólida que permita avanzar hacia conceptos de mayor complejidad en el desarrollo de software, estructuración de datos y arquitecturas backend.

## Metodología y Fuentes de Práctica

El núcleo práctico de este aprendizaje se basa principalmente en dos plataformas:
* **freeCodeCamp:** Para comprender los fundamentos, interactuar con bases de datos relacionales y aplicar la teoría en proyectos de backend.
* **Exercism (exercism.org):** Para resolver ejercicios algorítmicos locales mediante la terminal, fortaleciendo la lógica y la limpieza del código con pruebas automatizadas.

El material se organiza de manera progresiva en los siguientes módulos:

- [ ] **01_fundamentos:** Control de flujo (`if`, `for`, `while`), funciones y manipulación de tipos de datos.
- [ ] **02_matematicas_discretas:** Lógica proposicional, teoría de conjuntos y grafos.
- [ ] **03_poo:** Clases, objetos, herencia, encapsulamiento y polimorfismo.
- [ ] **04_estructuras_de_datos:** Implementación nativa de algoritmos de ordenamiento, listas enlazadas, pilas y colas.
- [ ] **05_bases_de_datos:** Interacción con bases de datos relacionales y ejecución de scripts.

---

## Guía de Instalación

Para ejecutar los scripts de este repositorio, es necesario contar con Python 3.10 o superior. A continuación, se detallan las instrucciones para los sistemas operativos más comunes:

### Windows
Existen dos opciones principales:
1. **Microsoft Store:** Busca "Python 3" en la tienda y haz clic en obtener. Esta opción configura automáticamente las variables de entorno.
2. **Instalador Oficial:** Descarga el ejecutable desde [python.org](https://www.python.org/). **Importante:** Durante la instalación, asegúrate de marcar la casilla *"Add Python to PATH"* antes de iniciar el proceso.

### macOS
La forma más sencilla y recomendada para gestionar paquetes en macOS es utilizando [Homebrew](https://brew.sh/):
```bash
brew install python
```
### Linux
Python suele estar integrado en las distribuciones de Linux en versiones 3.xx, no hace falta realizar alguna instalación.

##
Al aprender Python, se puede encontrar algún paquete que querrá ser probado, lo que deriva en la simplicidad de un "pip install" que es una manera sencilla e irresponsable de gestionar paquetes, la cual  puede llevar a distintos errores. Para evitarlo, lo ideal es manejar entornos virtuales.

### 1. Crear entornos virtuales
El primer paso para aislar los paquetes del Sistema Operativo (SO), es crear entornos virtuales.

### UNIX
```
python3.15 -m venv --prompt . .venv
```

### Windows
```
py -3.15 -m venv --prompt . .venv 
```
En dado caso de fallar el anterior, se puede sustituir por otra alternativa:
```
python3.15 -m venv --prompt . .venv
```

### 2. Activar los entornos virtuales
Activar el entorno virtual hará que al escribir ```python```, este apuntará al intérprete en el entorno virtual. Este paso es completamente opcional pero útil.

### Fish shell
```
source .venv/bin/activate.fish
```

### Bash shell
```
source .venv/bin/activate
```

### Powershell
Para la powershell se requieren dos comandos. El primero sólo necesita ejecutarse una vez y reduce la seguridad de la Powershell para permitir la ejecución de scripts con firmas. Sin el primer comando, el segundo no funcionará.
```
Set-ExecutionPolicy RemoteSigned
.venv\Scripts\Activate.ps1
```

### 3. Instalar los paquetes
A este punto, ya debería ser posible usar los entornos virtuales y así evitar conflictos con instalaciones globales.

### Si el entorno virtual está activado
El siguiente comando sirve para instalar paquetes mediante pip
```
python -m pip install {package} --upgrade pip
```

### Si el entorno virtual no está activo

### UNIX
```
.venv/bin/python -m pip install --upgrade pip
```

### Windows
```
.venv\Scripts\python -m pip install --upgrade pip
```
