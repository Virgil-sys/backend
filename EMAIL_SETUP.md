# 📧 Email Setup for seanzimucha@outlook.com

## ✅ What's Already Configured

Your `.env` file is set to use:
- **Email:** seanzimucha@outlook.com
- **SMTP Host:** smtp-mail.outlook.com
- **Port:** 587
- **TLS:** Enabled

## 🔑 What You Need to Add

You need to add your Outlook/Microsoft account password to the `.env` file.

### Option 1: Regular Password (Less Secure)
1. Open: `backend\.env`
2. Find line: `EMAIL_HOST_PASSWORD=`
3. Add your password: `EMAIL_HOST_PASSWORD=your-outlook-password`
4. Save file
5. Restart server

### Option 2: App Password (More Secure - Recommended)

**Step 1:** Generate App Password
1. Go to: https://account.microsoft.com/security
2. Sign in with seanzimucha@outlook.com
3. Click "Advanced security options"
4. Under "App passwords", click "Create a new app password"
5. Copy the generated password (example: `abcd efgh ijkl mnop`)

**Step 2:** Add to .env
1. Open: `backend\.env`
2. Find line: `EMAIL_HOST_PASSWORD=`
3. Paste the app password: `EMAIL_HOST_PASSWORD=abcd efgh ijkl mnop`
4. Save file
5. Restart server

## 🚀 How to Restart Server

**Windows PowerShell:**
```bash
# Stop current server: Ctrl + C

# Start again:
cd "C:\Users\sean\Desktop\my website\backend"
.venv\Scripts\activate
python manage.py runserver
```

## ✉️ Test Email

After adding password and restarting:

1. Open `test-api.html`
2. Click "Create Test Booking"
3. Check your email inbox (seanzimucha@outlook.com)
4. You should receive a "New booking" notification email!

## 🎯 Where Emails Are Sent

### Admin Email (you receive):
- **To:** seanzimucha@outlook.com
- **When:** New booking created
- **Subject:** "New Booking: [Package Title]"

### Customer Email:
- **To:** Customer's email (from booking form)
- **From:** seanzimucha@outlook.com
- **When:** Booking created
- **Subject:** "Booking Confirmation - Prairies Africa"
- **Content:** Bank details and payment instructions

## 🚨 Common Issues

### "Authentication failed"
- Check password is correct
- Make sure you're using the right email: seanzimucha@outlook.com
- Try app password instead of regular password

### "Connection refused"
- Check internet connection
- Make sure port 587 is not blocked by firewall
- Try `EMAIL_PORT=25` in .env as alternative

### "Emails not arriving"
- Check spam/junk folder
- Wait a few minutes (can be delayed)
- Check Django terminal for error messages

## 📝 Current .env Configuration

```env
# Email (Outlook SMTP)
EMAIL_HOST=smtp-mail.outlook.com
EMAIL_PORT=587
EMAIL_HOST_USER=seanzimucha@outlook.com
EMAIL_HOST_PASSWORD=           <-- ADD YOUR PASSWORD HERE
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=seanzimucha@outlook.com
```

---

**After adding password:**
1. Save .env
2. Restart Django server (Ctrl+C, then `python manage.py runserver`)
3. Test with test-api.html
4. Check your email!
