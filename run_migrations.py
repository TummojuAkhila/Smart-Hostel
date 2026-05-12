#!/usr/bin/env python
import os
import sys
import django

# Add project to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_hostel.settings')
django.setup()

# Run migrations
from django.core.management import call_command

print("Creating migrations...")
call_command('makemigrations', 'hostel', verbosity=2)

print("\nApplying migrations...")
call_command('migrate', verbosity=2)

print("\nMigrations complete!")
