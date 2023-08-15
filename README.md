# Repositorio backend CareYoursPets (5ta Devathon-equipo 4)

## 1. Descripción

Este repositorio alberga el código fuente del backend de la plataforma CareYourPets. Para desarrollar este backend nos hemos apoyado en dos marcos de trabajo muy potentes, NestJS y Django Rest.

NestJS es un framework para la construcción de aplicaciones de servidor eficientes y escalables en [Node.js](https://nodejs.org/). Ha sido diseñado para permitir a los desarrolladores aprovechar el desarrollo de JavaScript del lado del servidor utilizando una sintaxis similar a la de Angular.

Por otro lado, [Django Rest](https://www.django-rest-framework.org/) nos permite construir poderosas API web de manera rápida y fácil, siendo este un marco de trabajo de alto nivel en [Python](https://www.python.org/) que fomenta un diseño limpio y pragmático en el desarrollo.

La combinación de estas tecnologías nos permitirá crear un backend fiable, rápido y seguro para CareYourPets.


### 1.1 Características del proyecto

- Usuario
    - Proceso de autenticación para usuarios.
    - CRUD de usuarios.
    - Proceso para restablecer la contraseña.
- mascotas
    - CRUD de mascotas.
- veterinarias
    - CRUD de veterinarias.
    - Proceso de autenticación para veterinarias.
    - Proceso para restablecer la contraseña.



## 2. Instalación en local

Primero debes clonar este repositorio utilizando el siguiente comando en tu consola.

```bash
  git clone https://github.com/Care-Yours-Pets/CareYoursPets-backend.git
```


### 2.1 Inicialización del servidor de desarrollo NestJS

Estos son los pasos para la inicialización del servidor NestJS en local.


- **Paso 1 (requerimientos):** asegúrese de que Node.js (versión >= 16) esté instalado en su sistema operativo.

- **Paso 2 (configurar variables de entorno):** Crear un archivo con el nombre ".env" dentro de la carpeta "users". Dentro de este archivo definimos las variables que vamos a usar. 

    ```bash
    JWT_REFRESH_SECRET=refresh_secret
    JWT_REFRESH_SECRET_EXPIRY=1d
    JWT_ACCESS_SECRET=access_secret
    JWT_ACCESS_SECRET_EXPIRY=120m
    DATABASE_HOST=your-host
    DATABASE_USERNAME=username
    DATABASE_PASSWORD=password
    DATABASE_PORT=port
    DATABASE_NAME=name
    ```

    Para generar la JWT_REFRESH_SECRET y JWT_ACCESS_SECRET se usa el siguiente comando.

    ```bash
    node -e "console.log(require('crypto').randomBytes(256).toString('base64'));"
    ```

- **Paso 3 (instalar dependencias):** Usaremos NPM como gestor de libreria y vamos a instalar las dependencias necesarias para el correcto funcionamiento del framework:

    - bcrypt
    - swagger
    - class-validator
    - class-transformer
    - typeorm
    - jwt
    - passport y passport-jwt
    - config
    - mapped-types

    Luego instalamos las dependencias del package.json con el siguiente comando.

    ```bash
    npm install
    ```

  Otras dependencias que se requieren es EsLint que viene pre-instalado en el proyecto.



- **Paso 4 (iniciar el servidor):** Iremos a la carpeta del proyecto.

    ```bash
    cd users
    ```

  Por ultimo iniciamo el servidor.

    ```bash
    #Ejecutar la aplicación
    npm run start

    #Para ver los cambios en tus archivos
    npm run start:dev
    ```

### 2.2 Inicialización del servidor de desarrollo Django rest

Estos son los pasos para la inicialización del servidor NestJS en local.

- **Paso 1 (requerimientos):** asegúrese de que Python esté instalado en su sistema operativo.

- **Paso 2 (configurar variables de entorno):** se debe crear un archivo con el nombre ".env" dentro de la carpeta "veterinary". Dentro de este archivo definimos una variable "SECRET_KEY", el valor de esta variable lo obtendremos escribiendo en orden los siguientes comandos en tu consola.

    ```bash
    #Primer comando
    python

    #Segundo comando
    from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())
    ```
    El ultimo comando retorna el valor de la "SECRET_KEY" que deberas copiar en el archivo ".env".

- **Paso 3 (instalar dependencias):** para instalar las teconologias y paquetes que usa el proyecto usa el siguiente comando. Asegurate de estar dentro de la carpeta "backend_djangorest".

    ```bash
    pip install -r "requirements.txt"
    ```

- **Paso 4 (realizar migraciones):** migramos los modelos del proyecto necesarios para el funcionamiento del servidor con el siguiente comando.

    ```bash
    python manage.py migrate
    ```

- **Paso 5 (Iniciar el servidor):** para iniciar el servidor de manera local ejecuta el siguiente comando.

    ```bash
    python manage.py runserver
    ```

Para correr las pruebas unitarias del código "veterinary" ejecuta el siguiente comando.

```bash
python manage.py test
```


## 3. Integrantes del repositorio
- [Carlos Vega](https://github.com/temeriamos)
- [Carlos Andres Aguirre](https://github.com/The-Asintota)
- [Diego](https://github.com/sistemasitpro)