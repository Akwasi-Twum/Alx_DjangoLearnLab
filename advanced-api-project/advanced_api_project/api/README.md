# API Book Views Documentation

This API provides CRUD endpoints for the `Book` model using Django REST Framework's generic views.

## Endpoints

- `GET /books/`: List all books (public)
- `GET /books/<id>/`: Retrieve a single book (public)
- `POST /books/create/`: Create a new book (authenticated users only)
- `PUT/PATCH /books/<id>/update/`: Update a book (authenticated users only)
- `DELETE /books/<id>/delete/`: Delete a book (authenticated users only)

## Permissions

- **List & Detail**: Accessible to all users.
- **Create, Update, Delete**: Only accessible to authenticated users.

## Customizations

- `perform_create` and `perform_update` hooks in views for custom logic.
- Search filtering enabled for book list.
- Permission classes protect sensitive endpoints.

## Testing

Test endpoints with tools like Postman or curl. Check permission enforcement by using and omitting credentials.

## Extending

- Add custom permission classes in `api/views.py` as needed.
- Add more filters or search fields for advanced queries.
