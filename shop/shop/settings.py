# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = 'django-insecure-$c#vr(hdywxyt%_p#d5zq9b2ok57q5qvo+&bzfcr0g$(_0ln18'
# DEBUG = True
# ALLOWED_HOSTS = ['*']

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'website',
#     "corsheaders",
#     "rest_framework",  # ✅ add this
# ]

# MIDDLEWARE = [
#     "corsheaders.middleware.CorsMiddleware",  
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'shop.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / 'templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'shop.wsgi.application'

# DATABASES = {
#     # 'default': {
#     #     'ENGINE': 'django.db.backends.mysql',
#     #     'NAME': 'shop',
#     #     'USER': 'root',
#     #     'PASSWORD': '1234',
#     #     'HOST': 'localhost',
#     #     'PORT': '3306',
#     # }

#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# STATIC_URL = 'static/'
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # ✅ Sessions
# SESSION_ENGINE = "django.contrib.sessions.backends.db"
# # SameSite=Lax works with same-origin proxy (Vite) and HTTP dev
# # SESSION_COOKIE_SAMESITE = 'Lax'
# # SESSION_COOKIE_SECURE = False

# # # ✅ CSRF
# # CSRF_COOKIE_SAMESITE = 'Lax'
# # CSRF_COOKIE_SECURE = False
# CORS_ALLOW_CREDENTIALS = True
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:5173",
#     "http://127.0.0.1:5173",
#     "http://localhost:5174",
#     "http://127.0.0.1:5174",
#     "https://e-commerce-frontend-9rhn.onrender.com",
# ]
# CSRF_COOKIE_SAMESITE = 'None'
# CSRF_COOKIE_SECURE = True
# CSRF_TRUSTED_ORIGINS = [
#     "https://e-commerce-frontend-9rhn.onrender.com",
# ]

# # # ✅ CORS
# # # CORS_ALLOW_CREDENTIALS = True
# # # CORS_ALLOWED_ORIGINS = [
# # #     "http://localhost:5173",
# # #     "http://127.0.0.1:5173",
# # "https://e-commerce-frontend-9rhn.onrender.com",
# # # ]

# # ✅ CSRF trusted origins for dev Vite servers
# CSRF_TRUSTED_ORIGINS = [
#     "http://localhost:5173",
#     "http://127.0.0.1:5173",
#     "http://localhost:5174",
#     "http://127.0.0.1:5174",
#     "https://e-commerce-frontend-9rhn.onrender.com",
# ]

# # ✅ DRF Authentication
# REST_FRAMEWORK = {
#     "DEFAULT_AUTHENTICATION_CLASSES": [
#         "website.auth.CsrfExemptSessionAuthentication",  # ✅ custom
#     ],
#     "DEFAULT_PERMISSION_CLASSES": [
#         "rest_framework.permissions.IsAuthenticated",
#     ],
# }

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-$c#vr(hdywxyt%_p#d5zq9b2ok57q5qvo+&bzfcr0g$(_0ln18'
DEBUG = True  # Change to False in production
ALLOWED_HOSTS = ['*']  # or your domain

# ----------------- Installed apps -----------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
    'corsheaders',
    'rest_framework',
]

# ----------------- Middleware -----------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop.wsgi.application'

# ----------------- Database -----------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ----------------- Password validators -----------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ----------------- Internationalization -----------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ----------------- Static files -----------------
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ----------------- Sessions & CSRF -----------------
SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = "None"

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = "None"

# ----------------- CORS -----------------
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
    "https://e-commerce-frontend-9rhn.onrender.com",
]

# ----------------- CSRF trusted origins -----------------
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
    "https://e-commerce-frontend-9rhn.onrender.com",
]

# ----------------- DRF Authentication -----------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "website.auth.CsrfExemptSessionAuthentication",  # custom class
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}
