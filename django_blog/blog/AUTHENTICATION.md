# Authentication System Documentation

## Overview

This authentication system provides user registration, login, logout, and basic profile management for the `django_blog` project.

## Features

- **Registration:** Users can register with username, email, and password.
- **Login/Logout:** Uses Django’s secure authentication.
- **Profile:** Authenticated users can view and update their username and email.

## How It Works

- **Registration**: 
  - URL: `/register`
  - View: `register_view`
  - Form: `CustomUserCreationForm` extends Django's form to include email.
  - On success, user is logged in and redirected to `/profile`.

- **Login**: 
  - URL: `/login`
  - View: Django's `LoginView` with custom template.
  - On success, user is redirected to the default or next page.

- **Logout**: 
  - URL: `/logout`
  - View: Django's `LogoutView` with custom template.

- **Profile**:
  - URL: `/profile`
  - View: `profile_view` (requires login).
  - Form: `ProfileUpdateForm` allows updating username and email.

## Security

- **CSRF Protection**: All forms use CSRF tokens.
- **Password Hashing**: Uses Django's built-in hashing.
- **Access Control**: Profile page requires authentication.

## How to Test

1. **Register** at `/register`
2. **Login** at `/login`
3. **Logout** at `/logout`
4. **Edit Profile** at `/profile`

## Extending

To add more profile fields (e.g., profile picture, bio), create a `Profile` model linked with OneToOneField to User and extend the forms/views accordingly.

## Troubleshooting

- If templates do not load, ensure they are in `blog/templates/blog/`.
- If login/logout does not redirect, check `LOGIN_REDIRECT_URL` and `LOGOUT_REDIRECT_URL` in settings.

## Setup

1. Add `'blog'` to `INSTALLED_APPS`.
2. Run `python manage.py migrate`.
3. Create a superuser for admin access if needed.
