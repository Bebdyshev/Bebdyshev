#!/usr/bin/env python3
"""
Script to automatically update README.md with dynamic content
"""
from datetime import datetime, timedelta
import re

# Configuration
START_DATE = datetime(2024, 7, 2) # Adjust this to your actual start date
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
    
    # Update days of experience
    days = calculate_days_of_experience()
    content = re.sub(
        r'- \*\*\d+ days\*\* of experience',
        f'- **{days} days** of experience',
        content
    )
    
    # You can add more dynamic updates here, for example:
    # - Update current date
    # - Update project status
    # - Update statistics
    
    # Example: Add last updated timestamp (optional)
    # You can uncomment this if you want to show when README was last updated
    # today_str = datetime.now().strftime('%B %d, %Y')
    # if '<!-- LAST_UPDATED:' in content:
    #     content = re.sub(
    #         r'<!-- LAST_UPDATED:.*?-->',
    #         f'<!-- LAST_UPDATED: {today_str} -->',
    #         content
    #     )
    # else:
    #     content += f'\n\n<!-- LAST_UPDATED: {today_str} -->'
    
    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ README updated successfully!")
    print(f"📅 Days of experience: {days}")

if __name__ == "__main__":
    update_readme()
