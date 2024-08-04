from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tabelname__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Todo(db.Model):
    __tablename__ = "todo"

    id = db.Column(db.Integer, primary_key = True)
    userId = db.Column(db.String(32), nullable = False)
    content = db.Column(db.Text(), nullable = False)
    done = db.Column(db.Boolean, default=False, nullable=False)