# Web App with Django

A side project inspired by the [Andreas Jud's Django tutorial series](https://youtube.com/playlist?list=PL5E1F5cTSTtTAIw_lBp1hE8nAKfCXgUpW&si=8Y58O9fA9CqtUC5V). This application is a feature-rich web app built using Django and other modern web technologies.

## Features

- **User Authentication:**
  - New user registration
  - Existing user login/logout
  - User profile editing

- **Posts and Interactions:**
  - Create, edit, and delete posts with image support
  - Comment and reply to posts
  - Like posts, comments, and replies

- **Dynamic Updates:**
  - Integration with `htmx` for dynamic content updates
  - Seamless interactions without full-page reloads

## Technologies Used

- **Python:** Version 3.13
- **Django Framework:** Includes the use of:
  - `django-allauth` for authentication
  - Django ORM for database interactions
  - `htmx` for dynamic content

## Installation and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/verna0214/web_app_django.git
   cd web_app_django
   ```

2. Install dependencies using Poetry:

   ```bash
   poetry install
   ```

3. Activate the Poetry environment:

   ```bash
   poetry shell
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

5. Open your web browser and navigate to:

   ```
   http://127.0.0.1:8000/
   ```

## Acknowledgements

This project is based on the tutorial series by Andreas Jud. You can find the original series [here](https://youtube.com/playlist?list=PL5E1F5cTSTtTAIw_lBp1hE8nAKfCXgUpW&si=8Y58O9fA9CqtUC5V).
