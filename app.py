from flask import Flask, render_template, request, redirect, url_for, session, flash
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
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    priority = db.Column(db.Enum('Low', 'Medium', 'High'), nullable=False, default='Medium')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_completed = db.Column(db.Boolean, default=False)  # Add this line

    def __repr__(self):
        return f"<Task {self.title}, Priority: {self.priority}>"


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/add', methods=['POST'])
def add_task():
    if 'user_id' not in session:
        flash('Please log in to add a task.', 'warning')
        return redirect(url_for('login'))

    title = request.form['title']
    description = request.form.get('description', '')
    priority = request.form['priority']
    user_id = session['user_id']

    new_task = Task(title=title, description=description, priority=priority, user_id=user_id)
    db.session.add(new_task)
    db.session.commit()

    flash('Task added successfully!', 'success')
    return redirect(url_for('dashboard'))





@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('dashboard'))

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
        flash('Please log in to view your dashboard.', 'warning')
        return redirect(url_for('login'))

    # Use positional arguments for `case` whens
    tasks = Task.query.filter_by(user_id=session['user_id']).order_by(
        db.case(
            (Task.priority == 'High', 1),
            (Task.priority == 'Medium', 2),
            (Task.priority == 'Low', 3)
        )
    ).all()

    username = session.get('username')
    return render_template('index.html', username=username, tasks=tasks)


@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form.get('description', '')
        task.priority = request.form['priority']
        db.session.commit()

        flash('Task updated successfully!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('edit_task.html', task=task)


@app.route('/complete_task/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    if 'user_id' not in session:
        flash('Please log in to complete tasks.', 'warning')
        return redirect(url_for('login'))

    # Fetch the task
    task = Task.query.get(task_id)
    if task and task.user_id == session['user_id']:
        # Toggle the completed status
        task.is_completed = not task.is_completed
        db.session.commit()  # Save the change to the database
        flash('Task updated successfully!', 'success')
    else:
        flash('Task not found or unauthorized action.', 'danger')

    return redirect(url_for('dashboard'))



@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables if they don't exist
    app.run(debug=True)
