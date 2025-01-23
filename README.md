# Task Manager

## Overview
The **Task Manager** is a web application designed to streamline personal or team task management. It allows users to create, manage, and track tasks efficiently with features like task prioritization, authentication, and dynamic task updates. The application is built with Python (Flask) for the backend and utilizes a modern, responsive user interface for an intuitive experience.

---

## Features

### 1. User Authentication
- **Login & Registration**: Users can securely log in and register.
- **Session Management**: Tracks user sessions for personalized task data.

### 2. Task Management
- **Add Tasks**: Create tasks with a title, description, and priority level.
- **Edit Tasks**: Modify task details as needed.
- **Delete Tasks**: Remove tasks that are no longer required.
- **Mark as Completed**: Checkbox to mark tasks as completed.

### 3. Task Display
- **Dynamic Task List**: Displays all tasks with their priority and status.
- **Sort by Priority**: View tasks categorized by priority levels (Low, Medium, High).
- **Responsive Design**: Adapts to different screen sizes for desktop and mobile views.

### 4. Accessibility
- **Logout Button**: Positioned for easy access at the top right.
- **Interactive Feedback**: Buttons and input fields provide visual cues for user interaction.

---

## Technologies Used

### Backend
- **Flask**: Lightweight Python web framework for backend logic.
- **Session Management**: Tracks authenticated users.

### Frontend
- **HTML**: Markup for the structure.
- **CSS**: Styled for a modern, professional appearance.
- **JavaScript**: Handles dynamic interactions.

### Database
- **SQLite/MySQL**: Stores user and task data securely.

---

## Folder Structure
```
project-folder/
│
├── app.py                    # Main Flask application file
├── templates/                # HTML templates
│   ├── edit_task.html        # Edit Task
│   ├── index.html            # Task management page
│   ├── login.html            # Login page
│   ├── register.html         # Registration page
│
├── static/                   # Static assets
│   ├── script.js             # JavaScript for interactivity
│   ├── styles.css            # CSS for styling
│
├── instance/
│   ├── tasks.db               # MySQL database
```

---

## Setup Instructions

1. **Clone the Repository**
```bash
git clone https://github.com/AliTahaa/Task-Manager.git
cd Task-Manager
```

2. **Create a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the Application**
```bash
python app.py
```

5. **Access the App**
- Open a browser and navigate to: `http://127.0.0.1:5000`

---

## Usage

1. **Register/Login**
   - Register if you’re a new user, or log in with your existing credentials.

2. **Manage Tasks**
   - Use the task form to add tasks with a title, description, and priority.
   - Edit or delete tasks as needed.
   - Mark tasks as completed by selecting the checkbox.

3. **Logout**
   - Click the logout button in the top right corner to securely end your session.

---

## Screenshots

### Register Page
![Register Page](https://github.com/user-attachments/assets/3471991d-8934-43be-be2f-7541a1f63bd2)

### Login Page
![Login Page](https://github.com/user-attachments/assets/1df200fd-29c2-4218-b2e2-f1fd0ab68cba)

### Task List
![Task List](https://github.com/user-attachments/assets/790b785b-c4e1-4812-8aa3-49a65c5d7536)

---

## Future Enhancements

1. **Search and Filter**: Add the ability to search tasks by title or filter by completion status.
2. **Deadline Tracking**: Include deadlines with reminders for tasks.
3. **Collaborative Features**: Allow multiple users to collaborate on tasks.
4. **Mobile App Integration**: Develop a mobile version of the app.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contribution
Contributions are welcome! Feel free to submit a pull request or open an issue to discuss ideas and improvements.

---

## Contact
For any questions or support, please reach out:
- **Email**: am521144@gmail.com
