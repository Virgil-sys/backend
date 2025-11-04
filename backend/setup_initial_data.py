"""
Quick setup script to initialize admin user and seed bank accounts.
Run with: python manage.py shell < setup_initial_data.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth import get_user_model
from payments.models import BankAccount

User = get_user_model()

# Create or update admin user with password "admin123"
admin_user, created = User.objects.get_or_create(
    username='admin',
    defaults={
        'email': 'admin@prairiesafrica.com',
        'is_staff': True,
        'is_superuser': True,
    }
)
admin_user.set_password('admin123')
admin_user.is_staff = True
admin_user.is_superuser = True
admin_user.save()
print(f"✓ Admin user {'created' if created else 'updated'}: username='admin', password='admin123'")

# Seed 2 bank accounts
bank_accounts = [
    {
        'bank_name': 'First National Bank (FNB)',
        'account_name': 'Prairies Africa Tours',
        'account_number': '62812345678',
        'branch_code': '250655',
        'swift_code': 'FIRNZAJJ',
        'currency': 'ZAR',
        'is_active': True,
        'notes': 'Primary business account for ZAR payments',
    },
    {
        'bank_name': 'Standard Bank',
        'account_name': 'Prairies Africa International',
        'account_number': '123456789',
        'branch_code': '051001',
        'swift_code': 'SBZAZAJJ',
        'currency': 'USD',
        'is_active': True,
        'notes': 'International payments account',
    },
]

for acct_data in bank_accounts:
    acct, created = BankAccount.objects.get_or_create(
        account_number=acct_data['account_number'],
        defaults=acct_data
    )
    print(f"✓ Bank account {'created' if created else 'exists'}: {acct.bank_name} - {acct.account_number}")

print("\n🎉 Setup complete!")
print("Admin URL: http://127.0.0.1:8000/admin")
print("Username: admin")
print("Password: admin123")
