# Frontend Integration Guide

## Quick Start

Your backend is now running at: **http://127.0.0.1:8000**

## Available API Endpoints

### 1. Create a Booking
**Endpoint:** `POST http://127.0.0.1:8000/api/bookings/create/`

**What it does:** Customer books a tour package

**Request Body (JSON):**
```json
{
  "customer": {
    "name": "John Smith",
    "email": "john@example.com",
    "phone": "+27 11 123 4567",
    "customer_notes": "Vegetarian meals required"
  },
  "package_id": "PKG001",
  "package_title": "3-Day Safari Adventure",
  "package_price": "2500.00",
  "number_of_people": 2,
  "preferred_date": "2025-12-15",
  "payment_method": "bank_transfer",
  "special_requests": "Window seats preferred"
}
```

**Response:** Full booking details including:
- `id` - Booking ID
- `reference_number` - Use this for payment!
- `total_amount` - Calculated automatically
- `payment_deadline` - 48 hours from now
- `status` - Will be "pending"

---

### 2. Get Booking Details
**Endpoint:** `GET http://127.0.0.1:8000/api/bookings/{id}/`

**What it does:** Fetch full booking information

**Example:** `GET http://127.0.0.1:8000/api/bookings/1/`

---

### 3. Check Booking Status
**Endpoint:** `GET http://127.0.0.1:8000/api/bookings/{id}/status/`

**What it does:** Quick status check (lighter than full details)

**Response:**
```json
{
  "id": 1,
  "status": "pending",
  "reference_number": "BK-20251103151045-1"
}
```

---

### 4. Get Bank Transfer Details
**Endpoint:** `POST http://127.0.0.1:8000/api/payments/bank-details/`

**What it does:** Get active bank accounts for payment instructions

**Response:**
```json
{
  "accounts": [
    {
      "id": 1,
      "bank_name": "First National Bank (FNB)",
      "account_name": "Prairies Africa Tours",
      "account_number": "62812345678",
      "branch_code": "250655",
      "swift_code": "FIRNZAJJ",
      "currency": "ZAR",
      "notes": "Primary business account for ZAR payments"
    },
    {
      "id": 2,
      "bank_name": "Standard Bank",
      "account_name": "Prairies Africa International",
      "account_number": "123456789",
      "branch_code": "051001",
      "swift_code": "SBZAZAJJ",
      "currency": "USD",
      "notes": "International payments account"
    }
  ],
  "instructions": {
    "message": "Use your booking reference as the payment reference to speed up verification.",
    "deadline_hours": 48
  }
}
```

**Frontend Display:**
- Show bank accounts in a nice card/list
- Display the booking reference prominently
- Remind customer to use reference in their bank transfer
- Show the 48-hour deadline

---

### 5. Upload Proof of Payment
**Endpoint:** `POST http://127.0.0.1:8000/api/payments/upload-proof/`

**What it does:** Customer uploads payment receipt/screenshot

**Content-Type:** `multipart/form-data`

**Form Fields:**
- `booking_id` or `reference_number` (required, pick one)
- `proof` (required) - File upload (JPG, PNG, or PDF, max 5MB)
- `amount_received` (optional) - Decimal
- `transfer_date` (optional) - Date (YYYY-MM-DD)

**Example using JavaScript Fetch:**
```javascript
const formData = new FormData();
formData.append('booking_id', '1');
formData.append('proof', fileInput.files[0]); // File from <input type="file">
formData.append('amount_received', '5000.00');
formData.append('transfer_date', '2025-11-03');

fetch('http://127.0.0.1:8000/api/payments/upload-proof/', {
  method: 'POST',
  body: formData
})
.then(res => res.json())
.then(data => console.log(data));
```

**Response:**
```json
{
  "message": "Proof uploaded. We will verify your payment shortly.",
  "transfer": {
    "id": 1,
    "status": "pending",
    "reference_number": "BK-20251103151045-1",
    ...
  }
}
```

**File Validation:**
- Allowed: JPG, PNG, PDF
- Max size: 5MB
- Stored securely in backend

---

### 6. Check Payment Status
**Endpoint:** `GET http://127.0.0.1:8000/api/payments/payment-status/{booking_id}/`

**What it does:** Check if payment has been verified

**Example:** `GET http://127.0.0.1:8000/api/payments/payment-status/1/`

**Response:**
```json
{
  "booking_id": 1,
  "booking_status": "confirmed",
  "payment_status": "verified",
  "reference_number": "BK-20251103151045-1"
}
```

**Payment Status Values:**
- `null` - No proof uploaded yet
- `"pending"` - Proof uploaded, waiting for admin verification
- `"verified"` - Payment confirmed by admin
- `"failed"` - Payment rejected

**Booking Status Values:**
- `"pending"` - Waiting for payment
- `"confirmed"` - Payment verified, booking confirmed
- `"cancelled"` - Booking cancelled
- `"completed"` - Tour completed

---

## Frontend Flow Example

### Booking Flow:
1. **Customer fills booking form** → Call `POST /api/bookings/create/`
2. **Show confirmation page** with:
   - Booking reference number (BIG and bold!)
   - Total amount
   - Payment deadline
3. **Show bank details** → Call `POST /api/payments/bank-details/`
4. **Customer makes bank transfer** (outside your system)
5. **Customer uploads proof** → Call `POST /api/payments/upload-proof/`
6. **Show "waiting for verification" message**
7. **Poll payment status** → Call `GET /api/payments/payment-status/{id}/` every 30 seconds
8. **When verified** → Show success message and booking details

---

## CORS Configuration

Your backend already allows:
- `https://prairiesafrica.com`
- `https://www.prairiesafrica.com`
- `http://localhost:3000`

If you're developing on a different port, add it to `backend/backend/settings.py`:
```python
CORS_ALLOWED_ORIGINS = [
    'https://prairiesafrica.com',
    'https://www.prairiesafrica.com',
    'http://localhost:3000',
    'http://localhost:5173',  # Add your dev port
]
```

---

## Error Handling

All endpoints return standard HTTP status codes:
- `200` - Success (GET requests)
- `201` - Created (POST create booking/upload)
- `400` - Bad request (validation errors)
- `404` - Not found
- `500` - Server error

**Error Response Format:**
```json
{
  "detail": "Error message",
  "field_name": ["Field-specific error"]
}
```

---

## Testing Your Integration

Use these sample data for testing:

**Test Booking:**
```json
{
  "customer": {
    "name": "Test Customer",
    "email": "test@example.com",
    "phone": "+27 11 111 1111"
  },
  "package_id": "TEST001",
  "package_title": "Test Safari",
  "package_price": "1000.00",
  "number_of_people": 1,
  "preferred_date": "2025-12-25"
}
```

**Test with curl:**
```bash
curl -X POST http://127.0.0.1:8000/api/bookings/create/ \
  -H "Content-Type: application/json" \
  -d '{"customer": {"name": "Test", "email": "test@test.com"}, "package_id": "TEST", "package_title": "Safari", "package_price": "1000", "number_of_people": 1}'
```

---

## Email Notifications

Currently enabled (sent automatically):
1. **New Booking** → Email to admin
2. **Booking Confirmation** → Email to customer with bank details

To configure email, edit `.env`:
```env
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=no-reply@prairiesafrica.com
```

---

## Production Deployment

When deploying to production:

1. **Update `.env`:**
   ```env
   DEBUG=False
   ALLOWED_HOSTS=prairiesafrica.com,www.prairiesafrica.com
   SECRET_KEY=generate-strong-secret-key
   DATABASE_URL=postgres://user:pass@host:5432/dbname
   ```

2. **Collect static files:**
   ```bash
   python manage.py collectstatic
   ```

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Use Gunicorn (included in requirements.txt):**
   ```bash
   gunicorn backend.wsgi:application --bind 0.0.0.0:8000
   ```

---

## Need Help?

- Check Django server logs in terminal
- Test endpoints with Postman or curl
- Visit admin panel: http://127.0.0.1:8000/admin (username: `admin`, password: `admin123`)
