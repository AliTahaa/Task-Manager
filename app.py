from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ali123@localhost/task_manager'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    is_completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    new_task = Task(title=title, user_id=session['user_id'])
    db.session.add(new_task)  # Add task to the session
    db.session.commit()  # Commit the transaction
    return redirect(url_for('dashboard'))  # Redirect to the index page


@app.route('/update', methods=['POST'])
def update_tasks():
    completed_task_ids = request.form.getlist('completed_tasks')  # Get the selected tasks
    user_id = session['user_id']  # Get the current user's ID
    tasks = Task.query.filter_by(user_id=user_id).all()  # Filter tasks by the current user

    for task in tasks:
        if str(task.id) in completed_task_ids:
            task.is_completed = True
        else:
            task.is_completed = False

    db.session.commit()  # Commit the updates
    return redirect(url_for('dashboard'))  # Redirect to the index page


@app.route('/delete/<int:id>')
def delete_task(id):
    task_to_delete = Task.query.get_or_404(id)  # Fetch the task to delete
    db.session.delete(task_to_delete)  # Delete the task from the session
    db.session.commit()  # Commit the transaction
    return redirect(url_for('dashboard'))  # Redirect to the index page

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Check if email is already registered
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "Email already registered!", 400

        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect('/login')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username  # Store username in session
            return redirect(url_for('dashboard'))
        else:
            return "Invalid email or password!", 400

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    tasks = Task.query.filter_by(user_id=session['user_id']).all()
    username = session.get('username')  # Retrieve username from session
    return render_template('index.html', tasks=tasks, username=username)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables if they don't exist
    app.run(debug=True)
