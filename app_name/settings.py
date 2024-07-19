import os
# default flask app config settings

# sqlalchemy config settings
SQLALCHEMY_TRACK_MODIFICATIONS=False
SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL")

# jwt extended config settings
# needed for encoding by flask_jwt_extended
JWT_SECRET_KEY=os.environ.get("JWT_SECRET_KEY")
# needed for jwt extended token cookies
JWT_TOKEN_LOCATION="headers"
# JWT_ACCESS_COOKIE_PATH="/api/"
# JWT_COOKIE_SECURE=False # should be True in production to use https
# JWT_COOKIE_SAMESITE="Lax"
# fix this value with: datetime object, timedelta object or 
# int for total seconds
JWT_ACCESS_TOKEN_EXPIRES=7*24*3600*1000
# needed for CSRF protection
# JWT_COOKIE_CSRF_PROTECT=True
# JWT_CSRF_METHODS=["GET","POST","PUT","PATCH","DELETE"]
# JWT_COOKIE_DOMAIN=None

# apispec

APISPEC_SWAGGER_URL="/swagger/"
APISPEC_SWAGGER_UI_URL="/swagger-ui/"

# CORS
CORS_EXPOSE_HEADERS=["Pagination-Page", "Pagination-Count", "Pagination-Limit"]
CORS_ORIGIN=os.environ.get("CORS_ORIGINS")
