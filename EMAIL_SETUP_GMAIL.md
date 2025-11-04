# 📧 Email Setup - Get Booking Notifications!

## 🎈 What This Does (Simple!)

**When someone books a safari:**
1. ✅ They fill booking form
2. ✅ Booking saved to database
3. ✅ **EMAIL SENT TO YOU!** 📧
4. ✅ You get all booking details
5. ✅ Customer also gets confirmation email!

**Like getting a text message every time someone orders!** 📱

---

## ⚡ Quick Setup (5 Minutes!)

### Step 1: Get Gmail App Password (2 minutes)

**Why?** Gmail needs special password for apps (not your normal password!)

**How to get it:**

1. Go to: **https://myaccount.google.com/security**
2. Make sure "2-Step Verification" is ON
   - If not, turn it on first!
3. Scroll down to "App passwords"
4. Click "App passwords"
5. Select:
   - App: "Mail"
   - Device: "Windows Computer"
6. Click "Generate"
7. **Copy the 16-character password** (like: `abcd efgh ijkl mnop`)
8. Save it somewhere!

---

### Step 2: Add Password to .env File (1 minute)

1. Open: `C:\Users\sean\Desktop\my website\backend\.env`
2. Find this line:
   ```
   EMAIL_HOST_PASSWORD=
   ```
3. Change to:
   ```
   EMAIL_HOST_PASSWORD=abcd efgh ijkl mnop
   ```
   (Use YOUR app password from Step 1!)
4. **Save the file!** (Ctrl + S)

---

### Step 3: Restart Server (30 seconds)

**Why?** Server needs to load new password!

1. Close current server window (or Ctrl + C)
2. Double-click: `START_SERVER_FOREVER.bat`
3. Wait for: `Starting development server at http://127.0.0.1:8000/`
4. Done!

---

### Step 4: Test It! (1 minute)

1. Open your booking form
2. Fill in details:
   - Your name
   - **seantakudzwa050505@gmail.com** as email
   - Phone number
   - Pick a package
3. Click "Book Now"
4. **Check your Gmail inbox!** 📧
5. You should see email: "New Booking - Prairies Africa"

**If you see the email = IT WORKS!** 🎉

---

## 📧 What Emails You'll Get

### Email 1: Admin Notification (TO YOU)

**Subject:** New Booking: [Package Name]

**You get:**
- Customer name
- Customer email
- Customer phone
- Number of people
- Preferred date
- Special requests
- Package details
- Total price
- Booking reference number

**Sent to:** seantakudzwa050505@gmail.com

---

### Email 2: Customer Confirmation (TO CUSTOMER)

**Subject:** Booking Confirmation - Prairies Africa

**Customer gets:**
- Booking reference number
- Package details
- Bank payment instructions
- Your contact info
- Next steps

**Sent to:** [Customer's email from form]

---

## 🎯 Example Email You'll Receive

```
From: Prairies Africa <seantakudzwa050505@gmail.com>
To: seantakudzwa050505@gmail.com
Subject: New Booking: Victoria Falls Guided Tour

New booking received!

Customer Details:
------------------
Name: John Smith
Email: john@example.com
Phone: +1234567890

Booking Details:
------------------
Package: Victoria Falls Guided Tour
Number of People: 2
Preferred Date: 2025-12-15
Special Requests: Vegetarian meals

Reference: BK-20251103-001

Please login to admin panel to manage this booking:
http://127.0.0.1:8000/admin
```

---

## 🚨 Troubleshooting

### Problem: No emails received

**Check 1: App Password Correct?**
- Open `.env` file
- Check `EMAIL_HOST_PASSWORD=` has your app password
- No spaces, no quotes

**Check 2: Server Restarted?**
- After adding password, you MUST restart server
- Close and reopen server window

**Check 3: Gmail Spam Folder?**
- Check your spam/junk folder
- Mark as "Not Spam"

**Check 4: 2-Step Verification On?**
- Gmail requires 2FA for app passwords
- Turn it on in Google Account settings

---

### Problem: "Authentication failed" error

**Fix:**
1. Delete app password in Google
2. Generate NEW app password
3. Copy it carefully (all 16 characters)
4. Paste in .env file
5. Restart server

---

### Problem: Emails go to spam

**Fix:**
1. Open spam folder
2. Find Prairies Africa email
3. Click "Not Spam"
4. Create filter: Never send to spam

---

## 💡 Pro Tips

### Tip 1: Test Before Going Live
- Send test booking to yourself
- Make sure email arrives
- Check all details are correct

### Tip 2: Check Email Daily
- Morning: Check for overnight bookings
- Evening: Check for day bookings
- Set phone notification for Gmail!

### Tip 3: Save Email Template
- Emails are automatic
- No need to reply manually
- Use admin panel to manage bookings

### Tip 4: Multiple Email Addresses
Want notifications to multiple emails?
- Use Gmail forwarding
- Or ask me to add multiple recipients!

---

## ✅ Current Configuration

**Your email:** seantakudzwa050505@gmail.com

**SMTP Server:** smtp.gmail.com

**Port:** 587

**Security:** TLS (secure)

**Status:** 
- ✅ Configured
- ⏳ Waiting for app password
- ⏳ Needs server restart

---

## 🎯 Quick Checklist

Before emails work:

- [ ] Turn on 2-Step Verification in Gmail
- [ ] Generate App Password
- [ ] Add password to `.env` file
- [ ] Save `.env` file
- [ ] Restart server
- [ ] Test booking with your email
- [ ] Check Gmail inbox
- [ ] Verify email received

**All checked? Emails are working!** ✅

---

## 📱 Mobile Notifications

**Want instant notifications on your phone?**

1. Install Gmail app on phone
2. Turn on notifications for Gmail
3. Every booking = Phone notification! 📱
4. Even when away from computer!

---

## 🎊 You're All Set!

**What happens now:**

```
Customer fills form
       ↓
Clicks "Book Now"
       ↓
Booking saved to database
       ↓
📧 EMAIL TO YOU! (All details)
       ↓
📧 EMAIL TO CUSTOMER! (Confirmation)
       ↓
You check email
       ↓
Login to admin panel
       ↓
Verify payment when received
       ↓
Customer goes on safari! 🦁
```

**Never miss a booking!** 🎉

---

**🦁 Now go setup your app password and test it! 🦁**
