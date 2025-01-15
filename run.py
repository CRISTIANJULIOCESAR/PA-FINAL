from app import create_app

app = create_app()

if __name__ == '__main__':
    # Iniciar en modo debug para desarrollo
    app.run(debug=True)
