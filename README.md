# Django To-Do App

A simple Django-based To-Do list application that allows users to manage tasks by creating, updating, deleting, and viewing them. The app is built using Django's class-based views (CBVs) and follows the Model-View-Template (MVT) architecture. Users must log in to interact with the tasks, and tasks are stored in a SQLite database.

## Features
- User authentication via login.
- Create, update, and delete tasks.
- List all tasks in a user-friendly interface.
- Tasks are stored with a title and completion status.
- Authentication is required to interact with tasks.

## Project Structure

```
├── core
│   ├── asgi.py                 # ASGI application entry point.
│   ├── __init__.py
│   ├── settings.py             # Django project settings.
│   ├── urls.py                 # URL routing for the project.
│   ├── wsgi.py                 # WSGI application entry point.
│   └── __pycache__             # Compiled Python files.
├── manage.py                   # Django's command-line utility for managing the app.
├── templates
│   ├── registration
│   │   └── login.html          # Login template for user authentication.
│   ├── todo
│   │   ├── task_form.html      # Form to create a new task.
│   │   ├── task_list.html      # Displays the list of tasks.
│   │   └── task_update.html    # Form to update an existing task.
├── todo
│   ├── admin.py                # Admin interface for managing tasks.
│   ├── apps.py                 # Configuration for the todo app.
│   ├── models.py               # Database models for the To-Do tasks.
│   ├── migrations              # Database migrations for task model.
│   ├── urls.py                 # URL routing for the todo app.
│   ├── views.py                # Views handling the task management logic.
│   └── __pycache__             # Compiled Python files for the todo app.
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Amirhamidi2001/django-to-do-app
   cd django-to-do-app
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser to access the Django admin interface (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Navigate to `http://127.0.0.1:8000/` in your web browser to use the app.

## Usage

- **Login**: Use the login page at `/accounts/login/` to authenticate.
- **Task List**: After logging in, you can view all tasks at `/todo/`.
- **Create a Task**: To add a new task, visit `/todo/new/`.
- **Update a Task**: Click on any task to update its completion status at `/todo/update/<task_id>/`.
- **Delete a Task**: Click on any task to delete it at `/todo/delete/<task_id>/`.

## Technologies Used
- Python 3.x
- Django 4.x
- SQLite (default database for development)
- HTML5, CSS (for the front-end templates)

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push to your forked repository.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django documentation: https://docs.djangoproject.com/
- SQLite documentation: https://www.sqlite.org/

---

Feel free to customize the README further as needed for your specific project setup!