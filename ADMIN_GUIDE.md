# Admin Guide (Super Simple Version!)

## 🎯 What Is This?

Think of this backend like a **magic notebook** that:
- Remembers everyone who wants to go on tours (bookings)
- Keeps track of payments
- Sends emails automatically
- Lets you (the admin) check everything and approve payments

---

## 🔑 How to Log In as Admin

1. **Start the server** (if not running):
   - Open PowerShell in the backend folder
   - Type: `.venv\Scripts\activate`
   - Type: `python manage.py runserver`

2. **Open your web browser**
3. **Go to:** http://127.0.0.1:8000/admin
4. **Login:**
   - Username: `admin`
   - Password: `admin123`

✅ You're now in the admin dashboard!

---

## 👀 What You See as Admin

When you log in, you'll see a dashboard with sections like:

### 📋 **BOOKINGS**
- **Bookings** - All tour bookings from customers

### 👥 **CUSTOMERS**
- **Customers** - Everyone who has made a booking

### 💳 **PAYMENTS**
- **Bank accounts** - Your business bank accounts
- **Bank transfers** - All payment proofs from customers

### 🔐 **AUTHENTICATION AND AUTHORIZATION**
- **Users** - Admin users (like you!)

---

## 🚀 Your Daily Tasks as Admin

### Task 1: Check New Bookings

**When:** Every morning or multiple times a day

**What to do:**
1. Click **Bookings** in the left menu
2. You'll see a list of all bookings with:
   - Customer name
   - Package they booked
   - Price
   - Status (pending, confirmed, etc.)
   - Reference number

**What each status means:**
- 🟡 **Pending** = Waiting for payment
- 🟢 **Confirmed** = Payment verified, good to go!
- 🔴 **Cancelled** = Customer cancelled
- ⚫ **Completed** = Tour finished

---

### Task 2: Verify Payments (MOST IMPORTANT!)

**When:** After customers upload proof of payment

**What to do:**

#### Option A: Using the Admin Panel (Easy Way)
1. Click **Bank transfers** in the left menu
2. Look for entries with Status = **Pending**
3. Click on a pending transfer
4. You'll see:
   - The booking details
   - The proof of payment image/PDF (click to view)
   - Amount expected vs. amount customer says they paid
   - Transfer date
5. **Check the proof carefully:**
   - Does the amount match?
   - Does the reference number match?
   - Does the bank account match?
6. If everything looks good:
   - Change **Status** to **Verified**
   - Click **Save**
7. The booking automatically changes to "Confirmed"!

#### Option B: Using API (Advanced Way)
If you're using a custom admin interface:
- Call: `POST http://127.0.0.1:8000/api/payments/admin/bookings/{booking_id}/verify-payment/`
- You need to be logged in as admin

---

### Task 3: View All Pending Payments

**Quick way to see all proofs waiting for you:**

#### In Admin Panel:
1. Click **Bank transfers**
2. Filter by Status = "Pending" (use the filter on the right side)

#### Using API:
- Visit: `GET http://127.0.0.1:8000/api/payments/admin/payments/pending/`
- You'll see a list of all pending transfers

---

### Task 4: Manage Bank Accounts

**When:** Setting up or updating bank details

**What to do:**
1. Click **Bank accounts** in the left menu
2. Click **Add Bank Account** (top right)
3. Fill in:
   - **Bank name** (e.g., "FNB", "Standard Bank")
   - **Account name** (your business name)
   - **Account number**
   - **Branch code**
   - **SWIFT code** (for international)
   - **Currency** (ZAR, USD, etc.)
   - **Is active** ✅ (check this box!)
   - **Notes** (optional, like "For ZAR payments only")
4. Click **Save**

**Important:** Only accounts marked "Is active" will show to customers!

---

### Task 5: Check Customer Information

**When:** You need to contact a customer

**What to do:**
1. Click **Customers** in the left menu
2. Click on a customer name
3. You'll see:
   - Name, email, phone
   - Customer notes (allergies, special requests)
   - All their bookings (at the bottom)

---

### Task 6: Update Booking Status Manually

**When:** Something changes (customer cancels, tour completed, etc.)

**What to do:**
1. Click **Bookings**
2. Click on the booking
3. Change **Status** dropdown:
   - **Pending** → Waiting for payment
   - **Confirmed** → Paid and ready
   - **Cancelled** → Customer cancelled
   - **Completed** → Tour finished
4. Click **Save**

---

## 📧 Emails (Automatic!)

The system sends emails automatically:

### When a Booking is Created:
- ✉️ **You get an email** saying "New booking received!"
- ✉️ **Customer gets an email** with bank details and instructions

### When You Verify Payment:
- ✉️ **Customer gets an email** saying "Payment verified, booking confirmed!"

**Note:** To enable emails, you need to set up Gmail SMTP in the `.env` file.

---

## 🛠️ Common Admin Actions

### Search for Something:
- Use the search box at the top right of any list

### Filter Results:
- Use the filters on the right side of lists
- Example: Filter bookings by "Status = Confirmed"

### Sort by Column:
- Click on column headers to sort

### Bulk Actions:
- Select multiple items using checkboxes
- Choose an action from the dropdown above the list
- Click "Go"

---

## 📊 What You Should Monitor

### Daily Checks:
- ✅ New bookings
- ✅ Pending payment verifications
- ✅ Any email errors

### Weekly Checks:
- ✅ Completed bookings
- ✅ Cancelled bookings (why did they cancel?)
- ✅ Customer notes for upcoming tours

---

## 🚨 Troubleshooting

### "I can't log in!"
- Check username: `admin`
- Check password: `admin123`
- Make sure server is running

### "I don't see any bank accounts when creating a booking!"
- Go to **Bank accounts**
- Make sure at least one has "Is active" checked

### "Proof of payment image won't load!"
- Check that the `media` folder exists
- Check file was uploaded correctly

### "Emails aren't sending!"
- Check `.env` file has correct Gmail credentials
- Check Gmail allows "less secure apps" or use App Password

---

## 🎓 Simple Workflow Example

**Scenario:** Customer Jane books a safari

1. **Customer books online** 
   - Fills form on your website
   - Clicks "Book Now"

2. **System creates booking**
   - Status = "Pending"
   - Sends Jane an email with bank details
   - Sends YOU an email: "New booking!"

3. **You check admin panel**
   - See Jane's booking in the list
   - Note the reference number

4. **Jane makes bank transfer**
   - Uses the reference number
   - Goes to her bank and pays

5. **Jane uploads proof**
   - Takes screenshot of bank receipt
   - Uploads on your website

6. **You get notified**
   - See pending transfer in admin
   - Click to view proof
   - Check: Amount ✓ Reference ✓ Bank ✓

7. **You verify payment**
   - Change status to "Verified"
   - Click Save

8. **System confirms booking**
   - Booking status → "Confirmed"
   - Jane gets email: "Payment verified!"

9. **Tour happens**
   - After tour, you change status to "Completed"

✅ Done!

---

## 🎯 Tips for Being a Great Admin

1. **Check pending payments quickly** - Customers are waiting!
2. **Always verify bank proof carefully** - Don't approve wrong payments
3. **Keep customer notes updated** - Special requests matter
4. **Mark completed bookings** - Keeps records clean
5. **Check emails are working** - Test by making a booking yourself

---

## 🆘 Need More Help?

**Backend running?**
- Check terminal for errors
- Server should say: "Starting development server at http://127.0.0.1:8000/"

**Admin panel not loading?**
- Make sure you're at the right URL: http://127.0.0.1:8000/admin
- Check server is running

**Forgot admin password?**
- Run: `python setup_initial_data.py` (resets to `admin123`)

---

## 📝 Quick Reference Card

| Task | Where | What to Click |
|------|-------|---------------|
| View all bookings | Admin → Bookings | Click "Bookings" |
| Verify payment | Admin → Bank transfers | Find pending → Change to Verified |
| Add bank account | Admin → Bank accounts | "Add Bank Account" button |
| Check customer info | Admin → Customers | Click customer name |
| Change booking status | Admin → Bookings | Click booking → Change Status |
| View proof of payment | Admin → Bank transfers | Click transfer → View proof file |

---

## 🎉 You're All Set!

You now know how to:
- ✅ Log in as admin
- ✅ View bookings
- ✅ Verify payments
- ✅ Manage bank accounts
- ✅ Check customer details

**Remember:** Your main job is verifying payments quickly so customers can enjoy their tours! 🦁🌍

---

## Admin URLs Quick Access

- **Admin Panel:** http://127.0.0.1:8000/admin
- **API - All Bookings:** http://127.0.0.1:8000/api/payments/admin/bookings/
- **API - Pending Payments:** http://127.0.0.1:8000/api/payments/admin/payments/pending/

**Login:** admin / admin123
