from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegisterForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired(), Length(min=4, max=50)])
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6, max=50)])
    confirm_password = PasswordField('Confirmar contraseña', 
                                     validators=[DataRequired(), EqualTo('password', message='Las contraseñas deben coincidir.')])
    submit = SubmitField('Registrarse')

class LoginForm(FlaskForm):
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6, max=50)])
    submit = SubmitField('Iniciar sesión')

# NUEVO: Formulario para publicar preguntas
class QuestionForm(FlaskForm):
    title = StringField('Título de la pregunta', validators=[DataRequired(), Length(min=5, max=200)])
    body = TextAreaField('Contenido de la pregunta', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Publicar pregunta')
