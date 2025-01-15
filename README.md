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

Todos los entregrables etan en el FOLDER DE  link de [Tu Repositorio]([https://github.com/tu-usuario/studentoverflow](https://github.com/CRISTIANJULIOCESAR/PA-FINAL/tree/main/Entregables(E)%20y%20checkpoints(CP))  

## Enlaces Importantes

*(En esta sección, agrega los enlaces correspondientes a tu proyecto.)*

- **Repositorio GitHub**: [Tu Repositorio](https://github.com/tu-usuario/studentoverflow)  
- **Video GENERADOS:

# Videos Generados



## **E2: Grabación de pantalla**
Grabación de pantalla que muestra el flujo completo de la plataforma. Este video incluye los mismos pasos que el video anterior.  
[![E2 Video](https://img.youtube.com/vi/Hv077kkot1s/0.jpg)](https://youtu.be/Hv077kkot1s)

---

## **E3: Entregable 3**
Grabación de pantalla que muestra la persistencia de la sesión del usuario.  
**Descripción:** La sesión permanece activa aunque el usuario recargue la página, cierre temporalmente la aplicación o realice otras acciones sin necesidad de iniciar sesión nuevamente. Se demuestra con dos usuarios para ilustrar este comportamiento.  
[![E3 Video](https://img.youtube.com/vi/TEBXrVvOjT8/0.jpg)](https://youtu.be/TEBXrVvOjT8)



---

## Licencia

Este proyecto está bajo la licencia **MIT**. Puedes consultar el archivo [LICENSE](LICENSE) para más detalles (o agregar la licencia de tu preferencia).

---

### ¡Gracias por visitar StudentOverflow!
Si tienes alguna duda o sugerencia, no dudes en abrir un _issue_ en el repositorio de GitHub o contribuir con _pull requests_.
