# 🦁 Prairies Africa - One-Page Cheat Sheet

---

## 🚀 START SERVER (Do This First!)

```powershell
cd "C:\Users\sean\Desktop\my website\backend"
.venv\Scripts\python.exe manage.py runserver
```

**Wait for:** `Starting development server at http://127.0.0.1:8000/`

**✅ Server is now ON!** Don't close PowerShell!

---

## 🛑 STOP SERVER (When Done)

Press `Ctrl + C` in PowerShell window

---

## 👨‍💼 LOGIN AS ADMIN

1. Go to: **http://127.0.0.1:8000/admin**
2. Username: `admin`
3. Password: `admin123`

---

## 📋 DAILY TASKS (5-10 minutes)

### Morning:
1. ✅ Start server (see above)
2. ✅ Check email for "New Booking"
3. ✅ Login to admin panel

### Check Payments:
1. Click **"Bank transfers"**
2. Look for **Status = Pending**
3. Click on pending transfer
4. View proof image
5. Check: Amount ✓ Reference ✓ Bank ✓
6. Change **Status** to **"Verified"**
7. Click **"Save"**

### Evening:
1. ✅ Mark completed tours as "Completed"
2. ✅ Stop server (if done)

---

## 🌐 IMPORTANT URLs

| What | URL |
|------|-----|
| **Admin Panel** | http://127.0.0.1:8000/admin |
| **Your Website** | Open `index.html` in browser |
| **Test API** | Open `test-api.html` in browser |

---

## 🆓 HOST ONLINE FREE (20 minutes)

**Best Option: Render.com**

1. Go to https://render.com
2. Sign up with GitHub
3. Push your code to GitHub
4. Create "Web Service"
5. Connect your repo
6. Add environment variables
7. Deploy!

**Your site will be:** https://your-name.onrender.com

---

## 💰 HOST ONLINE PAID (When Growing)

**Best Option: Heroku - $12/month**

1. Go to https://heroku.com
2. Install Heroku CLI
3. Run:
   ```bash
   heroku create prairies-africa
   git push heroku main
   ```

---

## 🚨 TROUBLESHOOTING

### Server won't start?
```powershell
netstat -ano | findstr :8000
taskkill /PID <number> /F
```

### Can't login?
```powershell
.venv\Scripts\python.exe setup_initial_data.py
```
**Then:** admin / admin123

### Booking form error?
- Check server is running!
- Look for: `Starting development server...`

### No emails?
- Open `backend\.env`
- Add: `EMAIL_HOST_PASSWORD=your-password`
- Restart server

---

## ⏰ HOW LONG DOES SERVER RUN?

**Answer:** As long as PowerShell is open!

| You Do | Server Status |
|--------|---------------|
| PowerShell open | 🟢 ON |
| PowerShell closed | 🔴 OFF |
| Computer off | 🔴 OFF |
| Computer sleep | 🔴 OFF |

**For 24/7:** Host online (see above)

---

## 📞 QUICK FIXES

**Problem:** Forgot admin password  
**Fix:** Run `setup_initial_data.py`

**Problem:** Server error  
**Fix:** Restart server (Ctrl+C, then run again)

**Problem:** Form not working  
**Fix:** Check server is running

**Problem:** Proof upload fails  
**Fix:** File must be JPG/PNG/PDF, under 5MB

---

## 📁 BACKUP (Do This Weekly!)

**Copy this file:**
```
backend\db.sqlite3
```

**Save to:** USB drive / Google Drive / Dropbox

**Why:** All your bookings are in this file!

---

## ✅ GO-LIVE CHECKLIST

Before accepting real customers:

- [ ] Server starts OK
- [ ] Admin login works
- [ ] Test booking works
- [ ] Payment proof uploads
- [ ] Can verify payments
- [ ] Emails sending
- [ ] Hosted online
- [ ] Tested on phone
- [ ] Database backed up

**All checked? GO LIVE! 🚀**

---

## 💡 REMEMBER

- ✅ Keep PowerShell open = Server runs
- ✅ Check email daily for new bookings
- ✅ Verify payments within 24 hours
- ✅ Backup database weekly
- ✅ Start FREE hosting, upgrade later

---

## 📧 YOUR EMAIL

**Admin email:** seanzimucha@outlook.com

**Add password to `.env` file for emails to work!**

---

**🎉 You Got This! Your Booking System is Ready! 🦁🌍**

**Questions? Check `COMPLETE_MANUAL.md` for full guide!**
