from .base import *

DEBUG = env.bool('DJANGO_DEBUG', default=True)
SECRET_KEY = env('DJANGO_SECRET_KEY', default='$*y9+hfwqy7&+8fm)l$6^^3hsv#k_rrhldxwrgr&8utpb!2!m%')
