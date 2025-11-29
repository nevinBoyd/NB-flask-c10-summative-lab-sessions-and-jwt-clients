from flask import Blueprint, request, jsonify, session
from config import db
from models import Note

notes_bp = Blueprint('notes_bp', __name__)

def require_login():
    user_id = session.get('user_id')
    if not user_id:
        return None, jsonify({"error": "Unauthorized"}), 401
    return user_id, None, None

@notes_bp.route('/notes', methods=['GET'])
def get_notes():
    user_id, error, status = require_login()
    if error:
        return error, status

    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)

    pagination = db.paginate(
        Note.query.filter_by(user_id=user_id).order_by(Note.id),
        page=page,
        per_page=per_page,
        error_out=False
    )

    return jsonify({
        "items": [note.to_dict() for note in pagination.items],
        "total": pagination.total,
        "page": pagination.page,
        "pages": pagination.pages,
        "per_page": pagination.per_page
    }), 200

@notes_bp.route('/notes', methods=['POST'])
def create_note():
    user_id, error, status = require_login()
    if error:
        return error, status

    data = request.get_json()
    content = data.get('content')

    if not content:
        return jsonify({"error": "Content required"}), 400

    title = data.get("title", content)
    new_note = Note(title=title, content=content, user_id=user_id)

    db.session.add(new_note)
    db.session.commit()

    return jsonify(new_note.to_dict()), 201

@notes_bp.route('/notes/<int:note_id>', methods=['PATCH'])
def update_note(note_id):
    user_id, error, status = require_login()
    if error:
        return error, status

    note = Note.query.get(note_id)
    if not note or note.user_id != user_id:
        return jsonify({"error": "Not found"}), 404

    data = request.get_json()
    content = data.get('content')

    if content:
        note.content = content
        db.session.commit()

    return jsonify(note.to_dict()), 200

@notes_bp.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    user_id, error, status = require_login()
    if error:
        return error, status

    note = Note.query.get(note_id)
    if not note or note.user_id != user_id:
        return jsonify({"error": "Not found"}), 404

    db.session.delete(note)
    db.session.commit()

    return '', 204
