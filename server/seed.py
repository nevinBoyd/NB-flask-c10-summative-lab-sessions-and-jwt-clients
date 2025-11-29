from app import app
from config import db
from models import User, Note

# Run seeding inside the app context
with app.app_context():

    db.drop_all()

    db.create_all()

    # Seed a demo user
    user = User(username="demo")
    user.set_password("password") 

    db.session.add(user)
    db.session.commit()

    # Seed notes for that user
    notes = [
        Note(title="First Note", content="Seeded note content.", user_id=user.id),
        Note(title="Reminder", content="This is another seeded note.", user_id=user.id),
        Note(title="Ideas", content="Brainstorm session results!", user_id=user.id),
    ]

    db.session.add_all(notes)
    db.session.commit()