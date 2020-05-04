import os
from datetime import timedelta

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=1)
DATABASE_URL = os.getenv("DATABASE_URL")
