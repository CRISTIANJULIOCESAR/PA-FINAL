from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from . import db, login_manager
from .models import User, Question
from .forms import RegisterForm, LoginForm, QuestionForm

main = Blueprint('main', __name__)

@login_manager.user_loader
def load_user(user_id):
    """
    Función requerida por Flask-Login para cargar el usuario a partir de su id.
    """
    return User.query.get(int(user_id))

@main.route('/')
def index():
    """
    Página principal:
    - Si no hay sesión iniciada, se muestra una pantalla de bienvenida.
    - Si hay sesión, se muestra el dashboard con las preguntas.
    """
    if current_user.is_authenticated:
        questions = Question.query.all()
        return render_template('dashboard.html', questions=questions)
    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()

        flash('¡Te has registrado exitosamente!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Has iniciado sesión correctamente.', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Credenciales incorrectas. Intenta de nuevo.', 'danger')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('main.index'))

# NUEVO: Ruta para crear una pregunta
@main.route('/ask', methods=['GET', 'POST'])
@login_required
def ask():
    form = QuestionForm()
    if form.validate_on_submit():
        # Crear la pregunta y guardarla en la BD
        new_question = Question(
            title=form.title.data,
            body=form.body.data,
            user_id=current_user.id  # El usuario actual es el autor
        )
        db.session.add(new_question)
        db.session.commit()

        flash('¡Tu pregunta ha sido publicada!', 'success')
        return redirect(url_for('main.index'))
    
    return render_template('ask.html', form=form)

