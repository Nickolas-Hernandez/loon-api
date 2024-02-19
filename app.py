from flask import Flask
from flask_caching import Cache
from datetime import datetime, timedelta
import math
# import psycopg2

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)

app.config.from_mapping(config)
cache = Cache(app)

# conn = psycopg2.connect("dbname=loon_db user=nickhernandez")
# cur = conn.cursor()
# cur.execute("SELECT * FROM loon_db")
# records = cur.fetchall()

@app.route('/')
def moonPhase():
    # Date of a known new moon: January 6, 2000
    known_new_moon = datetime(2000, 1, 6)
    # Current UTC time
    now = datetime.utcnow()
    # Difference in days from the known new moon
    days_since_new_moon = (now - known_new_moon).days + (now - known_new_moon).seconds / 86400
    # The moon's age in the current cycle
    moon_age = days_since_new_moon % 29.53

    if moon_age < 7.4:
        return "New Moon" if moon_age < 1.5 else "Waxing Crescent"
    elif moon_age < 14.8:
        return "First Quarter" if moon_age < 8.9 else "Waxing Gibbous"
    elif moon_age < 22.1:
        return "Full Moon" if moon_age < 16.9 else "Waning Gibbous"
    else:
        return "Last Quarter" if moon_age < 24.6 else "Waning Crescent"

@app.route('/aboutme')
def about_me():
    return"<h1>This is an about me page</h1>" 
    