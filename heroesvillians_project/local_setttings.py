# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xfhc=2w88%#3s9gx8w*93*w&@(u^w@d$1t6mo8c0)4ti6&0qfv'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroesvillians_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Basketball3!'
    }
}
