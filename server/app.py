from config import create_app, db
from routes.auth_routes import auth_bp
from routes.notes_routes import notes_bp

app = create_app()

app.register_blueprint(auth_bp)
app.register_blueprint(notes_bp)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
