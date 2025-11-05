# Deploy Frontend to Netlify + Backend to Heroku

## Tasks
- [x] Deploy backend to Render using existing render.yaml
- [x] Create render.yaml for frontend static site deployment
- [x] Update frontend JavaScript files to use the deployed backend URL
- [x] Fix render.yaml configuration issues (region, publishDir, staticSiteGenerator, plan, rootDir, buildCommand)
- [x] Deploy frontend to Render (Blueprint created, publishDir added)
- [x] Switch to Netlify + Railway (easier deployment)
- [x] Create netlify.toml for frontend deployment
- [x] Create railway.json for backend deployment
- [x] Update API_BASE_URL to Railway backend URL
- [x] Update CORS settings for Netlify domains
- [x] Add ignore rule to prevent Netlify rebuilds on backend changes
- [x] Remove old Vercel and Render config files to avoid confusion
- [x] Deploy frontend to Netlify (connect to GitHub repo)
- [x] Update all HTML files with Railway backend URL
- [x] Fix settings.py indentation error
- [x] Create admin user
- [x] Migrate database
- [x] Collect static files
- [x] Commit changes to git
- [x] Push code to GitHub
- [x] Deploy backend to Railway (add DJANGO_SUPERUSER_PASSWORD env var)
- [x] Fix Railway deployment Python path issue with nixpacks.toml
- [x] Fix Railway start command to bind to 0.0.0.0:$PORT
- [x] Add healthcheck configuration to railway.json
- [x] Add collectstatic to Railway start command
- [x] Move collectstatic to start command in nixpacks.toml
- [x] Fix Railway start command path
- [x] Fix pip command in nixpacks.toml to use python -m pip
- [x] Fix Railway backend URL in settings.py and update CSRF_TRUSTED_ORIGINS
- [x] Deploy frontend to Netlify
- [x] Remove Procfile (not needed for Railway)
- [x] Switch to Heroku backend deployment
- [x] Remove Railway config files (railway.json, nixpacks.toml)
- [x] Create runtime.txt for Heroku Python version
- [x] Update settings.py for Heroku domains
- [x] Update TODO.md for Heroku deployment
- [ ] Set Heroku environment variables in dashboard:
  - SECRET_KEY: Generate a secure key (e.g., python -c "import secrets; print(secrets.token_urlsafe(50))")
  - DEBUG: False
  - DATABASE_URL: Provided by Heroku (PostgreSQL)
  - DJANGO_SUPERUSER_PASSWORD: Set for admin user creation
  - EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD (if email needed)
  - FRONTEND_URL: https://prairesafricatravel.netlify.app
- [ ] Deploy backend to Heroku
- [ ] Update frontend API_BASE_URL to Heroku backend URL
- [ ] Test the full deployment
- [ ] Access admin panel at: https://your-heroku-app.herokuapp.com/admin/
- [ ] Frontend available at: https://prairies-africa.netlify.app/

## Heroku Backend Deployment Checklist
- [x] Procfile configured for Heroku deployment
- [x] runtime.txt created for Python version
- [x] requirements.txt includes all necessary packages (Django, DRF, gunicorn, dj-database-url, psycopg2-binary, whitenoise, etc.)
- [x] settings.py ALLOWED_HOSTS includes .herokuapp.com
- [x] settings.py CSRF_TRUSTED_ORIGINS includes Heroku URL placeholder
- [x] Railway config files removed

## Notes
- Switched to Heroku for backend deployment
- Heroku provides reliable Django deployment with database
- Netlify handles static frontend with automatic deployments
- All configurations updated and ready for Heroku deployment
- Updated settings.py for Heroku domains
- Created runtime.txt for Python version specification
- Railway config files removed
