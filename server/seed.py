from config import db, create_app
from models import User, Note

# Create app context so db can be used
app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Example seed data (optional, minimal and realistic)
    user = User(username="testuser")
    user.set_password("test123")

    db.session.add(user)
    db.session.commit()

    note1 = Note(title="First Note", content="Seeded note content.", user_id=user.id)
    note2 = Note(title="Reminder", content="This is another seeded note.", user_id=user.id)

    db.session.add_all([note1, note2])
    db.session.commit()
