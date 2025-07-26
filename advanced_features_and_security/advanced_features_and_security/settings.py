# ... (other settings)

# Add 'accounts' to INSTALLED_APPS
INSTALLED_APPS = [
    # ...
    'accounts',
    # ...
]

# Specify the custom user model
AUTH_USER_MODEL = 'accounts.CustomUser'

# ... (rest of settings)