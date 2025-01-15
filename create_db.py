"""
Script para crear la base de datos y sus tablas a partir de los modelos definidos
en app/models.py. También (opcionalmente) inserta datos de prueba.
"""

from app import create_app, db
from app.models import User, Question, Answer
from werkzeug.security import generate_password_hash

def create_database_and_tables():
    """
    Crea la base de datos y todas las tablas definidas en los modelos.
    """
    app = create_app()
    with app.app_context():
        print("Creando tablas en la base de datos...")
        db.drop_all()    # En desarrollo, borra todo antes de crear (opcional)
        db.create_all()
        print("Tablas creadas con éxito.")

def insert_sample_data():
    """
    Inserta algunos datos de ejemplo para verificar el correcto funcionamiento.
    """
    app = create_app()
    with app.app_context():
        print("Insertando datos de prueba...")

        # Crear usuarios (usamos pbkdf2:sha256, no 'sha256' simple)
        user1 = User(
            username="alice",
            email="alice@example.com",
            password=generate_password_hash("alice123", method='pbkdf2:sha256')
        )
        user2 = User(
            username="bob",
            email="bob@example.com",
            password=generate_password_hash("bob123", method='pbkdf2:sha256')
        )
        db.session.add_all([user1, user2])
        db.session.commit()

        # Crear preguntas
        question1 = Question(
            title="¿Qué es Python?",
            body="Explicación básica de Python.",
            user_id=user1.id
        )
        question2 = Question(
            title="¿Cómo usar Flask?",
            body="Necesito ayuda con Flask y rutas.",
            user_id=user1.id
        )
        question3 = Question(
            title="¿Qué son las listas en Python?",
            body="No entiendo muy bien las listas, ¿alguien puede ayudarme?",
            user_id=user2.id
        )
        db.session.add_all([question1, question2, question3])
        db.session.commit()

        # Crear respuestas
        answer1 = Answer(
            body="Python es un lenguaje de programación de alto nivel.",
            question_id=question1.id,
            user_id=user2.id
        )
        answer2 = Answer(
            body="Para usar Flask, necesitas instalarlo y luego crear un objeto Flask en tu archivo principal.",
            question_id=question2.id,
            user_id=user2.id
        )
        db.session.add_all([answer1, answer2])
        db.session.commit()

        print("Datos de prueba insertados correctamente.")

if __name__ == "__main__":
    # Paso 1: Crear BD y tablas
    create_database_and_tables()

    # Paso 2 (opcional): Insertar datos de ejemplo
    insert_sample_data()
