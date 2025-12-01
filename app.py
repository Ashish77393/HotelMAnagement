import os

# Ensure settings module is set for Vercel's runtime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectAsh.settings')

# Import Django ASGI application
from django.core.asgi import get_asgi_application

# Vercel's python builder expects an 'app' ASGI/WSGI callable like FastAPI/Starlette
app = get_asgi_application()
