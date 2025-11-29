# Notes Tracking API — Flask + Sessions

Simple secure backend API for personal note-tracking.
Users can sign up or log in, create notes, edit them, delete them, and paginate through their list.
Each user only sees their own notes — access control locked down.

---

## Features

* Session-based authentication (login persists with cookies)
* Passwords hashed using Bcrypt
* CRUD for notes: create, read, update, delete
* Pagination on `GET /notes`
* SQLite database + Flask-Migrate migrations
* Clean JSON responses for easy frontend integration

---

## Stack

| Part             | Tool          |
| ---------------- | ------------- |
| Framework        | Flask         |
| ORM              | SQLAlchemy    |
| Auth             | Flask-Session |
| Password Hashing | Flask-Bcrypt  |
| DB               | SQLite        |

Runs on **Python 3.8+**

---

## Setup & Run

Clone the repo:

```bash
git clone https://github.com/nevinBoyd/NB-flask-c10-summative-lab-sessions-and-jwt-clients.git
cd NB-flask-c10-summative-lab-sessions-and-jwt-clients/server
```

Install + activate env:

```bash
pipenv install
pipenv shell
```

Database setup:

```bash
flask db upgrade
python seed.py   # optional sample data
```

Run the server:

```bash
python app.py
```

App runs at:
📍 [http://localhost:5555](http://localhost:5555)

---

## Routes

| Method | Endpoint                 | Purpose                        | Auth |
| ------ | ------------------------ | ------------------------------ | ---- |
| POST   | `/signup`                | Create a new user + auto-login | No   |
| POST   | `/login`                 | Login existing user            | No   |
| GET    | `/check_session`         | Verify login session           | Yes  |
| DELETE | `/logout`                | End session                    | Yes  |
| GET    | `/notes?page=&per_page=` | Paginated notes list           | Yes  |
| POST   | `/notes`                 | Create a note                  | Yes  |
| PATCH  | `/notes/<id>`            | Edit a note                    | Yes  |
| DELETE | `/notes/<id>`            | Remove a note                  | Yes  |

---

## Example Requests (Test with curl)

```bash
# Register + login
curl -X POST http://localhost:5555/signup \
-H "Content-Type: application/json" \
-d '{"username": "nev", "password": "123"}' \
-c cookie.txt

# Create a note
curl -X POST http://localhost:5555/notes \
-H "Content-Type: application/json" \
-d '{"content": "Note A"}' \
-b cookie.txt

# Get first page with 1 note per page
curl "http://localhost:5555/notes?page=1&per_page=1" -b cookie.txt
```

---

## Database

Minimal relational setup:

```
User 1 — ∞ Notes
```

---

## Project Structure

```
server/
  app.py
  config.py
  models.py
  seed.py
  routes/
    auth_routes.py
    notes_routes.py
migrations/
client-with-sessions/   # Provided
client-with-jwt/        # Not used
```


