
import os
from sc4py.env import env
os.environ.setdefault("URL_PATH_PREFIX", env("", "ege/dashboard/"))
os.environ.setdefault("MY_APPS", "ege_dashboard")
os.environ.setdefault("POSTGRES_DB", env("POSTGRES_DB_DASHBOARD", 'ege_dashboard'))

os.environ.setdefault("SUAP_EAD_UTILS_AUTH_JWT_BACKEND", env("SUAP_EAD_UTILS_AUTH_JWT_BACKEND", 'suap_ead.auth.CreateNewUserJwtBackend'))

from suap_ead.template_settings import *
