# Django Web App

This project is a side project inspired by [Andreas Jud's YouTube tutorial](https://youtube.com/playlist?list=PL5E1F5cTSTtTAIw_lBp1hE8nAKfCXgUpW&si=8Y58O9fA9CqtUC5V). It demonstrates a social media application with functionalities like posting, commenting, liking, user authentication, and profile management, built using Django and modern web technologies.

## Features

- User authentication with Django allauth:
  - New user registration
  - Existing user login
  - Edit user profile
- Post management:
  - Create, edit, delete posts
  - Add images to posts
- Comment system:
  - Add comments and replies
  - Like comments and replies
  - Edit and delete comments/replies
- Like system for posts, comments, and replies
- Dynamic front-end interactions using HTMX

## Technology Stack

- **Python**: 3.12
- **Django**: with allauth, ORM, HTMX
- **HTML/CSS**: For UI design
- **Pre-commit**: Ensures code quality with hooks like `isort` and `black`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/verna0214/web_app_django.git
   ```

2. Navigate to the project directory:
   ```bash
   cd web_app_django
   ```

3. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

4. Activate the Poetry environment:
   ```bash
   poetry shell
   ```

5. Run database migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and navigate to `http://127.0.0.1:8000` to view the application.

## Admin & Test User Credentials

For testing and development purposes, the following accounts are available:
| Role | Username | Email  | Password | Access Level |
|----------|----------|----------|----------|----------|
| Superuser | admin | admin@example.com | Ab123456! | Full access (admin panel & API) |
| Test User | user | user@example.com  | Ab123456! | Regular user (basic functionalities) |

### Admin Panel URL
http://127.0.0.1:8000/admin/

If you need to manually create a superuser, use the following command:
   ```bash
   python manage.py createssuperuser
   ```


## Pre-commit Setup

This project uses `pre-commit` hooks to maintain code quality and consistency. Hooks include tools like `isort` for sorting imports and `black` for code formatting.

### Setting up pre-commit

1. Install `pre-commit` if you haven't already:
   ```bash
   pip install pre-commit
   ```

2. Install the hooks defined in `.pre-commit-config.yaml`:
   ```bash
   pre-commit install
   ```

3. Run the hooks manually (optional):
   ```bash
   pre-commit run --all-files
   ```

### Pre-commit in Action

- On each commit, the hooks will automatically check your code for formatting and other issues.
- If any issues are found, `pre-commit` will attempt to fix them or prevent the commit.

## Acknowledgments

This project is based on the tutorial by [Andreas Jud](https://youtube.com/playlist?list=PL5E1F5cTSTtTAIw_lBp1hE8nAKfCXgUpW&si=8Y58O9fA9CqtUC5V). Special thanks for providing a clear and insightful guide to building Django applications.
