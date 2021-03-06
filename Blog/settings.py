"""
Django settings for Blog project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
DOMAIN = "http://127.0.0.1:8000/"
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ty7q^%y5bn1jk##(vvjm767td067z5cn#%0(%7*9xy%qxg*s(*'

# SECURITY W
# ARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1","localhost",".jxtalx970317.site"]
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'
CORS_ORIGIN_ALLOW_ALL = True
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
 'blogs',

    "comment",
    "collection",
    "ckeditor",
    "ckeditor_uploader",
    "compliment",
    "oauth",
    "haystack",
    "froala_editor",
    "rest_framework",
    "notifications",
    "notice",
    "appeal"
    
]
MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        # 'django.middleware.cache.UpdateCacheMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        # 'django.middleware.cache.FetchFromCacheMiddleware',
    "Blog.Midwares.AuthMidware",


]
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}
HAYSTACK_DEFAULT_OPERATOR = "OR"
HAYSTACK_LIMIT_TO_REGISTERED_MODELS = False
ELASTICSEARCH_AUTO_INDEX = True
# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
#         'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
#     },
# }
# HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HOST = "127.0.0.1"
ROOT_URLCONF = 'Blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'Blog.wsgi.application'
LOGIN_URL = "/account/login/"
BASE_DOMAIN = "http://127.0.0.1:8000"
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "blog",
        "HOST":"localhost",
        "PORT":"3306",
        "USER":"root",
        "PASSWORD":"",
        "character":"utf-8"
    }
}
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "TIMEOUT":300,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
            # "PASSWORD": "密码",
        }
    }
}
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': 'd:/program/1',
#     }
# }
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'log_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'djangoblog.log',
            'maxBytes': 16777216,  # 16 MB
            'formatter': 'simple'
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'formatter':'verbose',
        }
    },
    'loggers': {
        'django': {
            'handlers': ["log_file",'console'],
            'level':'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}
# 邮件配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.163.com'  # SMTP地址
EMAIL_PORT = 465  # SMTP端口
EMAIL_HOST_USER = '18747383641@163.com'  # 发送邮件的邮箱
EMAIL_HOST_PASSWORD = '19970317lx'  # 我的邮箱密码
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_SUBJECT_PREFIX = u'[prefix]'  # 为邮件Subject-line前缀,默认是'[django]' # 与SMTP服务器通信时，是否启动TLS链接(安全链接)。默认是false
# 管理员站点
# SERVER_EMAIL = '18747383641@163.com'  # The email address that error messages come from, such as those sent to ADMINS and MANAGERS.
ADMINS = (('receiver', '18747383641@163.com'),)  # 接收邮件的邮箱（或邮件组）
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
"""
富文本编辑器
"""
# ckeditor config
CKEDITOR_UPLOAD_PATH = 'Article_image/'
CKEDITOR_JQUERY_URL ='jqeury/jquery-3.3.1.js'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    # django-ckeditor默认使用default配置
    'comment': {
        # 编辑器宽度自适应
        'width':'600',
        'height':'100',
        "config.skin":"kama",
        # tab键转换空格数
        'tabSpaces': 4,
        # 工具栏风格
        'toolbar': 'Custom',
        # 工具栏按钮
        'toolbar_Custom': [
            # 表情 代码块
            ['Smiley'],
            # 字体颜色
            ['TextColor', 'BGColor'],
        ],
        'smiley_images': ['1.png', '2.png', '3.png', '4.png', '5.gif', '6.gif', '7.gif', '8.gif', '9.gif', '10.gif',
                          '11.gif', '12.gif', '13.gif', '14.gif', '15.gif', '16.gif', '17.gif', '18.gif', '19.gif',
                          '20.gif',
                          '21.gif', '22.gif', '23.gif', '24.gif', '25.gif', '26.gif', '27.gif', '28.gif', '29.gif',
                          '30.gif',
                          '31.gif', '32.gif', '33.gif', '34.gif', '35.gif', '36.gif', '37.gif', '38.gif', '39.gif',
                          '40.gif',
                          '41.gif', '42.gif', '43.gif', '54.gif', '45.gif', '46.gif', '47.gif', '48.gif', '49.gif',
                          '50.gif',
                          ],
    },

}
CKEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_BROWSE_SHOW_DIRS = True
#FROALA
FROALA_INCLUDE_JQUERY = False
FROALA_EDITOR_OPTIONS = {

}
SOFT_DELETE = True
# media_confige
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
AUTHENTICATION_BACKENDS = (
    'account.backend.EmailCheckBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

AUTH_USER_MODEL = "account.BlogUser"

USE_I18N = True

USE_L10N = True

USE_TZ = True

PAGINATE_BY = 15
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collectstatic')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../blog/static'),
)