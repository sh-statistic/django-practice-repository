# Phonebook Django Project

This is a simple Django project named "phonebook_django" with an app called "concat". The app consists of two models: `Phone` and `Information`.

## Project Structure

```
phonebook_django/
├── concat/
│   ├── migrations/
│   │   └── ...
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── phonebook_django/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py
```

## Models

### 1. Phone Model

- Fields:
  - `phone_number`: CharField to store the phone number.

### 2. Information Model

- Fields:
  - `first_name`: CharField to store the name of the contact.
  - `last_name`: CharField to store the name of the contact.
  - `address`: TextField to store the address of the contact.

## Setup

1. Clone the repository:

   ```
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```
   cd phonebook_django
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```


4. Apply migrations:

   ```
   python manage.py migrate
   ```

5. Create a superuser:

   ```
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```
   python manage.py runserver
   ```

7. Access the admin interface at `http://127.0.0.1:8000/admin/` to manage the `Phone` and `Information` models.


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.
