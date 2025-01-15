from app import create_app

app = create_app()

if __name__ == '__main__':
    # Ejecutar la app en modo debug (solo para desarrollo)
    app.run(debug=True)
