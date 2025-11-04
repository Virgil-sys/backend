# 🦁 Prairies Africa Complete Manual
## The Super Simple Guide (Explained to a 5-Year-Old!)

---

# 📖 Table of Contents

1. [What You Built](#what-you-built)
2. [How to Start Your Server](#how-to-start-server)
3. [How to Stop Your Server](#how-to-stop-server)
4. [How Long Will It Run](#how-long-it-runs)
5. [Being an Admin](#being-admin)
6. [Daily Admin Tasks](#daily-tasks)
7. [How to Host Online FREE](#host-free)
8. [How to Host Online PAID](#host-paid)
9. [Troubleshooting](#troubleshooting)
10. [Quick Reference Card](#quick-reference)

---

<a name="what-you-built"></a>
# 🎨 1. What You Built (Like Legos!)

Imagine you built a **lemonade stand** with magic robots! 🍋🤖

## Your Lemonade Stand Has:

### 🏠 The Stand (Your Website)
- **index.html** = Front of stand (shows activities)
- **packages.html** = Menu board (shows packages)
- **booking.html** = Order form (customers write orders)
- **upload-proof.html** = Receipt box (customers drop receipts)

### 🤖 The Robot Helper (Django Backend)
- **Lives in:** `backend` folder
- **Job:** Remember orders, send emails, keep records
- **Brain:** Database (db.sqlite3 file)
- **Memory:** Stores customer info, bookings, payments

### 👨‍💼 Your Office (Admin Panel)
- **Address:** http://127.0.0.1:8000/admin
- **Username:** admin
- **Password:** admin123
- **Job:** Check orders, approve payments

---

<a name="how-to-start-server"></a>
# 🚀 2. How to Start Your Server

## 🎈 Simple Explanation

Starting your server is like **turning on your lemonade stand's lights**. When lights are ON, customers can order! When lights are OFF, nobody can order.

## ⚡ Quick Start (Copy-Paste This!)

**Step 1: Open PowerShell**
- Press Windows Key
- Type: `PowerShell`
- Click "Windows PowerShell"

**Step 2: Copy and paste this:**
```powershell
cd "C:\Users\sean\Desktop\my website\backend"
.venv\Scripts\python.exe manage.py runserver
```

**Step 3: Wait for this message:**
```
Starting development server at http://127.0.0.1:8000/
```

**✅ DONE! Your server is running!**

## 📸 What You'll See

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 03, 2025 - 16:28:39
Django version 4.2.7, using settings 'backend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

**When you see this = Server is ON! 🟢**

---

<a name="how-to-stop-server"></a>
# 🛑 3. How to Stop Your Server

## 🎈 Simple Explanation

Stopping your server is like **turning off your lemonade stand lights**. Do this when you're done working.

## ⚡ How to Stop

**Option 1: Press Ctrl + C**
- Go to PowerShell window
- Press `Ctrl` + `C` keys together
- Server stops!

**Option 2: Close PowerShell Window**
- Click the X button
- Server stops!

**What You'll See:**
```
Quit the server with CTRL-BREAK.
^C
PS C:\Users\sean\Desktop\my website\backend>
```

**When you see this = Server is OFF! 🔴**

---

<a name="how-long-it-runs"></a>
# ⏰ 4. How Long Will Your Server Run?

## 🎈 Simple Answer

**Your server runs ONLY while PowerShell is open!**

Think of it like a **flashlight** 🔦:
- PowerShell open = Flashlight ON → Server works
- PowerShell closed = Flashlight OFF → Server stops

## 📊 Scenarios

| What You Do | Server Status | Can Customers Book? |
|-------------|---------------|---------------------|
| PowerShell open, command running | 🟢 ON | ✅ YES |
| PowerShell closed | 🔴 OFF | ❌ NO |
| Computer turned off | 🔴 OFF | ❌ NO |
| Computer sleeping | 🔴 OFF | ❌ NO |
| Internet disconnected | 🟢 ON (local only) | ⚠️ Only on your computer |

## 💡 Important Rules

### ✅ DO:
- Keep PowerShell window open while working
- Minimize PowerShell (don't close it!)
- Leave computer on if testing

### ❌ DON'T:
- Close PowerShell window (server stops!)
- Turn off computer (server stops!)
- Put computer to sleep (server stops!)

## 🌐 For 24/7 Online Website

**Problem:** Your computer can't run 24/7!

**Solution:** Host online (see Section 7 & 8)

When hosted online:
- ✅ Runs 24/7 even when your computer is off
- ✅ Customers can book anytime
- ✅ Server never sleeps!

---

<a name="being-admin"></a>
# 👨‍💼 5. Being an Admin (Your Job!)

## 🎈 What is an Admin?

You're like the **manager of a restaurant** 🍽️:
- Customers order food (book tours)
- You check if they paid (verify payment proofs)
- You confirm their reservation (approve bookings)

## 🔑 Your Admin Powers

**What You Can Do:**
1. ✅ See all bookings
2. ✅ See all customers
3. ✅ See all payment proofs
4. ✅ Approve or reject payments
5. ✅ Change booking status
6. ✅ Manage bank accounts
7. ✅ See everything in the database!

**What You CANNOT Do:**
- ❌ Delete the database by accident (protected!)
- ❌ Break the website (you can always undo)
- ❌ Lose customer data (auto-saved)

## 🚪 How to Login as Admin

**Step 1: Make sure server is running**
```powershell
.venv\Scripts\python.exe manage.py runserver
```

**Step 2: Open browser and go to:**
```
http://127.0.0.1:8000/admin
```

**Step 3: Login**
- Username: `admin`
- Password: `admin123`

**Step 4: You're in! 🎉**

---

<a name="daily-tasks"></a>
# 📋 6. Daily Admin Tasks (Your To-Do List!)

## ☀️ Morning Routine (5 minutes)

### Task 1: Start Server
```powershell
cd "C:\Users\sean\Desktop\my website\backend"
.venv\Scripts\python.exe manage.py runserver
```

### Task 2: Check New Bookings
1. Go to: http://127.0.0.1:8000/admin
2. Click **"Bookings"**
3. Look for new entries (today's date)
4. Note down booking reference numbers

### Task 3: Check Email
- Open: seanzimucha@outlook.com
- Look for: "New Booking" emails
- Read customer details

## 💼 Main Job: Verify Payments (10 minutes)

### When Customer Uploads Payment Proof

**You get email:** "Payment proof uploaded for booking #123"

**What to do:**

**Step 1: Go to Admin Panel**
- http://127.0.0.1:8000/admin

**Step 2: Click "Bank transfers"**

**Step 3: Click on the pending transfer**

**Step 4: Check the proof**
- Click on the proof_of_payment link
- Image/PDF opens in browser

**Step 5: Verify Details**
```
✅ Amount matches? (e.g., $1,500)
✅ Reference number matches? (e.g., BK-20251103-1)
✅ Bank account correct? (Your FNB or Standard Bank)
✅ Date reasonable? (Within last few days)
```

**Step 6a: If Everything is Correct**
- Change **Status** dropdown to **"Verified"**
- Click **"Save"** button
- ✅ Customer gets email: "Payment confirmed!"
- ✅ Booking status changes to "Confirmed"

**Step 6b: If Something is Wrong**
- Change **Status** to **"Failed"**
- Add note in **"Notes"** field (e.g., "Wrong amount")
- Click **"Save"**
- Contact customer via email/phone

## 🌙 Evening Routine (2 minutes)

### Task 1: Check Completed Tours
- Go to **Bookings**
- Find today's tours
- Change status to **"Completed"**
- Save

### Task 2: Stop Server (if done for the day)
- Press `Ctrl + C` in PowerShell
- Or leave running if expecting bookings

---

<a name="host-free"></a>
# 🆓 7. How to Host Online FREE

## 🎈 Simple Explanation

Right now your website is like a **toy phone** - only works in your house.

Hosting online makes it a **real phone** - works everywhere in the world! 🌍

## 🎯 Free Hosting Options

### Option 1: PythonAnywhere (Easiest!)

**What:** Free Python hosting, perfect for Django

**Limits:**
- ✅ FREE forever
- ✅ Good for 100-500 visitors/day
- ⚠️ Slow after 100,000 requests/month
- ⚠️ URL: yourusername.pythonanywhere.com

**How to Setup (20 minutes):**

**Step 1: Sign Up**
1. Go to: https://www.pythonanywhere.com/
2. Click "Start running Python online for free"
3. Create account (use seanzimucha@outlook.com)
4. Choose username: `prairiesafrica`

**Step 2: Upload Your Code**
1. Click **"Files"** tab
2. Upload your `backend` folder
3. Or use Git to clone

**Step 3: Setup Virtual Environment**
In PythonAnywhere console:
```bash
mkvirtualenv --python=/usr/bin/python3.11 prairiesenv
pip install -r backend/requirements.txt
```

**Step 4: Configure Web App**
1. Click **"Web"** tab
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Choose "Python 3.11"

**Step 5: Set WSGI file**
Edit WSGI configuration:
```python
import os
import sys

path = '/home/prairiesafrica/backend'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Step 6: Set Static Files**
- Static URL: `/static/`
- Static directory: `/home/prairiesafrica/backend/staticfiles/`

**Step 7: Run Migrations**
In console:
```bash
cd backend
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```

**Step 8: Update Settings**
Edit `.env`:
```env
DEBUG=False
ALLOWED_HOSTS=prairiesafrica.pythonanywhere.com
```

**Step 9: Reload Web App**
- Click green "Reload" button

**✅ Your site is LIVE!**
- URL: https://prairiesafrica.pythonanywhere.com

---

### Option 2: Railway.app (Modern & Fast!)

**What:** Modern hosting platform, free tier

**Limits:**
- ✅ FREE for $5 credit/month
- ✅ Fast servers
- ✅ Custom domain support
- ⚠️ Credit card required (not charged)

**How to Setup (15 minutes):**

**Step 1: Sign Up**
1. Go to: https://railway.app/
2. Sign up with GitHub
3. Verify email

**Step 2: Create New Project**
1. Click "New Project"
2. Choose "Deploy from GitHub repo"
3. Connect your GitHub account
4. Or "Deploy from template" → Django

**Step 3: Add PostgreSQL**
1. Click "New"
2. Choose "Database"
3. Select "PostgreSQL"
4. Copy DATABASE_URL

**Step 4: Set Environment Variables**
Click "Variables" tab:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app.railway.app
DATABASE_URL=(auto-filled)
EMAIL_HOST_USER=seanzimucha@outlook.com
EMAIL_HOST_PASSWORD=your-password
```

**Step 5: Deploy!**
- Railway auto-deploys from GitHub
- Wait 2-5 minutes

**✅ Your site is LIVE!**
- URL: https://your-app.railway.app

---

### Option 3: Render.com (Recommended!)

**What:** Free web hosting with PostgreSQL

**Limits:**
- ✅ FREE forever (with limits)
- ✅ Auto-deploy from GitHub
- ✅ Free PostgreSQL database
- ⚠️ Sleeps after 15 min inactivity (wakes up on visit)

**How to Setup (15 minutes):**

**Step 1: Push to GitHub**
1. Go to: https://github.com
2. Create account
3. Create new repository: `prairies-backend`
4. Push your backend folder

**Step 2: Sign up for Render**
1. Go to: https://render.com
2. Sign up with GitHub
3. Allow access to repository

**Step 3: Create Web Service**
1. Click "New +"
2. Choose "Web Service"
3. Connect `prairies-backend` repo
4. Fill in:
   - Name: `prairies-backend`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
   - Start Command: `gunicorn backend.wsgi:application`

**Step 4: Add Environment Variables**
```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=prairies-backend.onrender.com
DATABASE_URL=(auto-added by Render)
```

**Step 5: Create PostgreSQL Database**
1. Click "New +"
2. Choose "PostgreSQL"
3. Name: `prairies-db`
4. Plan: Free
5. Copy internal database URL
6. Add to web service as `DATABASE_URL`

**Step 6: Deploy!**
- Click "Create Web Service"
- Wait 3-5 minutes

**✅ Your site is LIVE!**
- URL: https://prairies-backend.onrender.com

---

## 🎯 Free Hosting Comparison

| Feature | PythonAnywhere | Railway | Render |
|---------|----------------|---------|--------|
| **Price** | FREE forever | FREE $5/month | FREE forever |
| **Speed** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Ease** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Database** | MySQL/PostgreSQL | PostgreSQL | PostgreSQL |
| **Custom Domain** | Paid only | ✅ FREE | ✅ FREE |
| **Sleep Mode** | No | No | Yes (15 min) |
| **Best For** | Beginners | Small business | Side projects |

**My Recommendation for You:** Start with **Render.com** (free + easy)!

---

<a name="host-paid"></a>
# 💰 8. How to Host Online PAID (Professional!)

## 🎈 When to Upgrade?

Upgrade when:
- ✅ You get 100+ bookings/month
- ✅ You want a custom domain (prairiesafrica.com)
- ✅ You need 24/7 support
- ✅ You want faster servers
- ✅ Free tier is too slow

## 💎 Paid Hosting Options

### Option 1: DigitalOcean (Best Value!)

**Cost:** $6/month (droplet) + $15/month (managed database) = **$21/month**

**What You Get:**
- ✅ Full server control
- ✅ Managed PostgreSQL database
- ✅ 99.99% uptime
- ✅ Fast global servers
- ✅ Easy scaling

**How to Setup:**

1. **Sign up:** https://digitalocean.com
2. **Create Droplet:**
   - Choose Ubuntu 22.04
   - $6/month plan (1GB RAM)
   - Choose region closest to Zimbabwe (Amsterdam or Frankfurt)
3. **Create Managed Database:**
   - PostgreSQL 14
   - $15/month plan
4. **Install Django:**
   ```bash
   # SSH into droplet
   apt update
   apt install python3-pip python3-venv nginx
   git clone your-repo
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
5. **Configure Nginx**
6. **Setup SSL (free with Let's Encrypt)**
7. **Run with Gunicorn + Supervisor**

**Total Cost:** ~$21/month

---

### Option 2: Heroku (Easiest Paid!)

**Cost:** $7/month (Eco Dyno) + $5/month (Postgres) = **$12/month**

**What You Get:**
- ✅ Super easy deployment
- ✅ Auto-scaling
- ✅ Built-in PostgreSQL
- ✅ Free SSL
- ✅ Great documentation

**How to Setup:**

1. **Sign up:** https://heroku.com
2. **Install Heroku CLI**
3. **Deploy:**
   ```bash
   cd backend
   heroku create prairies-africa
   git push heroku main
   heroku addons:create heroku-postgresql:essential-0
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

**Total Cost:** ~$12/month

---

### Option 3: AWS Lightsail (Amazon!)

**Cost:** $5/month (instance) + $15/month (database) = **$20/month**

**What You Get:**
- ✅ Amazon reliability
- ✅ Global CDN
- ✅ Easy scaling
- ✅ 3 months free trial

**How to Setup:**

1. **Sign up:** https://lightsail.aws.amazon.com
2. **Create Instance:**
   - Choose "Django" blueprint
   - $5/month plan
3. **Create Database:**
   - PostgreSQL
   - $15/month plan
4. **Connect and deploy**

**Total Cost:** ~$20/month

---

## 🎯 Paid Hosting Comparison

| Provider | Monthly Cost | Setup Difficulty | Best For |
|----------|-------------|------------------|----------|
| **Heroku** | $12 | ⭐⭐⭐⭐⭐ Easy | Beginners |
| **DigitalOcean** | $21 | ⭐⭐⭐ Medium | Developers |
| **AWS Lightsail** | $20 | ⭐⭐⭐⭐ Medium-Easy | Growing Business |
| **PythonAnywhere Paid** | $5 | ⭐⭐⭐⭐⭐ Easy | Small Business |

**My Recommendation:** Start with **Heroku** ($12/month) - easiest and cheapest!

---

## 📊 Upgrade Path (Smart Way!)

```
Month 1-3: FREE (Render.com)
  ↓
  If getting 50+ bookings/month
  ↓
Month 4-6: PAID ($12/month - Heroku)
  ↓
  If getting 200+ bookings/month
  ↓
Month 7+: SCALE ($50/month - DigitalOcean + CDN)
```

**Start FREE, upgrade when needed!**

---

<a name="troubleshooting"></a>
# 🚨 9. Troubleshooting (When Things Break!)

## Problem 1: Server Won't Start

**Symptoms:**
```
Error: Port 8000 already in use
```

**Solution:**
```powershell
# Kill existing server
netstat -ano | findstr :8000
taskkill /PID <number> /F

# Then start again
.venv\Scripts\python.exe manage.py runserver
```

---

## Problem 2: Can't Login to Admin

**Symptoms:**
- "Invalid username or password"

**Solution:**
```powershell
cd "C:\Users\sean\Desktop\my website\backend"
.venv\Scripts\python.exe setup_initial_data.py
```

**Login:** admin / admin123

---

## Problem 3: Booking Form Shows Error

**Symptoms:**
- "Failed to fetch"
- "Is the Django server running?"

**Solution:**
1. Check PowerShell - is server running?
2. Look for: `Starting development server at http://127.0.0.1:8000/`
3. If not running, start it:
   ```powershell
   .venv\Scripts\python.exe manage.py runserver
   ```

---

## Problem 4: Email Not Sending

**Symptoms:**
- No emails received
- "Authentication failed"

**Solution:**
1. Open: `backend\.env`
2. Add your Outlook password:
   ```env
   EMAIL_HOST_PASSWORD=your-password-here
   ```
3. Restart server
4. Test again

---

## Problem 5: File Upload Fails

**Symptoms:**
- "File too large"
- "Invalid file type"

**Solution:**
- File must be JPG, PNG, or PDF
- File must be under 5MB
- Compress image if too large

---

## Problem 6: Payment Proof Not Showing

**Symptoms:**
- Proof uploaded but admin can't see it

**Solution:**
1. Check `backend\media\proofs\` folder exists
2. Check file was saved
3. Click the proof_of_payment link in admin
4. If still broken, re-upload

---

<a name="quick-reference"></a>
# 📇 10. Quick Reference Card

## ⚡ Super Quick Commands

### Start Server
```powershell
cd "C:\Users\sean\Desktop\my website\backend"
.venv\Scripts\python.exe manage.py runserver
```

### Stop Server
```
Ctrl + C
```

### Admin Panel
```
http://127.0.0.1:8000/admin
Username: admin
Password: admin123
```

### Reset Admin Password
```powershell
.venv\Scripts\python.exe setup_initial_data.py
```

---

## 📱 Important URLs

| What | URL |
|------|-----|
| **Admin Panel** | http://127.0.0.1:8000/admin |
| **Test API** | file:///C:/Users/sean/Desktop/my%20website/test-api.html |
| **Booking Form** | file:///C:/Users/sean/Desktop/my%20website/booking.html |
| **Upload Proof** | file:///C:/Users/sean/Desktop/my%20website/upload-proof.html |
| **Your Website** | file:///C:/Users/sean/Desktop/my%20website/index.html |

---

## 📂 Important Files

| File | What It Does |
|------|--------------|
| `backend\db.sqlite3` | Database (all bookings stored here) |
| `backend\.env` | Secret settings (email, passwords) |
| `backend\manage.py` | Django control center |
| `booking.html` | Booking form (customers use this) |
| `index.html` | Homepage |
| `packages.html` | Package listings |

---

## 📞 Emergency Contacts

**When Something Breaks:**

1. **Check PowerShell** - Is server running?
2. **Check Admin Panel** - Can you login?
3. **Check Email** - Did you add password in .env?
4. **Read Error Message** - What does it say?

---

## 🎓 Learning Path (Next Steps!)

### Week 1: Master the Basics
- ✅ Start/stop server
- ✅ Login to admin
- ✅ Create test booking
- ✅ Verify payment proof

### Week 2: Host Online
- ✅ Sign up for Render.com
- ✅ Deploy backend
- ✅ Test live bookings
- ✅ Connect custom domain (optional)

### Week 3: Optimize
- ✅ Setup email properly
- ✅ Test full booking flow
- ✅ Train someone else to be admin
- ✅ Create backup strategy

### Month 2: Grow!
- ✅ Get real customers
- ✅ Process real payments
- ✅ Monitor bookings
- ✅ Upgrade to paid hosting if needed

---

## 🎯 Success Checklist

Before Going Live:

- [ ] Server starts without errors
- [ ] Admin login works
- [ ] Can create test booking
- [ ] Success modal appears
- [ ] Booking shows in admin
- [ ] Can upload payment proof
- [ ] Proof shows in admin
- [ ] Can verify payment
- [ ] Emails are sending
- [ ] Customer gets confirmation email
- [ ] Hosted online (Render/Heroku/etc)
- [ ] Custom domain connected (optional)
- [ ] Tested on phone
- [ ] Tested on different browsers
- [ ] Someone else tested it
- [ ] Backup of database created

**When all checked ✅ → GO LIVE! 🚀**

---

## 💡 Pro Tips

### Tip 1: Keep Server Running
**Problem:** Computer goes to sleep, server stops

**Solution:**
- Windows Settings → Power → Never sleep (when plugged in)
- Or host online (server never sleeps!)

### Tip 2: Backup Your Database
**Every week, copy this file:**
```
backend\db.sqlite3
```
**Save to:** USB drive, Dropbox, Google Drive

### Tip 3: Monitor Bookings
**Daily:**
- Check email for "New Booking"
- Check admin for pending payments

**Weekly:**
- Count total bookings
- Check revenue
- Plan tours

### Tip 4: Test Often
**Before each tour day:**
- Test booking form
- Test payment upload
- Make sure server is running

### Tip 5: Communicate
**With customers:**
- Send payment instructions clearly
- Reply to emails quickly
- Confirm bookings within 24 hours

---

## 🎉 You're Ready!

You now know:
- ✅ How to start/stop server
- ✅ How long it runs
- ✅ How to be admin
- ✅ Daily tasks
- ✅ How to host FREE
- ✅ How to host PAID
- ✅ How to troubleshoot

**You built a professional booking system!** 🦁🌍

**Remember:**
- Start small (run locally)
- Test everything
- Host free first
- Upgrade when needed
- Ask for help if stuck

**Your booking system is ready to make money!** 💰🎊

---

## 📚 More Resources

**Documentation:**
- `README.md` - Full system documentation
- `ADMIN_GUIDE.md` - Admin panel guide
- `FRONTEND_INTEGRATION.md` - API documentation
- `HOW_TO_USE.md` - Frontend connection guide
- `EMAIL_SETUP.md` - Email configuration

**Online Help:**
- Django Docs: https://docs.djangoproject.com
- Django REST: https://www.django-rest-framework.org
- Python Help: https://python.org

**Video Tutorials:**
- "Django for Beginners" on YouTube
- "Deploy Django to Heroku" tutorials
- "Python Anywhere Django" guides

---

**🎊 Congratulations on Building Your Booking System! 🎊**

**You did it! Now go make some bookings!** 🚀🦁🌍
