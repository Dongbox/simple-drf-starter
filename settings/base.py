"""
Base settings to build other settings files upon.
"""
import datetime
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
# apps/
APPS_DIR = BASE_DIR / "apps"

env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(BASE_DIR / ".env"))

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)
# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "Asia/Shanghai"
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/dev/ref/settings/#languages
# from django.utils.translation import gettext_lazy as _
# LANGUAGES = [
#     ('en', _('English')),
#     ('pt-br', _('Português')),
# ]
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(BASE_DIR / "locale")]

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(BASE_DIR / "db.sqlite3"),
    }
}

# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DEFAULT_AUTO_FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.humanize", # Handy template tags
    "django.contrib.admin",
]
THIRD_PARTY_APPS = [
    "rest_framework",
    "corsheaders",
    "drf_spectacular",
]

LOCAL_APPS = [
    "users",
    # Your stuff: custom apps go here
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    # `Argon2PasswordHasher`是一种现代的密码哈希算法，它使用Argon2算法。它被认为是当前最安全的选择之一。
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
# 当用户设置或更改密码时，这些验证器会运行，以确保密码符合安全性要求。
AUTH_PASSWORD_VALIDATORS = [
    # UserAttributeSimilarityValidator: 检查密码是否与用户的属性（如用户名、电子邮件地址等）相似。
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    # MinimumLengthValidator: 检查密码的长度是否达到或超过一定的最小值。
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    # CommonPasswordValidator: 检查密码是否是常见密码列表中的一个。
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    # NumericPasswordValidator: 检查密码是否只是数字。
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
# 中间件是一个轻量级、低级的插件系统，用于全局改变Django的输入或输出。
# 每个中间件组件都负责处理请求或响应的一小部分，这些组件按照在MIDDLEWARE设置中定义的顺序依次处理。
# 每个组件可以对请求或响应进行处理，然后将其传递给下一个中间件组件。
MIDDLEWARE = [
    # SecurityMiddleware 这个中间件为了提供一些安全增强，如XSS (跨站脚本) 防护。
    "django.middleware.security.SecurityMiddleware",
    # CorsMiddleware 处理跨域资源共享（CORS）的头信息。这在前后端分离的架构中尤其重要，允许来自不同域的请求访问资源。
    "corsheaders.middleware.CorsMiddleware",
    # WhiteNoise中间件用于在Django应用中高效地提供静态文件。它可以在生产环境中代替使用专用的服务器或CDN来提供静态文件。
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # SessionMiddleware 管理会话。它处理用户的session数据。
    "django.contrib.sessions.middleware.SessionMiddleware",
    # LocaleMiddleware 用于国际化和本地化。它根据用户的请求和设置来确定最合适的语言和时区。
    "django.middleware.locale.LocaleMiddleware",
    # CommonMiddleware 提供了一些常用的中间件功能，如处理HTTP中的APPEND_SLASH和PREPEND_WWW设置。
    "django.middleware.common.CommonMiddleware",
    # CsrfViewMiddleware 这个中间件用于跨站请求伪造（CSRF）保护。它确保在处理POST请求时，确保请求是合法的。
    "django.middleware.csrf.CsrfViewMiddleware",
    # AuthenticationMiddleware 这是一个用于处理用户验证的中间件。它将用户与其请求关联起来。
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # MessageMiddleware 用于在请求之间存储一次性的消息。这允许你在请求之后向用户显示一次性通知或提示。
    "django.contrib.messages.middleware.MessageMiddleware",
    # XFrameOptionsMiddleware 为了防止点击劫持，这个中间件通过设置X-Frame-Options头来控制页面是否可以被嵌套在<frame>或<iframe>标签内。
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # 自定义MIDDLEWARE
    "config.middleware.CustomExceptionMiddleware",
]

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
# 当你运行 python manage.py collectstatic 命令时，所有的静态文件会被复制到 STATIC_ROOT 目录。
# 这个设置通常用于生产环境，因为在生产环境中，你通常会将所有的静态文件放在一个单独的服务器或者CDN上。
STATIC_ROOT = str(BASE_DIR / "staticfiles")
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
# STATIC_URL 是用于构建静态文件URL的前缀。这是告诉Django，在模板或视图中引用静态文件时，应该使用哪个URL前缀。
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
# STATICFILES_DIRS 是一个包含文件系统路径的列表，这些路径应该包含你想要在不同位置手动管理的静态文件。
# 它让你可以在不同的地方存储静态文件，而不仅仅是每个app的 static 目录。
# STATICFILES_DIRS = [str(APPS_DIR / "static")]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
# STATICFILES_FINDERS 是Django用来查找静态文件的引擎列表。
# 当你使用 collectstatic 命令时，Django会使用这些查找引擎来找出所有的静态文件，然后将它们复制到 STATIC_ROOT 目录。
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",  # 这个查找器会在 STATICFILES_DIRS 设置的所有目录中搜索静态文件。
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",  # 这个查找器会在 STATICFILES_DIRS 设置的所有目录中搜索静态文件。
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR / "media")
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
# TEMPLATES 是一个包含模板引擎配置的字典列表。每个字典代表一个模板引擎的配置。
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        # BACKEND: 指定使用的模板引擎。
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#dirs
        # DIRS: 指定一个包含文件系统路径的列表，这些路径是Django在查找模板时应该搜索的。
        "DIRS": [],
        # https://docs.djangoproject.com/en/dev/ref/settings/#app-dirs
        # APP_DIRS: 一个布尔值，如果设置为True，Django将在每个已安装的应用程序的 templates 子目录中查找模板
        "APP_DIRS": True,
        # 这是一个包含各种可选设置的字典，最常见的是`context_processors`。
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            # context_processors: 是一个列表，其中包含Django应用于每个请求的上下文处理器。
            # 上下文处理器是在渲染模板之前处理数据的函数。
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
            ],
        },
    }
]

# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = (str(APPS_DIR / "fixtures"),)

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
# 这个设置决定了会话cookie是否应该使用HttpOnly标志。HttpOnly标志可以增加cookie的安全性，
# 因为它防止通过客户端脚本（例如JavaScript）访问cookie。这样可以减少跨站脚本攻击（XSS）的风险。
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
# 这个设置决定了CSRF（跨站请求伪造）保护使用的cookie是否应该使用HttpOnly标志。
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
# 这个设置控制Django应用在X-Frame-Options HTTP头中发送的值。
# X-Frame-Options头可以防止你的网站被其他网站通过<frame>, <iframe>或<object>嵌套。这有助于防止点击劫持攻击。
X_FRAME_OPTIONS = "DENY"

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = "admin/"
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [("""Dongbox""", "dongbox@example.com")]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}
# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#CACHES
# 缓存是一种非常有用的方式，可以用来提高网站的性能。
# 通过将经常访问但不常改变的数据或页面保存在一个快速访问的位置，可以显著减少数据库查询和处理时间。
CACHES = {
    "default": {
        # Memcached是一个高性能的，分布式的内存对象缓存系统，用于动态Web应用以减轻数据库负载。
        # 它通过在内存中缓存数据和对象来减少读取数据库的次数，从而提供快速的访问速度和提高应用的性能。
        # "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        # Django默认的本地内存缓存
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        #
    }
}


# django-rest-framework
# -------------------------------------------------------------------------------
# django-rest-framework - https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    # 设置默认的分页类。
    # 这是一个简单的分页方案，客户端可以通过指定一个页码来请求一组项目。
    "DEFAULT_PAGINATION_CLASS": ("rest_framework.pagination.PageNumberPagination"),
    # 设置默认的解析器类，这些类负责解析客户端发送的请求体。
    # 在此配置中，有三个解析器：JSONParser 解析 JSON 请求体，FormParser 解析表单请求体，MultiPartParser 解析多部分请求体（通常用于文件上传）。
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ),
    # 设置默认的渲染器类，这些类负责将响应数据渲染为内容类型。
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    # 只有经过身份验证的用户才能访问 API, 各别视图可以声明匿名权限解开此限制
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    # 设置默认的认证类。在此配置中，使用的是 Simple JWT 的 JWTAuthentication 类来处理 JSON Web Tokens。
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
    # 设置默认的页面大小。
    "PAGE_SIZE": 6,
    # 设置用于查询参数的名称，以允许客户端指定排序顺序。
    "ORDERING_PARAM": "sort",
    # 设置测试请求的默认格式。
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    # 设置用于自动生成 API schema 的类。
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    # 设置默认的节流（throttle）类。这些类用于控制 API 的请求速率。
    "DEFAULT_THROTTLE_CLASSES": [
        # 匿名用户
        "rest_framework.throttling.AnonRateThrottle",
        # 认证用户
        "rest_framework.throttling.UserRateThrottle",
    ],
    # 设置默认的节流率。
    "DEFAULT_THROTTLE_RATES": {"anon": "100/minute", "user": "100/minute"},
}

# 用于指示 Django REST framework 在身份验证过程中使用 JSON Web Tokens (JWT) 而不是使用传统的令牌。
REST_USE_JWT = True

SIMPLE_JWT = {
    # 定义了访问令牌(access token)的生命周期
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(hours=1),
    # 刷新令牌通常用于在不要求用户重新登录的情况下，获取一个新的访问令牌。
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=1),
    # 这个布尔值设置决定是否在使用刷新令牌获取新的访问令牌时，旋转(或替换)刷新令牌。
    "ROTATE_REFRESH_TOKENS": False,
    # 这个布尔值设置决定是否在使用刷新令牌获取新的访问令牌时，旋转(或替换)刷新令牌。
    "UPDATE_LAST_LOGIN": True,
    # 这定义了用于签署和验证JWT的加密算法。
    "ALGORITHM": "HS256",
    # 这定义了认证头部的类型。
    "AUTH_HEADER_TYPES": ("Bearer",),
    # 这定义了用于携带JWT的HTTP头部的名称。
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    # 定义了在用户模型中用于表示用户ID的字段名称。
    "USER_ID_FIELD": "id",
    # 定义了在JWT的有效负载(payload)中，表示用户ID的声明名称。
    "USER_ID_CLAIM": "user_id",
    # 定义了在JWT的有效负载中，表示令牌类型的声明名称。
    "TOKEN_TYPE_CLAIM": "token_type",
    # 定义了JWT的JWT ID (JTI)的声明名称。JTI通常是一个唯一标识符，用于标识单个JWT。
    "JTI_CLAIM": "jti",
}

# django-cors-headers - https://github.com/adamchainz/django-cors-headers#setup
# 配置项 CORS_URLS_REGEX 是一个正则表达式，它定义了哪些URL路径应该被 django-cors-headers 中间件处理。
CORS_URLS_REGEX = r"^/api/.*$"

# Your stuff...
# ------------------------------------------------------------------------------
