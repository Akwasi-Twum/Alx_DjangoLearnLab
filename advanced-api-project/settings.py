# ... existing imports ...
INSTALLED_APPS = [
    # Default Django apps...
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps
    'rest_framework',
    # Your API app
    'api',
]

# Using default SQLite DB (no changes needed unless you want another DB)
# ... rest of the settings file ...