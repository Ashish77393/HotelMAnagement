# HotelMAnagement

## Deployment (Render)

This project is ready to deploy to Render. High-level steps:

1. Create a new Web Service on Render (Python environment).
2. Connect your repository and set the build command to:

   pip install -r requirements.txt

3. Set environment variables in Render:

   - DJANGO_SETTINGS_MODULE = ProjectAsh.settings
   - SECRET_KEY = <your-production-secret>
   - DEBUG = False
   - ALLOWED_HOSTS = hotelmanagement-4-o2yw.onrender.com,localhost,127.0.0.1

4. Provision a managed PostgreSQL database on Render (optional but recommended) and attach it so Render sets DATABASE_URL; or manually set DATABASE_URL to your DB's connection string.

5. Start command (Render uses `render.yaml` or service settings):

   gunicorn ProjectAsh.wsgi:application --bind 0.0.0.0:$PORT

6. After deployment completes, run the migration and static collection (Render console):

   python manage.py migrate
   python manage.py collectstatic --noinput

Notes:

- We use `dj-database-url` to read DATABASE_URL when present.
- `whitenoise` serves static files using the compressed manifest storage.
- `Procfile` is configured to use `gunicorn ProjectAsh.wsgi:application`.

If you prefer to deploy elsewhere (Heroku, etc.) the steps are similar: ensure environment variables are set and that `requirements.txt` includes `gunicorn`, `whitenoise`, `dj-database-url` and `psycopg2-binary`.
