# 🚀 Praires Africa Booking System - Complete Deployment Guide

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Local Testing](#local-testing)
3. [Database Migrations](#database-migrations)
4. [Email Setup](#email-setup)
5. [Deployment Options](#deployment-options)
6. [Post-Deployment Steps](#post-deployment-steps)

---

## Prerequisites

Before deploying, ensure you have:
- Python 3.9 or higher
- Git installed
- A Gmail account (for email notifications)
- A domain name (optional but recommended)

---

## Local Testing

### 1. Install Dependencies

Open a terminal in the `backend` folder and run:

```bash
cd backend
.venv\Scripts\activate  # On Windows
# OR
source .venv/bin/activate  # On Mac/Linux

pip install -r requirements.txt
```

### 2. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Admin User

```bash
python manage.py createsuperuser
```

Enter your desired username, email, and password.

### 4. Start Development Server

```bash
python manage.py runserver
```

Or use the batch file:
```bash
START_SERVER_FOREVER.bat
```

Visit:
- Frontend: Open `index.html` in your browser
- Admin Panel: http://127.0.0.1:8000/admin/
- API: http://127.0.0.1:8000/api/

---

## Database Migrations

After adding the new features (additional activities, etc.), run:

```bash
python manage.py makemigrations bookings
python manage.py migrate bookings
```

This will add the new fields to your database.

---

## Email Setup

### Gmail Configuration

1. **Enable 2-Step Verification** on your Gmail account
   - Go to: https://myaccount.google.com/security
   - Enable "2-Step Verification"

2. **Generate App Password**
   - Visit: https://myaccount.google.com/apppasswords
   - Select "Mail" and "Windows Computer"
   - Copy the 16-character password

3. **Update .env File**

Create or update `backend/.env`:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=seantakudzwa050505@gmail.com
EMAIL_HOST_PASSWORD=your-16-char-app-password-here
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=seantakudzwa050505@gmail.com
```

4. **Test Email**

```bash
python manage.py shell
```

```python
from django.core.mail import send_mail
send_mail(
    'Test Email',
    'This is a test email from Praires Africa.',
    'seantakudzwa050505@gmail.com',
    ['seantakudzwa050505@gmail.com'],
    fail_silently=False,
)
```

---

## Deployment Options

### Option 1: PythonAnywhere (FREE - Recommended for Beginners)

**Perfect for: Small to medium traffic, easy setup**

#### Steps:

1. **Sign Up**
   - Go to: https://www.pythonanywhere.com
   - Create a free "Beginner" account

2. **Upload Your Code**
   - Click "Files" tab
   - Upload your entire `backend` folder
   - Or use Git: `git clone https://github.com/your-repo.git`

3. **Create Virtual Environment**
   
   Open a Bash console:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 prairesenv
   pip install -r backend/requirements.txt
   ```

4. **Configure Web App**
   - Click "Web" tab
   - "Add a new web app"
   - Choose "Manual configuration"
   - Python 3.10
   
5. **Set Working Directory**
   - Source code: `/home/yourusername/backend`
   - WSGI file: Edit and set:
   
   ```python
   import sys
   import os
   
   path = '/home/yourusername/backend'
   if path not in sys.path:
       sys.path.append(path)
   
   os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'
   
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

6. **Set Environment Variables**
   - In "Web" tab, find "Environment variables"
   - Add all variables from your `.env` file

7. **Collect Static Files**
   
   In Bash console:
   ```bash
   cd backend
   python manage.py collectstatic
   ```

8. **Run Migrations**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

9. **Reload Web App**
   - Click green "Reload" button

10. **Upload Frontend Files**
    - Upload HTML files to `/home/yourusername/`
    - Update API_BASE_URL in JavaScript files to your PythonAnywhere URL

---

### Option 2: Heroku (FREE Tier Available)

**Perfect for: Professional deployment, automatic scaling**

#### Steps:

1. **Install Heroku CLI**
   - Download from: https://devcenter.heroku.com/articles/heroku-cli

2. **Login**
   ```bash
   heroku login
   ```

3. **Create App**
   ```bash
   cd backend
   heroku create praires-africa
   ```

4. **Add Buildpack**
   ```bash
   heroku buildpacks:set heroku/python
   ```

5. **Set Environment Variables**
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   heroku config:set EMAIL_HOST_USER=seantakudzwa050505@gmail.com
   heroku config:set EMAIL_HOST_PASSWORD=your-app-password
   # Add all other env variables
   ```

6. **Create Procfile** (in backend folder):
   ```
   web: gunicorn backend.wsgi --log-file -
   release: python manage.py migrate
   ```

7. **Update settings.py**
   ```python
   ALLOWED_HOSTS = ['praires-africa.herokuapp.com', 'localhost']
   ```

8. **Deploy**
   ```bash
   git init
   git add .
   git commit -m "Initial deployment"
   git push heroku main
   ```

9. **Run Migrations**
   ```bash
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

10. **Open App**
    ```bash
    heroku open
    ```

---

### Option 3: Render (FREE)

**Perfect for: Modern deployment, automatic SSL**

1. **Sign Up**
   - Go to: https://render.com
   - Create account

2. **Create New Web Service**
   - Connect your GitHub repo
   - Or upload code manually

3. **Configure**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn backend.wsgi:application`

4. **Add Environment Variables**
   - Add all variables from `.env` file

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment

---

### Option 4: Railway (FREE $5/month credit)

**Perfect for: Fast deployment, PostgreSQL included**

1. **Sign Up**
   - Go to: https://railway.app

2. **New Project**
   - "Deploy from GitHub repo"
   - Select your repository

3. **Add Django Service**
   - Railway auto-detects Django
   - Add environment variables

4. **Deploy**
   - Automatic deployment on git push

---

## Frontend Hosting

### Option A: Netlify (Recommended for Static Files)

1. **Sign Up**: https://www.netlify.com
2. **Drag & Drop** your HTML files
3. **Update API URLs** in JavaScript to your backend URL

### Option B: GitHub Pages

1. Push HTML files to GitHub repo
2. Enable GitHub Pages in repository settings
3. Access via: `https://username.github.io/repo-name/`

### Option C: Vercel

1. Sign up: https://vercel.com
2. Import GitHub repository
3. Deploy automatically

---

## Post-Deployment Steps

### 1. Update API URLs

In all HTML files, update the API_BASE_URL:

```javascript
// booking.html, payment-status.html, etc.
const API_BASE_URL = 'https://your-backend-url.com';
```

### 2. Update CORS Settings

In `backend/settings.py`:

```python
CORS_ALLOWED_ORIGINS = [
    'https://your-frontend-domain.com',
    'https://www.your-frontend-domain.com',
]

CSRF_TRUSTED_ORIGINS = [
    'https://your-frontend-domain.com',
]
```

### 3. Set DEBUG=False

```python
DEBUG = False
```

### 4. Configure Custom Domain (Optional)

#### For Backend (PythonAnywhere):
- Upgrade to paid plan for custom domain
- Add DNS CNAME record pointing to `username.pythonanywhere.com`

#### For Frontend (Netlify):
- Add custom domain in Netlify settings
- Update DNS records as instructed

### 5. Set Up SSL/HTTPS

- **PythonAnywhere**: Included in paid plans
- **Heroku**: Automatic SSL
- **Render**: Automatic SSL
- **Netlify**: Automatic SSL

### 6. Test Everything

- ✅ Create a test booking
- ✅ Verify emails are sent (admin + customer)
- ✅ Check payment status page
- ✅ Test admin panel functionality
- ✅ Verify additional activities work
- ✅ Check responsive design on mobile

---

## Troubleshooting

### Email Not Sending

**Problem**: Emails not being received

**Solutions**:
1. Check Gmail App Password is correct
2. Verify `EMAIL_HOST_USER` matches sender email
3. Check spam folder
4. Enable "Less secure app access" if using old Gmail setup
5. Check Django logs for errors

### Database Errors

**Problem**: Migration errors

**Solutions**:
```bash
python manage.py migrate --run-syncdb
python manage.py makemigrations
python manage.py migrate
```

### Static Files Not Loading

**Problem**: CSS/JS not loading in production

**Solutions**:
```bash
python manage.py collectstatic --noinput
```

Update settings:
```python
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

### CORS Errors

**Problem**: Frontend can't connect to backend

**Solutions**:
1. Add frontend URL to `CORS_ALLOWED_ORIGINS`
2. Add to `CSRF_TRUSTED_ORIGINS`
3. Check browser console for exact error

---

## Maintenance

### Regular Tasks

**Daily**:
- Check admin panel for new bookings
- Verify payment confirmations

**Weekly**:
- Review pending bookings
- Check email delivery logs
- Backup database

**Monthly**:
- Update Django and dependencies
- Review security settings
- Check server logs

### Backup Commands

```bash
# Backup database
python manage.py dumpdata > backup.json

# Restore database
python manage.py loaddata backup.json
```

---

## Security Checklist

- [ ] DEBUG = False in production
- [ ] Strong SECRET_KEY
- [ ] HTTPS enabled
- [ ] Email credentials in environment variables (not hardcoded)
- [ ] ALLOWED_HOSTS configured
- [ ] CORS properly configured
- [ ] Regular security updates
- [ ] Strong admin passwords

---

## Support & Resources

### Documentation
- Django: https://docs.djangoproject.com/
- Django REST Framework: https://www.django-rest-framework.org/
- Jazzmin: https://django-jazzmin.readthedocs.io/

### Video Tutorials
- PythonAnywhere Deployment: https://www.youtube.com/results?search_query=django+pythonanywhere
- Heroku Deployment: https://www.youtube.com/results?search_query=django+heroku

### Community Support
- Django Forum: https://forum.djangoproject.com/
- Stack Overflow: Tag with `django`

---

## Quick Reference

### Development Server
```bash
python manage.py runserver
```

### Create Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Admin
```bash
python manage.py createsuperuser
```

### Collect Static Files
```bash
python manage.py collectstatic
```

### Run Tests
```bash
python manage.py test
```

---

## Contact

For questions or issues with deployment, contact:
- Email: seantakudzwa050505@gmail.com
- WhatsApp: +263 77 693 0966

---

**Good luck with your deployment! 🎉**
