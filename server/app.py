from config import create_app, db
from routes.auth_routes import auth_bp

app = create_app()

app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
