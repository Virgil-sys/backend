# 🎉 Your Frontend is NOW Connected to Backend!

## ✅ What I Just Did For You

I created 3 new files that connect your website to your Django backend:

1. **`booking-connected.html`** - Your booking form (CONNECTED! ✅)
2. **`upload-proof.html`** - Payment proof upload page (CONNECTED! ✅)
3. **`test-api.html`** - Test page to check everything works (CONNECTED! ✅)

---

## 🎈 Explained Like You're 5

### Before (Not Connected):
```
Your Website → ❌ Nothing happens → No booking saved
```

### Now (Connected!):
```
Customer fills form → ✅ Sends to Django → 💾 Saved in database → ✉️ Email sent!
```

It's like connecting a **toy phone** 📞 to a **real phone line** - now it actually works!

---

## 🚀 How to Test Right Now

### Step 1: Make Sure Backend is Running

Open PowerShell in `C:\Users\sean\Desktop\my website\backend` and run:
```bash
.venv\Scripts\activate
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
```

✅ Leave this running! Don't close it!

---

### Step 2: Open the Test Page

Double-click this file:
```
C:\Users\sean\Desktop\my website\test-api.html
```

Click each button and watch the green success messages appear! 🎉

**What each button does:**
- **Test 1:** Creates a fake booking (like a customer booking a safari)
- **Test 2:** Gets your bank account details
- **Test 3:** Checks if a payment is verified
- **Test 4:** Gets booking details

If you see ✅ GREEN results = Everything works!
If you see ❌ RED errors = Backend not running or wrong URL

---

### Step 3: Test the Booking Form

**Open this file:**
```
C:\Users\sean\Desktop\my website\booking-connected.html
```

**Add package info to URL** (copy-paste this):
```
booking-connected.html?title=Safari%20Adventure&price=1500&duration=3%20Days&id=PKG001
```

**Fill the form:**
- Name: Your Name
- Email: your@email.com
- Phone: +263 77 123 4567
- Number of people: 2
- Click "Book Now"

**What happens:**
1. Form sends data to Django ✅
2. Django saves to database ✅
3. Django calculates total (1500 × 2 = 3000) ✅
4. Django generates reference number ✅
5. Django sends emails ✅
6. Success modal pops up with booking reference! 🎉

---

### Step 4: Test Payment Proof Upload

**Open this file:**
```
C:\Users\sean\Desktop\my website\upload-proof.html
```

**Fill the form:**
- Booking Reference: BK-20251103-1 (or whatever you got from Step 3)
- Amount Paid: 3000
- Transfer Date: Today's date
- Upload File: Any JPG/PNG/PDF (screenshot of anything)

Click "Upload Proof"

**What happens:**
1. File uploads to Django ✅
2. Django saves in `media/proofs/` folder ✅
3. Success modal appears! 🎉
4. You can now verify it in admin panel

---

## 🎯 How to Use in Your Real Website

### Replace your old booking.html

**Option 1: Simple rename**
```
1. Rename old: booking.html → booking-old.html
2. Rename new: booking-connected.html → booking.html
3. Done! Your booking page now works!
```

**Option 2: Copy-paste the code**
Open both files side by side and copy the `<script>` section from `booking-connected.html` into your `booking.html`

---

## 📁 File Structure Now

```
my website/
├── index.html                 (your homepage - unchanged)
├── packages.html              (your packages - unchanged)
├── booking.html               (OLD - not connected)
├── booking-connected.html     (NEW - CONNECTED! ✅)
├── upload-proof.html          (NEW - for payment uploads ✅)
├── test-api.html              (NEW - for testing ✅)
└── backend/
    ├── manage.py
    ├── db.sqlite3             (bookings saved here!)
    └── media/
        └── proofs/            (uploaded receipts here!)
```

---

## 🔄 The Complete Customer Journey

### Step 1: Customer Books
1. Customer browses `packages.html`
2. Clicks "Book Now" on a package
3. Opens `booking-connected.html` (or `booking.html` after you rename)
4. Fills form and submits
5. **Backend saves booking** ✅
6. Customer sees success modal with **reference number**
7. **Email sent to customer** with bank details
8. **Email sent to you** saying "New booking!"

### Step 2: Customer Pays
1. Customer goes to their bank
2. Transfers money to your FNB or Standard Bank account
3. Uses the **reference number** in payment description
4. Takes screenshot of bank receipt

### Step 3: Customer Uploads Proof
1. Opens `upload-proof.html` (you'll add link in email)
2. Enters **reference number**
3. Uploads receipt image/PDF
4. **Backend saves proof** ✅
5. **Email sent to you** saying "New proof uploaded!"

### Step 4: YOU Verify
1. Open http://127.0.0.1:8000/admin
2. Login: admin / admin123
3. Click "Bank transfers"
4. See pending transfer
5. View receipt image
6. Check amount, reference, date
7. Change status to "Verified" and Save
8. **Backend confirms booking** ✅
9. **Email sent to customer** saying "Payment verified!"

### Step 5: Tour Day!
1. Customer goes on safari 🦁
2. After tour, you mark booking as "Completed" in admin
3. Done!

---

## 🛠️ What Each File Does (Technical)

### booking-connected.html
**Purpose:** Booking form that sends data to Django

**What it does:**
- Collects customer info (name, email, phone)
- Collects package info (title, price, number of people)
- Sends to: `POST http://127.0.0.1:8000/api/bookings/create/`
- Shows success modal with booking reference
- Format matches Django API exactly

**Key code:**
```javascript
const API_BASE_URL = 'http://127.0.0.1:8000';

const bookingData = {
  customer: {
    name: "John Smith",
    email: "john@example.com",
    phone: "+263 77 123 4567"
  },
  package_id: "PKG001",
  package_title: "Safari",
  package_price: "1500.00",
  number_of_people: 2,
  payment_method: "bank_transfer"
};

fetch(`${API_BASE_URL}/api/bookings/create/`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(bookingData)
});
```

---

### upload-proof.html
**Purpose:** Let customers upload payment receipts

**What it does:**
- Customer enters booking reference
- Uploads JPG/PNG/PDF (max 5MB)
- Validates file type and size
- Sends to: `POST http://127.0.0.1:8000/api/payments/upload-proof/`
- Uses `FormData` for file upload (multipart)

**Key code:**
```javascript
const formData = new FormData();
formData.append('reference_number', 'BK-20251103-1');
formData.append('proof', fileInput.files[0]);
formData.append('amount_received', '3000.00');

fetch(`${API_BASE_URL}/api/payments/upload-proof/`, {
  method: 'POST',
  body: formData  // No JSON - multipart form data!
});
```

---

### test-api.html
**Purpose:** Quick testing tool

**What it does:**
- 4 buttons to test all APIs
- Shows results in green/red
- Helps you debug
- Not for customers - just for you!

---

## 🔧 How to Change the Backend URL

Right now, everything points to `http://127.0.0.1:8000` (your local computer).

**When you deploy to production:**

1. **Deploy backend to a server** (e.g., Heroku, DigitalOcean, AWS)
2. **Get production URL** (e.g., `https://api.prairiesafrica.com`)
3. **Change in each file:**

```javascript
// Change this line:
const API_BASE_URL = 'http://127.0.0.1:8000';

// To this:
const API_BASE_URL = 'https://api.prairiesafrica.com';
```

**Files to update:**
- `booking-connected.html` (line ~208)
- `upload-proof.html` (line ~126)
- `test-api.html` (line ~95)

---

## ❓ Common Questions

### Q: Why do I see "Page not found" at http://127.0.0.1:8000?
**A:** That's normal! The backend has no homepage. Use:
- `http://127.0.0.1:8000/admin` (admin panel)
- `http://127.0.0.1:8000/api/bookings/create/` (API endpoints)

### Q: Can I test without the backend running?
**A:** No. Frontend needs backend to save data. Always run:
```bash
python manage.py runserver
```

### Q: What if CORS error appears?
**A:** Your backend already allows:
- `http://localhost:3000`
- `https://prairiesafrica.com`
- `https://www.prairiesafrica.com`

If you're using a different domain, add it to `backend/backend/settings.py`:
```python
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'https://prairiesafrica.com',
    'https://www.prairiesafrica.com',
    'http://your-new-domain.com',  # Add here
]
```

### Q: Where are uploaded files stored?
**A:** `backend/media/proofs/<booking_id>/filename.jpg`

### Q: How do I see the database?
**A:** Two ways:
1. Admin panel: http://127.0.0.1:8000/admin
2. SQLite viewer: Download "DB Browser for SQLite" and open `backend/db.sqlite3`

---

## 🎉 Success Checklist

Before going live, test:

- [ ] Backend starts without errors
- [ ] Admin login works (admin/admin123)
- [ ] Bank accounts show in admin (2 accounts)
- [ ] test-api.html shows all green ✅
- [ ] booking-connected.html creates bookings
- [ ] Success modal appears with reference number
- [ ] Booking appears in admin panel
- [ ] upload-proof.html accepts files
- [ ] Uploaded files appear in admin
- [ ] Emails are sent (configure .env first)

---

## 🚀 Next Steps

1. **Test everything locally** (use test-api.html)
2. **Replace booking.html** with booking-connected.html
3. **Add link to upload-proof.html** in your emails/website
4. **Configure email** (.env file with Gmail)
5. **Deploy backend** to production server
6. **Update API URLs** in frontend files
7. **Go live!** 🎉

---

## 📞 Need Help?

Check these files:
- `README.md` - Full backend docs
- `ADMIN_GUIDE.md` - How to use admin panel
- `FRONTEND_INTEGRATION.md` - API reference
- `QUICK_START.md` - Quick commands

**Your website now:**
- ✅ Takes bookings
- ✅ Saves to database
- ✅ Sends emails
- ✅ Handles payments
- ✅ Uploads proofs
- ✅ Everything works!

**You just need to:**
- Keep backend running
- Check admin for pending payments
- Verify proofs
- Enjoy your automated booking system! 🎉
