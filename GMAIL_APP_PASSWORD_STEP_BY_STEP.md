# 🔑 Gmail App Password - Complete Step-by-Step Guide

## 📋 Before We Start

**What you'll need:**
- Your Gmail: **seantakudzwa050505@gmail.com**
- Your Gmail password
- Your phone (for verification)
- 10 minutes

**Let's do this together!** 🚀

---

# PART 1: Enable 2-Step Verification (REQUIRED!)

## Step 1: Go to Google Account

**Click this link:**
```
https://myaccount.google.com
```

**What you'll see:**
- Google Account page
- Your profile picture in top right
- Menu on left side

**Action:** Make sure you're signed in with **seantakudzwa050505@gmail.com**

---

## Step 2: Click on "Security"

**Where to find it:**
- Look at LEFT side menu
- Find "Security" (it has a shield 🛡️ icon)
- Click on it

**Or use direct link:**
```
https://myaccount.google.com/security
```

---

## Step 3: Find "2-Step Verification"

**Scroll down on Security page until you see:**

**Section heading:** "How you sign in to Google"

**Under this section, look for:**
- Password
- 2-Step Verification
- Passkeys

**What does it say next to "2-Step Verification"?**

### If it says "OFF" or "Get Started":
✅ **GOOD!** Continue to Step 4!

### If it says "ON" or shows checkmark ✓:
✅ **PERFECT!** Skip to PART 2 (You already have it enabled!)

---

## Step 4: Click on "2-Step Verification"

**Click the text** "2-Step Verification"

**Or click the "GET STARTED" button**

**What happens next:**
- New page opens
- Title says "Protect your account with 2-Step Verification"
- Blue "GET STARTED" button

**Action:** Click the blue **"GET STARTED"** button

---

## Step 5: Enter Your Password

**What you see:**
- Google logo at top
- "Enter your password"
- Password field
- Blue "Next" button

**Action:**
1. Type your Gmail password
2. Click blue "Next" button

---

## Step 6: Add Your Phone Number

**What you see:**
- "Get verification codes"
- Phone number field
- Two options:
  - Text message (SMS) ← **Choose this one!**
  - Phone call

**Action:**
1. Enter your phone number (e.g., +263 77693096)
2. Make sure "Text message (SMS)" is selected
3. Click blue "Send" button

---

## Step 7: Enter Verification Code

**What happens:**
- You receive SMS with 6-digit code
- Example: "123456"

**What you see on screen:**
- "Enter the code we sent to +263 77693096"
- 6 boxes for entering code
- "Next" button

**Action:**
1. Check your phone for SMS
2. Type the 6-digit code
3. Click "Next"

---

## Step 8: Confirm 2-Step Verification

**What you see:**
- "Turn on 2-Step Verification?"
- Explanation text
- Blue "TURN ON" button

**Action:**
1. Click the blue **"TURN ON"** button
2. Wait for confirmation

**Success message appears:**
- "2-Step Verification is on"
- Checkmark ✓ icon

**Action:** Click "Done" or "Got it"

---

## ✅ PART 1 COMPLETE!

**2-Step Verification is now ON!** 🎉

**IMPORTANT:** Wait 5 minutes before continuing to Part 2!

**Why wait?** Google needs time to activate this feature on your account.

**Meanwhile:**
- ☕ Get some water
- 📱 Check your messages
- 🎵 Listen to music
- ⏰ Set timer for 5 minutes

---

# PART 2: Generate App Password (After 5 Minutes!)

## Step 9: Go Back to Security Page

**After waiting 5 minutes, click this link:**
```
https://myaccount.google.com/security
```

**Action:** Make sure you're still signed in

---

## Step 10: Find "App passwords"

**Scroll down to section:** "How you sign in to Google"

**Look for these items (in order):**
1. Password
2. 2-Step Verification ← Should show "ON" now ✓
3. **App passwords** ← Look for this!

**What you see:**
- "App passwords" text
- Arrow → on the right
- It might say "Not available" if you just enabled 2-Step (wait longer!)

**If you DON'T see "App passwords" at all:**
- Try direct link: https://myaccount.google.com/apppasswords
- Or wait another 5 minutes and refresh page

**Action:** Click on **"App passwords"**

---

## Step 11: Sign In Again (Security Check)

**What you see:**
- "Enter your password"
- Password field

**Action:**
1. Enter your Gmail password again
2. Click "Next"

---

## Step 12: Select App

**What you see:**
- "Select app" dropdown menu
- Currently shows "Select app"

**Action:**
1. Click the dropdown
2. Scroll down
3. Find **"Mail"**
4. Click "Mail"

---

## Step 13: Select Device

**What you see:**
- "Select device" dropdown menu (appears after choosing app)
- Currently shows "Select device"

**Action:**
1. Click the dropdown
2. Find **"Windows Computer"**
3. Click "Windows Computer"

**Alternative:** If you don't see "Windows Computer", choose "Other (Custom name)"
- Type: "Prairies Backend"
- Click "Generate"

---

## Step 14: Click "Generate"

**What you see:**
- Blue "GENERATE" button

**Action:**
1. Click the **"GENERATE"** button
2. Wait 2 seconds

---

## Step 15: COPY YOUR APP PASSWORD!

**What you see:**
- Yellow box appears
- Title: "Your app password for your device"
- **16-character password in a box** like:
  ```
  abcd efgh ijkl mnop
  ```
- "Done" button

**SUPER IMPORTANT - DO THIS NOW:**

1. **SELECT** all 16 characters (click and drag)
2. **COPY** them (Ctrl + C)
3. **PASTE** into Notepad immediately
4. **SAVE** the Notepad file

**Remove the spaces!**
- From: `abcd efgh ijkl mnop`
- To: `abcdefghijklmnop`

**Save this password! You'll NEVER see it again!**

---

## Step 16: Click "Done"

**Action:**
1. After copying password, click **"Done"**
2. Window closes

**You did it!** ✅

---

# PART 3: Add Password to Your Website

## Step 17: Open .env File

**Using File Explorer:**
1. Open: `C:\Users\sean\Desktop\my website\backend`
2. Find: `.env` file
3. Right-click → Open with → Notepad

**Or in VS Code:**
1. File → Open File
2. Navigate to backend folder
3. Select `.env`

---

## Step 18: Find EMAIL_HOST_PASSWORD Line

**Look for line 13:**
```
EMAIL_HOST_PASSWORD=
```

**It's empty after the = sign**

---

## Step 19: Paste Your App Password

**Change from:**
```
EMAIL_HOST_PASSWORD=
```

**To:**
```
EMAIL_HOST_PASSWORD=abcdefghijklmnop
```

**IMPORTANT RULES:**
- ✅ NO spaces in password
- ✅ NO quotes around password
- ✅ Directly after the = sign
- ✅ All lowercase letters (doesn't matter if yours are uppercase)

**Example of what it should look like:**
```
EMAIL_HOST_PASSWORD=abcdefghijklmnop
```

---

## Step 20: Save the File

**Action:**
1. Click File → Save
2. Or press `Ctrl + S`
3. Close Notepad/VS Code

**✅ Password is now saved!**

---

# PART 4: Restart Server & Test

## Step 21: Stop Current Server

**Find your server window** (the green/black window with server running)

**Action:**
1. Click on the window
2. Press `Ctrl + C` (both keys together)
3. Or just close the window with X button

**Server stops!**

---

## Step 22: Start Server Again

**Action:**
1. Find: `START_SERVER_FOREVER.bat`
2. Double-click it
3. Wait for: `Starting development server at http://127.0.0.1:8000/`

**Server is now running with NEW password!** ✅

---

## Step 23: Make Test Booking

**Action:**
1. Open your booking form in browser
2. Fill in details:
   - Name: Your name
   - Email: **seantakudzwa050505@gmail.com** (YOUR email!)
   - Phone: Your phone
   - Number of people: 1
   - Date: Tomorrow
3. Click **"Book Now"**
4. Wait for success message

---

## Step 24: Check Your Gmail!

**Action:**
1. Go to: https://mail.google.com
2. Sign in with: seantakudzwa050505@gmail.com
3. Look at inbox (refresh if needed)

**What you should see:**
- **New email!** 📧
- Subject: "New Booking: [Package Name]"
- From: Prairies Africa

**Open the email and read it!**

**If you see this email = IT WORKS!** 🎉🎉🎉

---

# 🎊 COMPLETE SUCCESS CHECKLIST

After following all steps, check these:

- [ ] 2-Step Verification is ON (green checkmark in Google Account)
- [ ] App Password generated (16 characters)
- [ ] App Password saved in Notepad (backup!)
- [ ] Password added to `.env` file (line 13)
- [ ] No spaces in password
- [ ] `.env` file saved
- [ ] Server restarted
- [ ] Test booking made
- [ ] Email received in Gmail inbox
- [ ] Email contains booking details

**All checked? YOU DID IT!** 🎊

---

# 🚨 Troubleshooting

## Problem: Can't find "App passwords" option

**Solution 1:** Wait longer
- 2-Step Verification needs time to activate
- Wait 10-15 minutes
- Refresh page

**Solution 2:** Use direct link
```
https://myaccount.google.com/apppasswords
```

**Solution 3:** Sign out and back in
- Sign out of Google completely
- Close browser
- Open browser again
- Sign in
- Try again

---

## Problem: "This setting is not available for your account"

**Reason:** Your account type doesn't support it

**Is it a Work/School account?**
- Contact your IT administrator
- Or use personal Gmail instead

**Is it a brand new account?**
- Wait 24 hours after creating account
- Try again tomorrow

---

## Problem: No email received after test booking

**Check 1:** Is server running?
- Look for green server window
- Should show "Starting development server..."

**Check 2:** Password correct in .env?
- Open `.env` file
- Check line 13: `EMAIL_HOST_PASSWORD=your16chars`
- No spaces? No quotes?

**Check 3:** Did you restart server?
- Server must restart after changing .env
- Close and open again

**Check 4:** Check spam folder
- Gmail might put it in spam first
- Mark as "Not Spam"

**Check 5:** Wait a minute
- Emails can take 30-60 seconds
- Refresh your Gmail

---

## Problem: Server shows email error

**Look at server window, do you see:**
```
SMTPAuthenticationError
```

**This means:**
- Password is wrong
- Or not added to .env correctly

**Fix:**
1. Check password in .env (no typos?)
2. Generate NEW app password
3. Replace in .env
4. Restart server

---

# 📝 Quick Reference

## Important Links:

**Google Account Security:**
```
https://myaccount.google.com/security
```

**App Passwords Direct:**
```
https://myaccount.google.com/apppasswords
```

**Gmail:**
```
https://mail.google.com
```

## Files to Edit:

**Email configuration:**
```
C:\Users\sean\Desktop\my website\backend\.env
```

**Line to change:**
```
Line 13: EMAIL_HOST_PASSWORD=your16digitpassword
```

## Commands:

**Restart server:**
```
Close window, then double-click: START_SERVER_FOREVER.bat
```

---

# 🎯 Summary

**What we did:**
1. ✅ Enabled 2-Step Verification on Gmail
2. ✅ Generated 16-character App Password
3. ✅ Added password to `.env` file
4. ✅ Restarted server
5. ✅ Tested with booking
6. ✅ Received email!

**What you have now:**
- ✅ Secure email setup
- ✅ Automatic notifications for every booking
- ✅ Professional booking system!

---

**Time to complete:** 15-20 minutes

**Difficulty:** Medium (but we did it together!)

**Result:** AMAZING! 🎊

---

**🎉 YOU NOW HAVE A COMPLETE BOOKING SYSTEM WITH EMAIL NOTIFICATIONS! 🎉**

**Every booking → Email to your inbox automatically!** 📧✨
