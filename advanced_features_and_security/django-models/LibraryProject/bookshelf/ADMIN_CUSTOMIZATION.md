# Django Admin Customization for Book Model

This guide documents the steps taken to enhance the Django admin interface for the `Book` model in the bookshelf app.

## Steps Performed

1. **Registered the Book Model:**
   - Edited `bookshelf/admin.py` to register the `Book` model, enabling management via the Django admin panel.

2. **Customized the Admin List View:**
   - Implemented a custom `BookAdmin` class to:
     - Show `title`, `author`, and `publication_year` in the list view.
     - Add filter options for `publication_year` and `author`.
     - Enable search functionality for `title` and `author`.

## Setup Instructions

1. Ensure your app (`bookshelf`) is listed under `INSTALLED_APPS` in `LibraryProject/settings.py`.
2. Run migrations if you haven't:
    ```bash
    python manage.py makemigrations bookshelf
    python manage.py migrate
    ```
3. Create a superuser if needed:
    ```bash
    python manage.py createsuperuser
    ```
4. Start the development server:
    ```bash
    python manage.py runserver
    ```
5. Log into the admin interface at `http://localhost:8000/admin/` and verify the updated Book model management experience.

## Notes

- The admin customization improves efficiency for librarians and staff by making it easier to find, edit, and filter books.
- You can further extend `BookAdmin` by adding more fields, filters, or custom actions as needed.
