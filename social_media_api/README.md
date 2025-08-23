# Social Media API

## Overview

A Django REST Framework-based Social Media API with user authentication, profile management, and token-based access.

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Akwasi-Twum/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab/social_media_api
   ```

2. **Install Dependencies:**
   ```bash
   pip install django djangorestframework
   ```

3. **Apply Migrations:**
   ```bash
   python manage.py makemigrations accounts
   python manage.py migrate
   ```

4. **Create Superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- **Register:** `POST /accounts/register/`
- **Login:** `POST /accounts/login/`
- **Profile:** `GET/PUT /accounts/profile/` (Requires Token)

Use token authentication for endpoints that require authentication.

## User Model

- **username**: Unique identifier for each user.
- **email**: Email address.
- **bio**: Short biography.
- **profile_picture**: Image field for profile picture.
- **followers**: ManyToMany field for user followers (non-symmetrical).

## Testing

- Use [Postman](https://www.postman.com/) or [httpie](https://httpie.io/) to test registration, login, and profile endpoints.
- Tokens will be returned on registration/login and must be included in the `Authorization` header for authenticated requests.

## Notes

- Change `SECRET_KEY` in `settings.py` to a secure value before deploying.
- Profile picture uploads require proper media configuration in production.
