import datetime

def current_time():
    return datetime.datetime.now()

def clean_text(text):
    return text.strip().lower()
