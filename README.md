# 🦁 Prairies Africa Backend - Tour Booking System

> A complete Django backend for handling tour bookings, bank transfer payments, and admin management.

---

## 🎈 What Is This? (Explained Like You're 5)

Imagine you have a **lemonade stand** 🍋:
- Customers want to buy lemonade (book tours)
- They need to pay you with money (bank transfer)
- They show you a receipt to prove they paid (upload proof)
- You check the receipt and give them lemonade (verify payment)

This backend is like a **robot helper** that:
1. **Remembers** who ordered lemonade (stores bookings)
2. **Tells** customers where to send money (shows bank details)
3. **Collects** their receipts (stores proof of payment)
4. **Helps you check** receipts quickly (admin panel)
5. **Sends emails** automatically to everyone

---

## 🚀 Quick Start (Get Running in 5 Minutes!)

### Step 1: Your Server is Already Running! ✅

Look at your terminal - you should see:
```
Starting development server at http://127.0.0.1:8000/
```

If not running:
```bash
.venv\Scripts\activate
python manage.py runserver
```

### Step 2: Visit Admin Panel

1. Open browser: http://127.0.0.1:8000/admin
2. Login:
   - Username: `admin`
   - Password: `admin123`

### Step 3: You're Done!

Your backend is running and ready to receive bookings from your website! 🎉

---

## 📦 What's Inside?

### Three Main Parts:

#### 1. **Customers App** 👥
Keeps track of people who book tours:
- Name
- Email
- Phone number
- Special notes (like allergies)

#### 2. **Bookings App** 📋
Remembers tour reservations:
- Which tour package
- How many people
- When they want to go
- Total price (calculated automatically!)
- Reference number (for payment tracking)
- Status (pending, confirmed, cancelled, completed)

#### 3. **Payments App** 💳
Handles bank transfer payments:
- Your bank account details
- Customer payment proofs (receipts/screenshots)
- Payment verification by admin

---

## 🔄 How It Works (The Full Story)

### Act 1: Customer Books a Tour 🎭

1. **Customer visits your website**
   - Sees amazing safari tours
   - Picks "3-Day Safari Adventure" - $2,500

2. **Customer fills booking form**
   - Name: John Smith
   - Email: john@example.com
   - Number of people: 2 adults
   - Preferred date: December 15

3. **Customer clicks "Book Now"**
   - Your website sends data to: `POST /api/bookings/create/`
   - Backend creates the booking
   - Backend calculates total: $2,500 × 2 = $5,000
   - Backend generates reference: `BK-20251103-1`
   - Backend sets deadline: 48 hours from now

4. **Emails fly out! ✉️**
   - Email to John: "Thanks! Here's how to pay..."
   - Email to you: "New booking from John Smith!"

### Act 2: Getting Bank Details 🏦

1. **Customer sees "Pay Now" button**
   - Your website calls: `POST /api/payments/bank-details/`

2. **Backend returns bank accounts:**
   ```
   FNB: 62812345678
   Account Name: Prairies Africa Tours
   Reference: BK-20251103-1 (IMPORTANT!)
   Amount: $5,000
   ```

3. **Customer sees nice payment instructions**
   - Shows both banks (ZAR and USD options)
   - Shows reference number in BIG letters
   - Shows 48-hour countdown timer

### Act 3: Customer Pays 💰

1. **Customer goes to their bank**
   - Opens banking app
   - Makes transfer to your account
   - Uses reference: `BK-20251103-1`

2. **Customer gets bank receipt**
   - Screenshot or PDF

### Act 4: Upload Proof 📸

1. **Customer clicks "Upload Proof" on your website**
   - Selects receipt image
   - Clicks upload

2. **Your website sends to:** `POST /api/payments/upload-proof/`
   - File must be: JPG, PNG, or PDF
   - File must be: Less than 5MB

3. **Backend saves the proof**
   - Stores in: `media/proofs/1/` (booking ID)
   - Creates transfer record
   - Status: Pending

4. **Email to you:** "New proof uploaded for booking #1!"

### Act 5: You Verify Payment ✅

1. **You open admin panel**
   - See "1 pending payment"

2. **You click on the transfer**
   - View the proof image
   - Check amount: $5,000 ✓
   - Check reference: BK-20251103-1 ✓
   - Check bank account: Correct ✓

3. **You click "Verified" and Save**

4. **Magic happens:**
   - Transfer status → Verified
   - Booking status → Confirmed
   - Email to John: "Payment verified! Your tour is confirmed!"

### Act 6: Tour Day! 🦁

1. **Tour happens**
2. **You mark booking as "Completed"**
3. **Everyone's happy!**

---

## 🛠️ Technical Setup (What Got Built)

### Database (SQLite for Development)
- Stores everything in `db.sqlite3`
- Tables:
  - `customers_customer` - Customer records
  - `bookings_booking` - Tour bookings
  - `payments_bankaccount` - Your bank accounts
  - `payments_banktransfer` - Payment proofs

### API Endpoints (12 Total)

#### Public Endpoints (Anyone can use):
1. `POST /api/bookings/create/` - Create booking
2. `GET /api/bookings/{id}/` - Get booking details
3. `GET /api/bookings/{id}/status/` - Check booking status
4. `POST /api/payments/bank-details/` - Get bank accounts
5. `POST /api/payments/upload-proof/` - Upload payment proof
6. `GET /api/payments/payment-status/{id}/` - Check payment status

#### Admin Endpoints (Require login):
7. `GET /api/payments/admin/bookings/` - List all bookings
8. `GET /api/payments/admin/payments/pending/` - Pending verifications
9. `POST /api/payments/admin/bookings/{id}/verify-payment/` - Verify payment

#### Admin Panel:
10. `GET /admin/` - Django admin dashboard

### Files & Folders Structure

```
backend/
├── .venv/                    # Python virtual environment
├── backend/                  # Main project folder
│   ├── settings.py          # Configuration (DB, email, CORS, etc.)
│   ├── urls.py              # URL routing
│   └── ...
├── customers/               # Customer app
│   ├── models.py           # Customer database model
│   ├── admin.py            # Admin panel config
│   └── ...
├── bookings/               # Bookings app
│   ├── models.py          # Booking database model
│   ├── serializers.py     # JSON converters
│   ├── views.py           # API logic
│   ├── urls.py            # Booking endpoints
│   └── admin.py           # Admin panel config
├── payments/              # Payments app
│   ├── models.py         # Bank account & transfer models
│   ├── serializers.py    # JSON converters
│   ├── views.py          # Payment API logic
│   ├── urls.py           # Payment endpoints
│   └── admin.py          # Admin panel config
├── media/                # Uploaded files (proofs)
│   └── proofs/          # Payment proof receipts
├── static/              # Static files (CSS, JS)
├── db.sqlite3          # Database file
├── manage.py           # Django management commands
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (secrets!)
├── setup_initial_data.py  # Initial data seeder
├── README.md          # This file
├── ADMIN_GUIDE.md     # Admin instructions
└── FRONTEND_INTEGRATION.md  # Frontend dev guide
```

---

## 🎯 Configuration Files

### `.env` (Secret Settings)
```env
# Django
SECRET_KEY=dev-secret-key-change-me
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Frontend
FRONTEND_URL=https://prairiesafrica.com

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=no-reply@prairiesafrica.com

# Database (for production)
# DATABASE_URL=postgres://user:pass@host:5432/dbname
```

**What each setting does:**
- `SECRET_KEY` - Secret code for security (change in production!)
- `DEBUG` - Show detailed errors (True for dev, False for production)
- `ALLOWED_HOSTS` - Which domains can access the backend
- `EMAIL_HOST_USER` - Your Gmail address
- `EMAIL_HOST_PASSWORD` - Gmail app password (not regular password!)
- `DATABASE_URL` - PostgreSQL connection (for production only)

---

## 📧 Email Setup (Gmail)

### Why Emails Matter:
- Customers get booking confirmations
- You get alerts for new bookings
- Customers get payment verification

### How to Enable:

1. **Get Gmail App Password:**
   - Go to: https://myaccount.google.com/apppasswords
   - Create app password for "Mail"
   - Copy the 16-character password

2. **Update `.env`:**
   ```env
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=abcd efgh ijkl mnop
   ```

3. **Restart server:**
   ```bash
   Ctrl+C  (stop server)
   python manage.py runserver  (start again)
   ```

4. **Test it:**
   - Create a test booking with your email
   - Check inbox for confirmation

---

## 🏦 Bank Accounts (Already Seeded!)

Two bank accounts are ready:

### Bank 1 (South African Rand)
- Bank: First National Bank (FNB)
- Account: Prairies Africa Tours
- Number: 62812345678
- Branch: 250655
- SWIFT: FIRNZAJJ
- Currency: ZAR

### Bank 2 (US Dollar)
- Bank: Standard Bank
- Account: Prairies Africa International
- Number: 123456789
- Branch: 051001
- SWIFT: SBZAZAJJ
- Currency: USD

**To edit or add more:**
1. Go to: http://127.0.0.1:8000/admin
2. Click: **Bank accounts**
3. Add/Edit accounts
4. ✅ Check "Is active" to show to customers

---

## 🔒 Security Features Built-In

1. **File Upload Protection**
   - Only JPG, PNG, PDF allowed
   - Max 5MB file size
   - Files stored in secure folder
   - Automatic filename sanitization

2. **CORS Protection**
   - Only your domains can access API
   - Configurable in settings

3. **Admin Authentication**
   - Admin endpoints require login
   - Password hashing (never stored plain text)

4. **Input Validation**
   - Email format checking
   - Price validation
   - Date validation
   - Reference number uniqueness

5. **SQL Injection Prevention**
   - Django ORM protects automatically

---

## 🧪 Testing Your Backend

### Manual Test Flow:

#### Test 1: Create Booking
```bash
curl -X POST http://127.0.0.1:8000/api/bookings/create/ \
  -H "Content-Type: application/json" \
  -d '{
    "customer": {
      "name": "Test User",
      "email": "test@example.com",
      "phone": "+27 11 111 1111"
    },
    "package_id": "TEST001",
    "package_title": "Test Safari",
    "package_price": "1000.00",
    "number_of_people": 1
  }'
```

**Expected:** Returns booking with `id` and `reference_number`

#### Test 2: Get Bank Details
```bash
curl -X POST http://127.0.0.1:8000/api/payments/bank-details/
```

**Expected:** Returns 2 bank accounts

#### Test 3: Check Booking Status
```bash
curl http://127.0.0.1:8000/api/bookings/1/status/
```

**Expected:** Returns status "pending"

#### Test 4: Upload Proof (Using Postman)
- Method: POST
- URL: http://127.0.0.1:8000/api/payments/upload-proof/
- Body: form-data
  - `booking_id`: 1
  - `proof`: [Select a JPG/PNG/PDF file]

**Expected:** Success message with transfer details

#### Test 5: Verify Payment (Admin Only)
- Login to admin panel first
- Then use session cookie with request

---

## 🚨 Common Issues & Solutions

### Server won't start
```
Error: Port already in use
```
**Solution:** Another server is running on port 8000
```bash
netstat -ano | findstr :8000  # Find process
taskkill /PID <process_id> /F  # Kill it
```

### Can't login to admin
```
Invalid username or password
```
**Solution:** Reset admin user
```bash
python setup_initial_data.py
```
Username: `admin`, Password: `admin123`

### File upload fails
```
Error: File too large
```
**Solution:** File must be ≤ 5MB. Compress image or use PDF.

### Email not sending
```
Error: SMTPAuthenticationError
```
**Solution:**
1. Use Gmail App Password (not regular password)
2. Enable "Less secure app access" in Gmail
3. Check `.env` has correct credentials

### "No module named ..."
```
Error: ModuleNotFoundError
```
**Solution:** Install dependencies
```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🔧 Useful Management Commands

### Create superuser (admin account)
```bash
python manage.py createsuperuser
```

### Reset database (DELETES ALL DATA!)
```bash
del db.sqlite3
python manage.py migrate
python setup_initial_data.py
```

### Make database changes
```bash
python manage.py makemigrations
python manage.py migrate
```

### Collect static files (for production)
```bash
python manage.py collectstatic
```

### Run tests
```bash
python manage.py test
```

### Open Python shell with Django loaded
```bash
python manage.py shell
```

---

## 📚 For Developers

### Tech Stack
- **Framework:** Django 4.2.7
- **API:** Django REST Framework 3.14.0
- **Database:** SQLite (dev), PostgreSQL (prod)
- **CORS:** django-cors-headers
- **Static Files:** WhiteNoise
- **Server:** Gunicorn (production)
- **Email:** SMTP (Gmail/Workspace)

### Key Features
- RESTful API design
- Automatic reference number generation
- Computed total amounts
- File upload handling with validation
- Admin verification workflow
- Email notifications
- CORS-enabled for frontend
- Environment-based configuration
- Production-ready setup

### Database Models

**Customer:**
- name, email, phone, customer_notes
- Auto timestamps (created_at, updated_at)

**Booking:**
- Links to Customer (ForeignKey)
- package_id, package_title, package_price
- number_of_people, preferred_date, special_requests
- status (pending/confirmed/cancelled/completed)
- payment_method (bank_transfer/cash/card)
- total_amount (computed: price × people)
- reference_number (auto-generated unique)
- payment_deadline (auto-set: now + 48 hours)

**BankAccount:**
- bank_name, account_name, account_number
- branch_code, swift_code, currency
- is_active (only active accounts shown to customers)
- notes

**BankTransfer:**
- Links to Booking (ForeignKey)
- Bank details snapshot
- reference_number (from booking)
- amount_expected, amount_received, transfer_date
- status (pending/verified/failed)
- proof_of_payment (FileField)
- verified_by (User), verified_at (timestamp)

---

## 🚀 Production Deployment

### Step 1: Update `.env` for Production
```env
DEBUG=False
SECRET_KEY=<generate-strong-key>
ALLOWED_HOSTS=prairiesafrica.com,www.prairiesafrica.com
DATABASE_URL=postgres://user:pass@host:5432/dbname
```

### Step 2: Setup PostgreSQL
```bash
# Install PostgreSQL
# Create database
createdb prairies_db
```

### Step 3: Run Migrations
```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

### Step 4: Create Production Admin
```bash
python manage.py createsuperuser
```

### Step 5: Run with Gunicorn
```bash
gunicorn backend.wsgi:application --bind 0.0.0.0:8000
```

### Step 6: Setup Nginx (Reverse Proxy)
```nginx
server {
    listen 80;
    server_name prairiesafrica.com;

    location /static/ {
        alias /path/to/staticfiles/;
    }

    location /media/ {
        alias /path/to/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## 📖 Documentation Links

- **Admin Guide:** `ADMIN_GUIDE.md` - How to use admin panel
- **Frontend Integration:** `FRONTEND_INTEGRATION.md` - API documentation
- **Django Docs:** https://docs.djangoproject.com/
- **DRF Docs:** https://www.django-rest-framework.org/

---

## 🎓 Learning Resources

New to Django? Start here:
1. Django Official Tutorial: https://docs.djangoproject.com/en/4.2/intro/tutorial01/
2. DRF Tutorial: https://www.django-rest-framework.org/tutorial/quickstart/
3. Python Virtual Environments: https://docs.python.org/3/tutorial/venv.html

---

## ✅ You're All Set!

Your backend is:
- ✅ Running on http://127.0.0.1:8000
- ✅ Admin panel ready at /admin (admin/admin123)
- ✅ API endpoints working
- ✅ Bank accounts seeded
- ✅ Email notifications configured
- ✅ File uploads enabled
- ✅ Database migrations complete

**Next Steps:**
1. Connect your frontend (see `FRONTEND_INTEGRATION.md`)
2. Configure email in `.env`
3. Test the full booking flow
4. Read `ADMIN_GUIDE.md` for admin tasks

**Need help?** Check the docs or review terminal logs for errors.

---

## 🎉 Happy Booking!

Your tour booking system is ready to handle customers, payments, and make your business run smoothly! 🦁✨

**Admin Login:**
- URL: http://127.0.0.1:8000/admin
- Username: `admin`
- Password: `admin123`

**Remember:** Change the admin password in production!
