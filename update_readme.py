#!/usr/bin/env python3
from datetime import datetime, timedelta
import re

START_DATE = datetime(2024, 7, 2) 
README_FILE = "README.MD"

def calculate_days_of_experience():
    """Calculate days since start date"""
    today = datetime.now()
    delta = today - START_DATE
    return delta.days

def get_current_year():
    """Get current year"""
    return datetime.now().year

def update_readme():
    """Update README with current information"""
    with open(README_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    days = calculate_days_of_experience()
    content = re.sub(
        r'- \*\*\d+ days\*\* of experience',
        f'- **{days} days** of experience',
        content
    )
    
    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ README updated successfully!")
    print(f"📅 Days of experience: {days}")

if __name__ == "__main__":
    update_readme()
