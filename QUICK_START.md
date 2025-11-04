# 🚀 Praires Africa - Quick Start Guide

## ⚡ 5-Minute Setup

### Step 1: Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### Step 2: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Create Admin User
```bash
python manage.py createsuperuser
```
Enter:
- Username: admin (or your choice)
- Email: seantakudzwa050505@gmail.com
- Password: (choose strong password)

### Step 4: Start Server
```bash
# Option A: Use batch file
START_SERVER_FOREVER.bat

# Option B: Manual
python manage.py runserver
```

### Step 5: Test
- Open `index.html` in browser
- Admin: http://127.0.0.1:8000/admin/
- Make test booking
- Check admin panel

---

## 🔧 Configure Email (Required for Production)

### Get Gmail App Password:
1. Go to: https://myaccount.google.com/security
2. Enable "2-Step Verification"
3. Go to: https://myaccount.google.com/apppasswords
4. Select "Mail" → "Windows Computer"
5. Copy 16-character password

### Update backend/.env:
```env
EMAIL_HOST_USER=seantakudzwa050505@gmail.com
EMAIL_HOST_PASSWORD=xxxx xxxx xxxx xxxx
EMAIL_USE_TLS=True
```

---

## ⚠️ Important: Update Bank Details

**File**: `backend/bookings/views.py`

**Lines to update**: 241-259 (customer email) and similar in admin email

Find this section:
```python
<div class="info-row">
    <span class="label">Bank Name:</span>
    <span class="value">Standard Bank</span>
</div>
<div class="info-row">
    <span class="label">Account Number:</span>
    <span class="value"><strong>123456789</strong></span>
</div>
```

Replace with your actual bank details!

---

## 📋 Daily Workflow

### Morning:
1. Open admin panel: http://127.0.0.1:8000/admin/
2. Check "Bookings" → filter by "Pending"
3. Review new bookings from email notifications

### When Payment Received:
1. Find booking by reference number
2. Change status to "Confirmed"
3. Customer receives auto-update (if they refresh status page)

### End of Day:
- Review all pending bookings
- Follow up on overdue payments (marked with ⚠️)

---

## 🐛 Common Issues & Fixes

### Issue: Emails not sending
**Fix**: Check Gmail App Password in `.env` file

### Issue: "Module not found: jazzmin"
**Fix**: `pip install django-jazzmin==2.6.0`

### Issue: Database errors after update
**Fix**: 
```bash
python manage.py makemigrations
python manage.py migrate
```

### Issue: Static files not loading
**Fix**: `python manage.py collectstatic`

### Issue: CORS errors in browser console
**Fix**: Check `CORS_ALLOWED_ORIGINS` in `settings.py`

---

## 📞 Quick Links

- **Admin Panel**: http://127.0.0.1:8000/admin/
- **API Docs**: http://127.0.0.1:8000/api/
- **Full Guide**: See `DEPLOYMENT_GUIDE.md`
- **Summary**: See `IMPLEMENTATION_SUMMARY.md`

---

## 🎯 Testing Checklist

Quick test before going live:

- [ ] Create test booking
- [ ] Verify email received (admin + customer)
- [ ] Check payment status page
- [ ] Test additional activities
- [ ] Change booking status in admin
- [ ] Verify price calculations
- [ ] Test on mobile device
- [ ] Check all links work

---

## 🚀 Ready to Deploy?

See `DEPLOYMENT_GUIDE.md` for complete deployment instructions to:
- PythonAnywhere (FREE - easiest)
- Heroku
- Render
- Railway

All options include step-by-step instructions!

---

**Need Help?**
- 📧 seantakudzwa050505@gmail.com
- 📱 WhatsApp: +263 77 693 0966
