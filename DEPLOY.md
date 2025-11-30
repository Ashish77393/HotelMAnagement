# Deploying this project to Render (GitHub + Render)

This guide walks through connecting your GitHub repository to Render and using the included GitHub Action to trigger deployments.

Important: I cannot connect to your GitHub or Render account for you. Follow these steps in your accounts to finish the setup.

## 1) Quick checklist (what needs to be in repo)

- `requirements.txt` includes: gunicorn, whitenoise, dj-database-url, psycopg2-binary
- `Procfile` points to `gunicorn ProjectAsh.wsgi:application --bind 0.0.0.0:$PORT`
- `render.yaml` exists with build and start commands
- `ProjectAsh/settings.py` reads env vars and uses WhiteNoise
- `.github/workflows/render-deploy.yml` exists (already added)

## 2) Connect GitHub Repo to Render (via Render dashboard)

1. Sign in to https://dashboard.render.com.
2. Click "New" → "Web Service".
3. Connect your Git provider (GitHub) and pick this repository.
4. Select the branch (main) and confirm the build command and start command. If you use `render.yaml`, Render uses that.
   - Build command (if not using render.yaml): `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Start command: `gunicorn ProjectAsh.wsgi:application --bind 0.0.0.0:$PORT`
5. Provision a managed PostgreSQL database if you want production DB — attach it to the service so Render provides `DATABASE_URL`.

## 3) Configure environment variables in Render

Under your service → Environment → Add environment variable(s):

- DJANGO_SETTINGS_MODULE = ProjectAsh.settings
- SECRET_KEY = <your production secret>
- DEBUG = False
- ALLOWED_HOSTS = hotelmanagement-4-o2yw.onrender.com (or add your hostnames comma separated)

If using a managed DB, leave `DATABASE_URL` to be populated by Render when you attach the database.

## 4) Add repository secrets in GitHub (for automated deploys with the workflow)

1. Get `RENDER_API_KEY`: In Render dashboard → Account → API Keys → Create an API key for Deploys.
2. Get `RENDER_SERVICE_ID`: go to your service's dashboard on Render and note the `Service ID` from the URL or service settings.
3. In GitHub → repo → Settings → Secrets and variables → Actions → New repository secret:
   - `RENDER_API_KEY` = <the API key>
   - `RENDER_SERVICE_ID` = <your service id>

The included workflow `.github/workflows/render-deploy.yml` will POST to the Render Deploy API and kick off a new deploy each time you push to `main`.

## 5) Run migrations and collect static after deploy

Render builds the app during deploy using `render.yaml` or the build commands you provide. After the first deploy you should:

1. Open your Render service dashboard → Shell (or Console) and run:

   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```

2. Alternatively, you can run these commands via the Render web terminal or any other CI if you prefer.

## 6) Troubleshooting tips

- If static files not loading: confirm `STATICFILES_STORAGE` is set and `collectstatic` completed.
- If you get db connection errors: confirm `DATABASE_URL` is set correctly and you ran `migrate`.
- Logs on Render (service → logs) are your first stop for errors.

If you'd like, I can create a small helper workflow step to run `python manage.py migrate` on Render automatically after a successful deploy — but it requires careful handling of credentials and when you want it to run.
