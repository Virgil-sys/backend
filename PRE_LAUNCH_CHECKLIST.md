# ✅ Praires Africa - Pre-Launch Checklist

## 🔧 Technical Setup

### Backend Setup
- [ ] Installed all dependencies (`pip install -r requirements.txt`)
- [ ] Installed django-jazzmin (`pip install django-jazzmin==2.6.0`)
- [ ] Run migrations (`python manage.py makemigrations && python manage.py migrate`)
- [ ] Created superuser account
- [ ] Collected static files (`python manage.py collectstatic`)
- [ ] Server starts without errors

### Database
- [ ] All migrations applied successfully
- [ ] Additional activity fields added to Booking model
- [ ] Test booking created successfully
- [ ] No database errors in console

### Configuration Files
- [ ] `.env` file created in `backend/` folder
- [ ] `SECRET_KEY` set in `.env`
- [ ] `DEBUG=True` for testing (change to False for production)
- [ ] `ALLOWED_HOSTS` configured

---

## 📧 Email Configuration

### Gmail Setup
- [ ] 2-Step Verification enabled on Gmail account
- [ ] App Password generated (16 characters)
- [ ] `EMAIL_HOST_USER` set in `.env`
- [ ] `EMAIL_HOST_PASSWORD` set in `.env`
- [ ] Test email sent successfully

### Email Testing
- [ ] Create test booking
- [ ] Admin email received at seantakudzwa050505@gmail.com
- [ ] Customer email received
- [ ] HTML formatting displays correctly
- [ ] All links in email work
- [ ] No emails in spam folder

---

## 💰 Bank Details Configuration

### Critical: Update Bank Information
- [ ] Open `backend/bookings/views.py`
- [ ] Find line ~241 (customer email template)
- [ ] Replace placeholder bank details:
  - [ ] Bank Name
  - [ ] Account Name
  - [ ] Account Number
  - [ ] Branch Code
  - [ ] Swift Code
- [ ] Update admin email template (similar section)
- [ ] Test by creating booking and checking email

**Current Placeholders**:
```
Bank Name: Standard Bank
Account Number: 123456789
Branch Code: 123456
Swift Code: SBZAZAJJ
```

---

## 🎨 Frontend Testing

### Booking Flow
- [ ] Open `index.html` - homepage loads
- [ ] Navigate to `packages.html`
- [ ] Click "Reserve" on any package
- [ ] Booking form loads with correct package details
- [ ] All form fields work
- [ ] Additional activity dropdown shows 5 options
- [ ] Price updates when selecting activity
- [ ] Price multiplies correctly by number of people
- [ ] Form validation works (try submitting empty form)
- [ ] Success modal appears after booking
- [ ] Auto-redirects to payment status page

### Payment Status Page
- [ ] Page loads with booking details
- [ ] Status displays correctly
- [ ] Bank details show (if pending)
- [ ] Customer info displays
- [ ] Refresh button works
- [ ] "Back to Packages" link works
- [ ] WhatsApp button works

### Responsive Design
- [ ] Test on desktop browser
- [ ] Test on mobile device (or use browser dev tools)
- [ ] All pages are readable on small screens
- [ ] Buttons are clickable on mobile
- [ ] Forms work on mobile

---

## 🖥️ Admin Panel Testing

### Access & Login
- [ ] Admin panel accessible at `/admin/`
- [ ] Jazzmin theme loads (modern orange/amber design)
- [ ] Login with superuser credentials
- [ ] Dashboard displays properly

### Bookings Management
- [ ] Navigate to "Bookings"
- [ ] List view shows color-coded status badges
- [ ] Search works (try reference number)
- [ ] Filters work (status, payment method, date)
- [ ] Click on booking to view details
- [ ] All fields display correctly
- [ ] Additional activity fields visible
- [ ] Change status dropdown works
- [ ] Save changes works

### Bulk Actions
- [ ] Select multiple bookings
- [ ] Use bulk action: "Mark as Confirmed"
- [ ] Verify status changed
- [ ] Try other bulk actions

### Customer Management
- [ ] Navigate to "Customers"
- [ ] View customer list
- [ ] Search by name/email works
- [ ] Customer details display correctly

---

## 🔐 Security Checks

### Environment Variables
- [ ] No sensitive data hardcoded in code
- [ ] `.env` file exists and populated
- [ ] `.env` in `.gitignore` (don't commit to Git)
- [ ] Strong `SECRET_KEY` generated

### Production Settings (Before Going Live)
- [ ] `DEBUG=False` in production `.env`
- [ ] `ALLOWED_HOSTS` includes your domain
- [ ] `CORS_ALLOWED_ORIGINS` configured correctly
- [ ] `CSRF_TRUSTED_ORIGINS` includes your domain
- [ ] HTTPS enabled (via hosting platform)

### Access Control
- [ ] Strong admin password set
- [ ] Only authorized users have admin access
- [ ] Admin panel not publicly accessible without login

---

## 📱 Integration Testing

### Email Flow
- [ ] Customer books package
- [ ] Admin receives notification email immediately
- [ ] Customer receives confirmation email immediately
- [ ] Emails contain correct information
- [ ] Bank details correct in customer email
- [ ] Reference numbers match

### Status Updates
- [ ] Booking created with "Pending" status
- [ ] Admin changes to "Confirmed" in admin panel
- [ ] Status updates in database
- [ ] Payment status page shows "Confirmed" when refreshed

### Additional Activities
- [ ] Select additional activity when booking
- [ ] Total price calculates correctly
- [ ] Both main and additional activity saved in database
- [ ] Admin can see additional activity in booking details
- [ ] Email shows both activities (if applicable)

---

## 🚀 Deployment Preparation

### Code Ready
- [ ] All features tested locally
- [ ] No console errors in browser
- [ ] No errors in Django console
- [ ] All tests passing

### Documentation
- [ ] Read `DEPLOYMENT_GUIDE.md`
- [ ] Chosen hosting platform
- [ ] Domain name ready (optional)
- [ ] SSL certificate plan (usually automatic)

### Backups
- [ ] Export current database: `python manage.py dumpdata > backup.json`
- [ ] Backup all code files
- [ ] Save `.env` file securely (don't lose passwords!)

---

## 📊 Final Verification

### Feature Completeness
- [ ] ✅ Email automation working
- [ ] ✅ Payment status page functional
- [ ] ✅ Additional activities feature working
- [ ] ✅ Dynamic pricing calculating correctly
- [ ] ✅ Success messages displaying
- [ ] ✅ Admin panel customized and working
- [ ] ✅ All bank details updated

### User Experience
- [ ] Booking process is smooth
- [ ] Emails are professional and clear
- [ ] Status page is informative
- [ ] Admin panel is easy to use
- [ ] Mobile experience is good

### Performance
- [ ] Pages load quickly
- [ ] No slow database queries
- [ ] Images optimized
- [ ] Server responds promptly

---

## 🎯 Launch Day Checklist

### Final Steps Before Launch
1. [ ] Change `DEBUG=False`
2. [ ] Update `ALLOWED_HOSTS`
3. [ ] Run `collectstatic`
4. [ ] Test on production server
5. [ ] Create real admin account (not test)
6. [ ] Delete test bookings from database

### Post-Launch Monitoring
- [ ] Monitor first few bookings closely
- [ ] Check emails are being sent
- [ ] Watch for any errors in logs
- [ ] Test customer journey end-to-end
- [ ] Verify payment confirmations work

### Marketing Ready
- [ ] Share website URL
- [ ] Test booking from external device
- [ ] Announce on social media
- [ ] Add WhatsApp number to marketing materials

---

## 📞 Support Information

### If Something Goes Wrong

**Check These First**:
1. Django console for error messages
2. Browser console (F12) for JavaScript errors
3. Email configuration in `.env`
4. Database migrations are applied

**Get Help**:
- 📧 Email: seantakudzwa050505@gmail.com
- 📱 WhatsApp: +263 77 693 0966
- 📚 Documentation: `DEPLOYMENT_GUIDE.md`
- 🔍 Troubleshooting: See guide Section "Troubleshooting"

---

## ✨ Congratulations!

Once all items are checked, you're ready to launch! 🎉

Your Praires Africa Booking System includes:
- Professional email notifications
- Modern admin interface
- Dynamic pricing with add-ons
- Real-time payment tracking
- Mobile-responsive design
- Secure payment processing

**Ready to welcome your first customers!**

---

**Last Updated**: January 2025
**Version**: 2.0 (With all new features)
