# ⚡ Quick Start Cheat Sheet

## 🚀 Start the Server

```bash
cd "C:\Users\sean\Desktop\my website\backend"
.venv\Scripts\activate
python manage.py runserver
```

**Server running at:** http://127.0.0.1:8000

---

## 🔑 Admin Access

**URL:** http://127.0.0.1:8000/admin

**Login:**
- Username: `admin`
- Password: `admin123`

---

## 📋 API Endpoints (For Frontend)

### Create Booking
```
POST http://127.0.0.1:8000/api/bookings/create/
```

### Get Bank Details
```
POST http://127.0.0.1:8000/api/payments/bank-details/
```

### Upload Proof
```
POST http://127.0.0.1:8000/api/payments/upload-proof/
Content-Type: multipart/form-data
```

### Check Payment Status
```
GET http://127.0.0.1:8000/api/payments/payment-status/{booking_id}/
```

---

## 👨‍💼 Your Daily Admin Tasks

1. **Open admin panel:** http://127.0.0.1:8000/admin
2. **Click "Bank transfers"**
3. **Filter by Status = "Pending"**
4. **View proof images**
5. **Change Status to "Verified"**
6. **Click Save**

✅ Done! Customer gets confirmation email automatically.

---

## 🏦 Bank Accounts (Already Set Up)

✅ FNB (ZAR) - 62812345678  
✅ Standard Bank (USD) - 123456789

**To edit:** Admin → Bank accounts

---

## 🛠️ Common Commands

### Stop server
```
Ctrl + C
```

### Reset admin password
```bash
python setup_initial_data.py
```

### View all bookings (as JSON)
```
http://127.0.0.1:8000/api/payments/admin/bookings/
```

---

## 📁 Important Files

- **README.md** - Full documentation
- **ADMIN_GUIDE.md** - How to be admin
- **FRONTEND_INTEGRATION.md** - How to connect frontend
- **.env** - Secret settings (email, passwords)

---

## 🔥 Testing Quick

**Test booking (copy-paste in PowerShell):**

```powershell
curl -X POST http://127.0.0.1:8000/api/bookings/create/ `
  -H "Content-Type: application/json" `
  -d '{\"customer\": {\"name\": \"Test\", \"email\": \"test@test.com\", \"phone\": \"+27111111111\"}, \"package_id\": \"TEST\", \"package_title\": \"Safari\", \"package_price\": \"1000\", \"number_of_people\": 1}'
```

**Test bank details:**

```powershell
curl -X POST http://127.0.0.1:8000/api/payments/bank-details/
```

---

## ✅ Is Everything Working?

- [ ] Server running? (Check terminal says "Starting development server")
- [ ] Admin login works? (Go to /admin and login)
- [ ] Can create booking? (Test API or use admin)
- [ ] Bank accounts showing? (2 accounts in admin)
- [ ] Can upload files? (Test proof upload)

---

## 🆘 Problems?

**Server won't start:**
```bash
# Kill existing server
netstat -ano | findstr :8000
taskkill /PID <number> /F
```

**Can't login:**
```bash
python setup_initial_data.py
# Then try: admin / admin123
```

**Module errors:**
```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

---

## 📧 Enable Email

1. Get Gmail App Password: https://myaccount.google.com/apppasswords
2. Edit `.env`:
   ```
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   ```
3. Restart server

---

## 🎯 What You Built

- ✅ Customer database
- ✅ Booking system with auto-calculation
- ✅ Payment proof upload (5MB max, JPG/PNG/PDF)
- ✅ Admin verification workflow
- ✅ Email notifications
- ✅ Bank account management
- ✅ RESTful API for frontend
- ✅ Admin dashboard

---

## 🎉 Ready to Go!

**Your backend handles:**
1. Customers book tours on your website
2. System shows bank details automatically
3. Customers upload payment proof
4. You verify payments in admin panel
5. System confirms bookings automatically
6. Everyone gets email notifications

**All automatic! You just verify payments!** ⚡

---

**Need more help?** Read the full guides:
- Simple explanation → **README.md**
- Admin tasks → **ADMIN_GUIDE.md**
- Connect frontend → **FRONTEND_INTEGRATION.md**
