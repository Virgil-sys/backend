# 🔧 URGENT FIXES - Praires Booking System

## Issues Found & Fixed:

### ❌ Problem 1: Admin Page Not Accessible
**Cause**: Server not running

### ❌ Problem 2: Bookings Not Going Through  
**Cause**: Server not running + old single-activity system

### ❌ Problem 3: Limited to 5 Activities
**Cause**: Hardcoded dropdown - now fixed with unlimited selection system

---

## ✅ SOLUTION: New Unlimited Activities System

I've completely redesigned the system to support **unlimited** activities, transport, and accommodation selection.

### New Features:
- ✅ Select as many activities as you want
- ✅ Add transport options
- ✅ Add accommodation
- ✅ Real-time price calculator
- ✅ Better UI with category tabs

---

## 🚀 HOW TO FIX & START (Step-by-Step)

### Step 1: Install New Dependencies
```bash
cd backend
pip install djangorestframework
```
(Already have it, but making sure)

### Step 2: Run Migrations for New System
```bash
python manage.py makemigrations activities
python manage.py makemigrations bookings
python manage.py migrate
```

### Step 3: Populate Activities Database
```bash
python manage.py shell < populate_activities.py
```

This adds:
- 10 Activities (bungee, rafting, elephant ride, etc.)
- 6 Transport options (airport transfer, car rental, etc.)
- 6 Accommodation options (budget to luxury)

### Step 4: Create Admin User (if not already done)
```bash
python manage.py createsuperuser
```
Enter:
- Username: admin
- Email: seantakudzwa050505@gmail.com  
- Password: (your choice - remember it!)

### Step 5: Start Server
```bash
python manage.py runserver
```

Keep this terminal open!

### Step 6: Test the System

**Test Admin Panel:**
1. Open browser: http://127.0.0.1:8000/admin/
2. Login with your admin credentials
3. Click "Activities" - you should see all items
4. Click "Bookings" - check if styled correctly

**Test Booking:**
1. Open `booking-new.html` in browser
2. Fill in customer details
3. Click through tabs: Activities, Transport, Accommodation
4. Select multiple items (unlimited!)
5. Watch price update in real-time
6. Submit booking
7. Check admin panel for new booking

---

## 📁 New File Structure

```
backend/
├── activities/              ← NEW APP
│   ├── models.py           (Activity, BookingActivity)
│   ├── admin.py            (Manage activities)
│   ├── views.py            (API endpoints)
│   └── serializers.py      (JSON API)
├── bookings/
│   └── models.py           (Updated for multiple activities)
└── populate_activities.py  ← Run this to add items
```

Frontend:
```
booking-new.html            ← NEW unlimited booking page
booking.html                ← OLD (keep as backup)
```

---

## 🎯 How the New System Works

### Admin Side:
1. Go to Admin → Activities
2. Add/Edit/Delete activities, transport, accommodation
3. Set prices, descriptions, display order
4. Toggle active/inactive

### Customer Side:
1. Customer opens `booking-new.html?id=safari&title=Safari&price=100`
2. Sees main package
3. Clicks "Activities" tab → selects multiple activities
4. Clicks "Transport" tab → selects airport transfer
5. Clicks "Accommodation" tab → selects hotel nights
6. Price updates automatically
7. Submits → all items saved to booking
8. Gets confirmation email

### Database:
```
Booking (main booking)
  ├── BookingActivity 1 (Sunset Cruise × 2 people)
  ├── BookingActivity 2 (Bungee Jump × 2 people)
  ├── BookingActivity 3 (Airport Transfer × 1)
  └── BookingActivity 4 (Hotel × 3 nights)
```

---

## 🔍 Troubleshooting

### "Unable to connect to admin"
**Fix**: Start server with `python manage.py runserver`

### "No module named 'activities'"
**Fix**: Run `python manage.py migrate`

### "Activities list empty"
**Fix**: Run `python manage.py shell < populate_activities.py`

### "API returns 404"
**Fix**: Check server is running, check browser console for errors

### "Can't create booking"
**Fix**: 
1. Check server console for errors
2. Open browser console (F12) for JavaScript errors
3. Verify `booking-new.html` is using correct API URL

---

## 📋 Quick Test Checklist

Run through this to verify everything works:

**Backend:**
- [ ] Server starts without errors
- [ ] Can access http://127.0.0.1:8000/admin/
- [ ] Can login to admin
- [ ] Activities app shows in admin
- [ ] Can see list of activities
- [ ] Can create/edit activities

**API:**
- [ ] http://127.0.0.1:8000/api/activities/ shows JSON
- [ ] http://127.0.0.1:8000/api/bookings/create/ accepts POST

**Frontend:**
- [ ] Open `booking-new.html` in browser
- [ ] Activities tab loads items
- [ ] Transport tab loads items
- [ ] Accommodation tab loads items
- [ ] Can select multiple items
- [ ] Price updates correctly
- [ ] Can submit booking
- [ ] Success modal appears
- [ ] Redirects to payment status

**Admin Check:**
- [ ] New booking appears in admin
- [ ] Booking shows all selected activities
- [ ] Total price is correct

---

## 💡 Adding Your Own Activities

### Via Admin Panel (Easy):
1. Go to http://127.0.0.1:8000/admin/
2. Click "Activities" → "Add Activity"
3. Fill in:
   - Activity ID: `unique-id` (no spaces)
   - Title: Display name
   - Category: Activity/Transport/Accommodation
   - Price: Dollar amount
   - Description: Details
   - Duration: How long
4. Click "Save"

### Via Code:
Edit `populate_activities.py` and add to the lists:

```python
activities_list = [
    # Add your activity:
    {'activity_id': 'new-activity', 'title': 'New Activity Name', 
     'category': 'activity', 'price': 99, 
     'duration': '2 hours', 'description': 'Description here'},
]
```

Then run: `python manage.py shell < populate_activities.py`

---

## 🔄 Migration from Old to New System

Your old bookings will still work! They use the old fields (additional_activity_id, etc.).

New bookings will use the new BookingActivity system for unlimited items.

Both systems work side-by-side.

---

## 📞 Still Having Issues?

### Check Server Console:
Look for error messages when server starts or when you submit booking.

### Check Browser Console:
Press F12 in browser, look for red errors.

### Common Errors:

**"CSRF verification failed"**
→ Make sure CORS is configured in settings.py

**"Activity matching query does not exist"**
→ Run `populate_activities.py` again

**"relation 'activities_activity' does not exist"**
→ Run migrations: `python manage.py migrate`

---

## ✅ Final Steps After Everything Works

1. **Update packages.html** - Change booking links to use `booking-new.html`:
   ```html
   <a href="booking-new.html?id=safari&title=Safari&price=100">Reserve</a>
   ```

2. **Configure Email** - Update `.env` file with Gmail settings

3. **Add Your Bank Details** - Update in `bookings/views.py`

4. **Customize Activities** - Add your own via admin panel

5. **Test Everything** - Make a real booking end-to-end

6. **Deploy** - Follow DEPLOYMENT_GUIDE.md

---

## 🎉 You're Ready!

Once the server is running and activities are populated:
- Admin panel: http://127.0.0.1:8000/admin/
- New booking page: Open `booking-new.html`
- API: http://127.0.0.1:8000/api/activities/

**The system now supports unlimited activities, transport, and accommodation! 🚀**
