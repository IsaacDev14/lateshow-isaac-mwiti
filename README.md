
# Late Show API

A Flask RESTful API for managing Late Show episodes, guests, and their appearances. Built during Phase 4 Code Challenge.

---

## 📁 Project Structure

```
lateshow-isaac-mwiti/
├── app/
│   ├── __init__.py        # Flask app factory + extensions setup
│   ├── models.py          # SQLAlchemy models: Episode, Guest, Appearance
│   ├── routes.py          # API routes (GET, POST, DELETE)
│   ├── seed.py            # Seed script with sample data
├── config.py              # App configuration
├── run.py                 # Entry point (optional)
├── requirements.txt       # Dependencies
├── migrations/            # Alembic migrations
├── .flaskenv              # Flask CLI environment variables
└── README.md              # Project documentation
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/lateshow-isaac-mwiti.git
cd lateshow-isaac-mwiti
```

### 2. Create Virtual Environment and Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run Migrations and Seed the Database

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python -m app.seed
```

### Optional: Use a `.flaskenv` file

Create a `.flaskenv` file to simplify Flask CLI commands:

```
FLASK_APP=app
FLASK_RUN_PORT=5555
```

Then you can just run:

```bash
flask run
```

---

## 🌐 Base URL

All requests should be made to:

```
http://127.0.0.1:5555
```

---

## 📌 API Endpoints

### 🔹 GET `/episodes`

Returns a list of all episodes (short form):

**Example:** `GET http://127.0.0.1:5555/episodes`

```json
[
  {
    "id": 1,
    "date": "1/11/99",
    "number": 1
  }
]
```

---

### 🔹 GET `/episodes/<id>`

Returns an episode and its appearances:

**Example:** `GET http://127.0.0.1:5555/episodes/1`

```json
{
  "id": 1,
  "date": "1/11/99",
  "number": 1,
  "appearances": [
    {
      "id": 1,
      "rating": 4,
      "episode_id": 1,
      "guest_id": 1,
      "guest": {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      },
      "episode": {
        "id": 1,
        "date": "1/11/99",
        "number": 1
      }
    }
  ]
}
```

If not found:

```json
{
  "error": "Episode not found"
}
```

---

### 🔹 DELETE `/episodes/<id>`

Deletes an episode and all its appearances.

Returns:

```json
{}
```

Or:

```json
{
  "error": "Episode not found"
}
```

---

### 🔹 GET `/guests`

Returns all guests:

**Example:** `GET http://127.0.0.1:5555/guests`

```json
[
  {
    "id": 1,
    "name": "Michael J. Fox",
    "occupation": "actor"
  }
]
```

---

### 🔹 POST `/appearances`

Creates a new appearance:

**Example:** `POST http://127.0.0.1:5555/appearances`

**Request Body:**

```json
{
  "rating": 5,
  "episode_id": 2,
  "guest_id": 3
}
```

**Success Response:**

```json
{
  "id": 3,
  "rating": 5,
  "guest_id": 3,
  "episode_id": 2,
  "episode": {
    "id": 2,
    "date": "1/12/99",
    "number": 2
  },
  "guest": {
    "id": 3,
    "name": "Tracey Ullman",
    "occupation": "television actress"
  }
}
```

**Error Response:**

```json
{
  "errors": ["validation errors"]
}
```

---

## 📚 Technologies Used

- Python 3
- Flask
- Flask-RESTful
- Flask-Migrate
- SQLAlchemy
- SQLite

---

## 👤 Author

**Isaac Mwiti Kubai**  
GitHub: [@isaacmwiti](https://github.com/isaacmwiti)

---
