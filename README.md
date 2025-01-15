# proyecto_final
# StudentOverflow

Este proyecto consiste en un portal web de preguntas y respuestas, inspirado en StackOverflow, donde los estudiantes pueden **registrarse**, **iniciar sesión** y **publicar preguntas** relacionadas con sus materias.

---

## Descripción General

- **Tecnologías**: Python 3, Flask, SQLAlchemy, Flask-Login, Flask-WTF  
- **Objetivo**: Permitir a los estudiantes compartir dudas y recibir ayuda en un entorno colaborativo.  
- **Características principales**:
  1. Registro de usuarios (sign up).
  2. Inicio de sesión (login) y manejo de sesiones.
  3. Creación y visualización de preguntas.
  4. Autorización para que solo usuarios registrados puedan crear preguntas.

---

## Estructura del Proyecto

```
studentoverflow/
├── app/
│   ├── __init__.py      # App factory y configuración de extensiones
│   ├── config.py        # Configuración (cadena de conexión a BD, SECRET_KEY, etc.)
│   ├── forms.py         # Formularios Flask-WTF
│   ├── models.py        # Modelos SQLAlchemy (User, Question, Answer)
│   ├── routes.py        # Rutas (endpoints) de la aplicación
│   ├── static/
│   │   └── css/
│   │       └── styles.css
│   └── templates/
│       ├── ask.html
│       ├── base.html
│       ├── dashboard.html
│       ├── index.html
│       ├── login.html
│       └── register.html
├── documentation/
│   └── db/
│       └── (Aquí irá tu diagrama entidad-relación)
├── create_db.py         # Script para crear y poblar la base de datos
├── run.py               # Punto de entrada para ejecutar la aplicación
├── requirements.txt     # Lista de dependencias
└── README.md            # Este documento
```

---

## Checkpoints y Entregables

A continuación se describen los **checkpoints** y **entregables**, así como dónde se ubican en este repositorio:

### Checkpoint 1: Prototipo y estructura inicial
1. **Entregable 1**:  
   - Documento PDF con el **prototipo de todas las vistas** o pantallas.  
   *(Colocar aquí el enlace al PDF si se encuentra en línea o indicar ruta en el repositorio)*  

2. **Entregable 2**:  
   - **Liga del repositorio público** en GitHub (este repositorio).
   - Estructura inicial del proyecto, archivo `README.md` y `requirements.txt`.

### Checkpoint 2: Diseño inicial de la base de datos y flujos de usuario
1. **Entregable 1**:  
   - **Esquema entidad-relación (ER)** de la base de datos. Se ubica en:  
     ```
     documentation/db/DiagramaER.pdf
     ```
   - Subirlo también como PDF o imagen en el repositorio.

2. **Entregable 2**:  
   - **Diagramas de flujo** de los distintos casos de uso (cómo se registra un usuario, cómo inicia sesión, etc.).  
   - Subirlos sin comprimir en el repositorio (puede ser dentro de `documentation/diagrams`).

### Checkpoint 3: Desarrollo de landing page, login y sign up
1. **Entregable 1**:  
   - **Capturas de pantalla** de:
     - Página de inicio sin sesión iniciada  
     - Página de inicio con sesión iniciada  
     - Pantalla de inicio de sesión (login)  
     - Pantalla de registro de usuario (sign up)  
   - Agregar las capturas en un apartado de la plataforma y/o en el repositorio (por ejemplo, en `documentation/screenshots/`).

2. **Entregable 2**:  
   - **Grabación de pantalla** que muestre el flujo completo de navegación hasta este punto (inicio, registro, login).  
   - *(Coloca aquí el enlace de YouTube u otra plataforma de video si corresponde.)*

### Checkpoint 4: Implementación de autenticación y autorización
1. **Entregable 1**:  
   - Grabación de pantalla mostrando el **flujo completo de registro** de un usuario.  
   - *(Coloca el link de YouTube o plataforma)*

2. **Entregable 2**:  
   - Grabación de pantalla mostrando **inicio de sesión** de un usuario.  
   - *(Coloca el link de YouTube o plataforma)*

3. **Entregable 3**:  
   - Grabación de pantalla mostrando la **persistencia de la sesión** (por ejemplo, si cierras y abres el navegador).  
   - *(Coloca el link de YouTube o plataforma)*

### Checkpoint 5: Implementación de la página inicial de la aplicación
1. **Entregable 1**:  
   - **Capturas de pantalla** de la página inicial mostrando **contenido dinámico** basado en la sesión.  
     - (Ejemplo: cuando el usuario está logueado vs cuando no lo está.)

2. **Entregable 2**:  
   - **Video demostrativo** de cómo la página inicial cambia en función de la sesión del usuario.  
   - *(Coloca aquí el link correspondiente.)*

---

## Instrucciones de Instalación

1. **Clona** este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/studentoverflow.git
   ```
2. Entra al directorio del proyecto e **instala las dependencias**:
   ```bash
   cd studentoverflow
   pip install -r requirements.txt
   ```
   *(Asegúrate de usar un entorno virtual si así lo deseas.)*

3. **Crea la base de datos** (SQLite) y poblarla con datos de prueba:
   ```bash
   python create_db.py
   ```
   Esto creará el archivo `studentoverflow.db` en la carpeta `instance/` (o donde lo especifique tu configuración).

4. **Ejecuta la aplicación**:
   ```bash
   python run.py
   ```
5. **Abre tu navegador** e ingresa a:
   ```
   http://127.0.0.1:5000
   ```

---

## Uso de la Aplicación

- **Landing page**: Muestra un mensaje de bienvenida, con enlaces para Iniciar Sesión o Registrarse.
- **Registro**: Permite crear un nuevo usuario (ingresando un nombre de usuario, email y contraseña).
- **Inicio de Sesión**: Una vez registrado, el usuario puede loguearse e iniciar su sesión.
- **Página de inicio (autenticado)**: Se muestra un listado de preguntas y la opción de crear una nueva pregunta.
- **Crear Pregunta**: Solo para usuarios con sesión iniciada.

---

## Otros Comandos Útiles

- **Recrear la base de datos** en modo de desarrollo (con datos de prueba):
  ```bash
  python create_db.py
  ```
- **Agregar más dependencias**:
  ```bash
  pip install <paquete> 
  pip freeze > requirements.txt
  ```
  (Esto actualizará tu lista de dependencias.)

---

## Enlaces Importantes

*(En esta sección, agrega los enlaces correspondientes a tu proyecto.)*

- **Repositorio GitHub**: [Tu Repositorio](https://github.com/tu-usuario/studentoverflow)  
- **Video Checkpoint 1** (Prototipo y estructura inicial): [Enlace de YouTube](#)  
- **Video Checkpoint 2** (Diseño base de datos y flujos de usuario): [Enlace de YouTube](#)  
- **Video Checkpoint 3** (Landing page, login y sign up): [Enlace de YouTube](#)  
- **Video Checkpoint 4** (Autenticación y autorización): [Enlace de YouTube](#)  
- **Video Checkpoint 5** (Página inicial dinámica): [Enlace de YouTube](#)

*(Reemplaza los “(#)” con tus enlaces reales.)*

---

## Licencia

Este proyecto está bajo la licencia **MIT**. Puedes consultar el archivo [LICENSE](LICENSE) para más detalles (o agregar la licencia de tu preferencia).

---

### ¡Gracias por visitar StudentOverflow!
Si tienes alguna duda o sugerencia, no dudes en abrir un _issue_ en el repositorio de GitHub o contribuir con _pull requests_.