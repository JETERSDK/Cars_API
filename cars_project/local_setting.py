# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6p!g4mu#4am$&7m)q!d8_10$@*)2zix%01)xdwc_ii(m(q38nd'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'M@ximu$70'
    }
}